Feature: Onboarding feature

   Scenario: 01. Create a new account with profile information in vehicle's info slide
     Given I navigate to the create an account button in the menu
     When I submit email password and profile information
     And The get started button is displayed in vehicle's info slide
     And I allow notifications
     And The app should display My Garage screen
     Then I should be logged in

