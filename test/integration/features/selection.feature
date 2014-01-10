Feature: Entities selection

    Background:
        Given Firefox as the default browser
        Given a browser

    @wip
    Scenario: pick entities
        Given my program has the entities aa, ab, ba and bb
        When I open the app
        And I search ab
        And I hit Enter
        Then I see ab added to the canvas
