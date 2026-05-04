Feature: Product Inventory Management
  As a store administrator
  I want to manage products via the web interface
  So that the online store data is accurate

  Scenario: Successful search for an existing product
    Given I navigate to the home page
    And a product named "Fedora" exists in the system
    When I enter "Fedora" into the name field
    And I press search
    Then I should see the product "Fedora" in the results table

  Scenario: Attempting to retrieve a non-existent ID
    Given I navigate to the home page
    When I enter "9999" into the ID field
    And I press retrieve
    Then I should see an error message "404 Not Found"
