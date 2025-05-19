Feature: login
  The purpose of this feature is to cover all the possible scenarios related to the login functionality.

  Background:
    Given The page loads
    When Allow the cookies
    Then Click on sign in label

  @Test
    Scenario Outline: 01. Login with a user file
      Given The user data is read from the CSV file
      And The user enters the "<username>" and "<password>"
      When Click on sign in button
      Then User must successfully login to the Dashboard page
      And The user clicks on account name
      And The Vehicles and Service Records title is display

      Examples: Users
        | username                     | password     |
        | natalia.mateus+mf@zemoga.com | Tester1234*  |
        | natalia.mateus+tp@zemoga.com | Tester1234*  |
        | natalia.mateus@zemoga.com    | Tester1234*  |
        # Add more rows as needed


    Scenario Outline: 02. User enters a username and password
    Given User fills the "<username>" and "<password>"
    When Click on sign in button
    Then User must successfully login to the Dashboard page
    And The user clicks on account name
    And The Vehicles and Service Records title is display

    Examples: Users
      | username                     | password     |
      | natalia.mateus+mf@zemoga.com | Tester1234*  |
      | natalia.mateus+tp@zemoga.com | Tester1234*  |
      | natalia.mateus@zemoga.com    | Tester1234*  |
      # Add more rows as needed

