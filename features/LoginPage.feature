Feature: Test LoginPage
  Testing loginpage for the url https://courses.letskodeit.com/login

  Background: User on Login page is common for all scenarios
    Given User on Login page

 @Sanity
  Scenario: Test with valid credentials
    When User enters email "test@gmail.com"
    And User enters password "test@123"
    And User clicks on Login button
    Then User should be logged successfully

  @Smoke
  Scenario: Test with invalid credentials
    When User enters invalid email "qerer@gmail.com"
    And User enters invalid password "123243"
    And User clicks on Login button
    Then User Login should fail

  @Sanity
  Scenario: Test for Forgot password
    When User clicks on Forgot password link
    And User enter valid email "test@gmail.com"
    And User clicks on Reset password button
    Then Password reset link should be sent