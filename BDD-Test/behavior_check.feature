# BDD Scenarios for Product Store
# This folder mirrors the functionality defined in the primary Gherkin features

Feature: Product Management Behavior

    As a Store Manager
    I want to interact with the Product Catalog
    So that I can verify the end-to-end user experience

    Scenario: Product Visibility
        Given the inventory is populated
        When I search for "Fedora"
        Then I should see "Fedora" in the search results
