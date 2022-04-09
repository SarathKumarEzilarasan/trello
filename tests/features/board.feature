
Feature: Create a Board, Add Card and comment on the card

  Background:

  Scenario: Create a Board
    Given Create a Board
    When Create a card
    Then Delete a card
    When Create a card
    When Create a card
    Then Edit card
    Then Add a comment to the card API
@tag
  Scenario: Verify Board
    Given User logs in
    When Verify card with comment
    Then Add a comment in UI
    Then Set card as done

#Feature: Login to the ATI Application
#This features contains login to the ATI Application
#
# Scenario:User is on ATI Login HomePage
#  Given user open the browser and nivigate to the ATI Login Homepage
#  When user enter Director as a user name
#  And  user enter Password as a password
#  Then  user should able to the ATI Homepage