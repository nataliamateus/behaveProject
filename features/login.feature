Feature: login

  Scenario Outline: 01. Login with a users file
    Given The user data is read from the CSV file
    And User enters the "<username>" and "<password>"
    When Click on sign up button
    Then User must successfully login to the Dashboard page

    Examples: Users
      | username                     | password     |
      | natalia.mateus+mf@zemoga.com | Tester5678$  |
      | natalia.mateus+tp@zemoga.com | Tester1234*  |
      | natalia.mateus@zemoga.com    | Tester5678$  |
      # Add more rows as needed


  @test
    Scenario Outline: 02. User enters a username and password from the users list
    Given User enters a "<username>" and "<password>" from the users list
    When Click on sign up button
    Then User must successfully login to the Dashboard page

    Examples: Users
      | username                     | password     |
      | natalia.mateus+mf@zemoga.com | Tester5678$  |
      | natalia.mateus+tp@zemoga.com | Tester1234*  |
      | natalia.mateus@zemoga.com    | Tester5678$  |
      # Add more rows as needed

