@fixture.browser.chrome
Feature: Google search
  As a user
  I'd like to search for some phrase to get new information about it

  @sometag
  Scenario: a User can search for a phrase
    Given a User visit Google
    When the user searches for the "mlem" phrase
    Then one of the results contains: "What Does mlem Mean?"


  Scenario: a user can search for a very long phrase
    Given a user visit Google
    When the user searches for the:
          """
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
          """
    Then one of the results contains: "Wikipedia"


  Scenario:  a user search something
    When user do the search of "Dan North"
    Then one of the results contains: "Introducing BDD"
