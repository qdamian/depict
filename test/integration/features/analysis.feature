Feature: Program analysis
    Background:
        Given Firefox as the default browser
        And a browser

    Scenario: functions
        Given my program has functions a_func
        When I open the app
        And I search a_func
        Then I see options a_func
