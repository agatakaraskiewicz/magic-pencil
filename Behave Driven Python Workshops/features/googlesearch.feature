Feature: Google search
  As a user
  I'd like to search for some phrase to get new information about it

  Scenario: a User can search for a phrase
    Given a User visit Google
    When the User searches for a phrase
    Then one of the results contains expected result
