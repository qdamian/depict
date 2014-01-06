Feature: Entities search
    Background:
        Given Firefox as the default browser
        Given a browser

    @search_no_match @extended
    Scenario: no match
        Given my program has the entities aa, ab, ba and bb
        When I open the app
        And I search c
        Then I see no options

    @search_single_match
    Scenario: single match
        Given my program has the entities aa, ab, ba and bb
        When I open the app
        And I search ab
        Then I see options ab

    @search_multiple_match
    Scenario: multiple match
        Given my program has the entities aa, ab, ba and bb
        When I open the app
        And I search b
        Then I see options ab, ba and bb
