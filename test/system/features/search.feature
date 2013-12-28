Feature: Search
    Background:
        Given Chrome as the default browser

    Scenario: single match
        Given a browser
        And my program has modules aa, ab, ba, bb
        When I run depict on it
        And I open the app
        And I start to fill in "search" with "ab"
        Then I see options ab
