Feature: login
  The purpose of this feature is to cover all the possible scenarios related to the login functionality.

  Background:
    Given I allow the cookies

  @test
  Scenario Outline: 01. Login with a users file
    Given The user data is read from the CSV file
    And User enters the "<username>" and "<password>"
    When Click on sign in button
    Then User must successfully login to the Dashboard page
    And The user clicks on account name
    And The Vehicles and Service Records title is display

    Examples: Users
      | username                     | password     |
      | natalia.mateus+mf@zemoga.com | Tester5678$  |
      | natalia.mateus+tp@zemoga.com | Tester5678$  |
      | natalia.mateus@zemoga.com    | Tester5678$  |
      # Add more rows as needed

  @test
    Scenario Outline: 02. User enters a username and password from the users list
    Given User enters a "<username>" and "<password>" from the users list
    When Click on sign in button
    Then User must successfully login to the Dashboard page
    And The user clicks on account name
    And The Vehicles and Service Records title is display

    Examples: Users
      | username                     | password     |
      | natalia.mateus+mf@zemoga.com | Tester5678$  |
      | natalia.mateus+tp@zemoga.com | Tester5678$ |
      | natalia.mateus@zemoga.com    | Tester5678$  |
      # Add more rows as needed

