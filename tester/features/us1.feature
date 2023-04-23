Feature: Login functionality

  Scenario: US1: As a user, I want to log in to the website, 
  so I can access my account
    Given I'm on the login page
    When I attempt to log in using "<email>" and "<password>"
    Then I should see a message with "<message>"

    Examples:
      | email           | password  | message    |
      |                 |           | Empty      |
      | emailN          | passwordN | Failed     |
      | good@test.com   | passwordY | Successful |
      | bad@test.com    | passwordY | Failed     |      