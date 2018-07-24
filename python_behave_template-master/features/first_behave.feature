@MCQ_Varient
Feature: MCQ Variant
  Description: Here i am testing levels of mcq with valid inputs

  Background: 
    Given Application should launch
    And Tap on Launch MCQ button
    Then It should load MCQ Scene

  Scenario: Check if first level is complete
    When Tap on the correct answer
    Then Pop up message should be display as Awesome and next Level question2 should load
    When Tap on the correct answer2
    Then Pop up message should be display as Superb and next Level question3 should load
    When Tap on the correct answer3
    Then Pop up message should be display as Clever