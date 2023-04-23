from importlib import metadata

from model_w.env_manager import EnvManager
from model_w.preset.django import ModelWDjango

REST_FRAMEWORK = {}


def get_package_version() -> str:
    """
    Trying to get the current package version using the metadata module. This
    assumes that the version is indeed set in pyproject.toml and that the
    package was cleanly installed.
    """

    try:
        return metadata.version("end_to_end_tester")
    except metadata.PackageNotFoundError:
        return "0.0.0"


with EnvManager(ModelWDjango()) as env:
    # ---
    # Apps
    # ---

    INSTALLED_APPS = [
        "drf_spectacular",
        "drf_spectacular_sidecar",
        "end_to_end_tester.apps.cms",
        "end_to_end_tester.apps.people",
    ]

    # ---
    # Plumbing
    # ---

    ROOT_URLCONF = "end_to_end_tester.django.urls"

    WSGI_APPLICATION = "end_to_end_tester.django.wsgi.application"

    # ---
    # Auth
    # ---

    AUTH_USER_MODEL = "people.User"

    # ---
    # i18n
    # ---

    LANGUAGES = [
        ("en", "English"),
    ]

    # ---
    # OpenAPI Schema
    # ---

    REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

    SPECTACULAR_SETTINGS = {
        "TITLE": "End To End Tester",
        "VERSION": get_package_version(),
        "SERVE_INCLUDE_SCHEMA": False,
        "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
        "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
        "REDOC_DIST": "SIDECAR",
    }

    # ---
    # Wagtail
    # ---

    WAGTAIL_SITE_NAME = "End To End Tester"
    WAGTAILIMAGES_IMAGE_MODEL = "cms.CustomImage"
    WAGTAILDOCS_DOCUMENT_MODEL = "cms.CustomDocument"

    # ---
    # S3 for local development
    # Overwrite AWS URLs with local S3 and use HTTP
    # ---
    if env.get("STORAGES", None) == "local":
        # Upload S3 URL inc scheme eg. "http://localhost:9099"
        AWS_S3_ENDPOINT_URL = env.get("AWS_S3_ENDPOINT_URL")

        # Download bucket URL excluding scheme eg. "localhost:9099/mybucket"
        AWS_S3_CUSTOM_DOMAIN = env.get("AWS_S3_CUSTOM_DOMAIN")

        # Download URL scheme eg. "http:"
        AWS_S3_URL_PROTOCOL = env.get("AWS_S3_URL_PROTOCOL")

    AUTHENTICATION_BACKENDS = [
        "end_to_end_tester.apps.people.authentication.EmailBackend"
    ]

    DEFAULT_AUTHENTICATION_CLASSES = [
        "rest_framework.authentication.BasicAuthentication",
    ]
