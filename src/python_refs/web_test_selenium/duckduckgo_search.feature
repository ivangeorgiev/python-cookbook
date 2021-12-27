Feature: DuckDuckGo Search
    Scenario: Basic DuckDuckGo Search
        Given the DuckDuckGo Homepage is displayed
        When the user searches for "<query>"
        Then the search result title contains "<query>"
        And the search result query is "<query>"
        And the search result links pertain to "<query>"

        Examples:
            | query      |
            | panda      |
            | big baobab |
