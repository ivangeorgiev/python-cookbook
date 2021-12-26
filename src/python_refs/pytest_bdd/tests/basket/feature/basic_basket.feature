Feature: Basic basket
    Scenario: Create empty basket
        When I create empty basket
        Then basket should be empty

    Scenario: Add to empty basket
        Given empty basket
        When I put 3 cucumbers
        Then basket should have 3 cucumbers
