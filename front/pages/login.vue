<template>
    <div class="container">
        <UserMessage ref="messageComponent" />
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="email">Email</label>
                <input id="email" v-model="email" type="text" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input id="password" v-model="password" type="password" />
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import UserMessage from "../components/UserMessage.vue";

export default {
    components: {
        UserMessage,
    },
    data() {
        return {
            email: "",
            password: "",
        };
    },
    methods: {
        async handleSubmit() {
            if (this.email === "") {
                this.$refs.messageComponent.showMessage(
                    "Email cannot be empty.",
                    "error"
                );
                return;
            }

            if (this.password === "") {
                this.$refs.messageComponent.showMessage(
                    "Password cannot be empty.",
                    "error"
                );
                return;
            }

            try {
                const response = await this.$axios.post("/back/api/me/", {
                    email: this.email,
                    password: this.password,
                });
                if (response.data.is_authenticated) {
                    this.$refs.messageComponent.showMessage(
                        "Log in successful!",
                        "success"
                    );
                } else {
                    this.$refs.messageComponent.showMessage(
                        "Log in failed. Please try again.",
                        "error"
                    );
                }
            } catch (error) {
                this.$refs.messageComponent.showMessage(
                    "Log in failed. Please try again.",
                    "error"
                );
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: "Roboto", sans-serif;
    letter-spacing: 0.1em;
    font-weight: 600;
    font-size: 1rem;
    color: darkblue;
    text-shadow: grey 0px 0px 1px;
}

form {
    width: 300px;
    padding: 4rem;
    background: linear-gradient(45deg, #9ee1bd, #d1c6ee);
    border-radius: 2rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
}

label {
    margin-bottom: 0.5rem;
}

input[type="text"],
input[type="password"] {
    padding: 0.5rem;
    border-radius: 0.3rem;
    border: 1px solid #ced4da;
    border-radius: 0.5rem;
    outline: none;
    font-size: 1.3rem;

    &:hover {
        border-color: #a7c8ff;
    }

    &:focus {
        border-color: #2b6cb0;
        box-shadow: 0 0 0 0.2rem rgba(43, 108, 176, 0.25);
    }
}

button[type="submit"] {
    margin-top: 1rem;
    padding: 0.8rem;
    border-radius: 0.3rem;
    background-color: #482d8f;
    color: #fff;
    border: none;
    font-size: 1.3rem;
    width: 100%;
    border-radius: 0.5rem;
    font-family: "Roboto", sans-serif;
    letter-spacing: 0.05em;
    font-weight: 400;
    text-transform: uppercase;
    cursor: pointer;

    &:hover {
        background-color: #0f1769;
    }

    &:active {
        background-color: #406698;
    }
}
</style>
