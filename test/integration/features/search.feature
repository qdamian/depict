Feature: Search
    Background:
        Given Firefox as the default browser

    Scenario: no match
        Given a browser
        And my program has modules aa, ab, ba, bb
        When I open the app
        And I start to fill in search with c
        Then I see no options

    Scenario: single match
        Given a browser
        And my program has modules aa, ab, ba, bb
        When I open the app
        And I start to fill in search with ab
        Then I see options ab

    Scenario: multiple match
        Given a browser
        And my program has modules aa, ab, ba, bb
        When I open the app
        And I start to fill in search with b
        Then I see options ab, ba, bb

    Scenario: functions
        Given a browser
        And my program has functions a_func
        When I open the app
        And I start to fill in search with a_func
        Then I see options a_func
