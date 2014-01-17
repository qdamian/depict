Feature: Analysis
    Background:
        Given Firefox as the default browser
        Given a browser

    @modules
    Scenario: modules
        Given my program has modules aa_mod, ab_mod, ba_mod, bb_mod
        When I run depict on it
        And I open the app
        And I search ab_mod
        Then I see options ab_mod

    @functions
    Scenario: functions
        Given my program has functions aa_func, ab_func, ba_func, bb_func
        When I run depict on it
        And I open the app
        And I search ab_func
        Then I see options ab_func

    @threads
    Scenario: threads
        Given my program spawns four threads
        When I run depict on it
        And I open the app
        And I search Thread
        Then I see four options listed
