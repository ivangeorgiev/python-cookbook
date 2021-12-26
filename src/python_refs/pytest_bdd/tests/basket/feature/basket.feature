Feature: Basket
    Scenario: Create empty basket
        When I create empty basket
        Then I should have 0 cucumbers

    Scenario: Get cucumbers
        Given there are <start> cucumbers in the basket
        When I put <num> cucumbers
        Then I should have <left> cucumbers

        Examples:
            | start | num | left |
            | 0     | 5   | 5    |
            | 3     | 7   | 10   |

    Scenario: Get cucumbers multiple times
        Given there are 5 cucumbers in the basket
        When I get 1 cucumber from the basket
        And I get 3 cucumbers from the basket
        Then I should have 1 cucumbers in the basket
