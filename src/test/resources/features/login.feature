Feature: login

  @test
  Scenario Outline: 01. Login with a users file
    Given User enters the "<username>" and "<password>"
    When Click on sign up button
    Then User must successfully login to the Dashboard page

    Examples: Users
      | username  | password |
      | <user1>   | <pass1> |
      | <user2>   | <pass2> |


  @test
  Scenario Outline: 02. Login with a valid credentials
    Given User fills the "<username>" and "<password>"
    When Click on sign up button
    Then User must successfully login to the Dashboard page

  Examples: users
    | username                          | password    |
    | natalia.mateus+mfapp@zemoga.com   | Tester1272* |
    | natalia.mateus+tp@zemoga.com      | Tester1265* |