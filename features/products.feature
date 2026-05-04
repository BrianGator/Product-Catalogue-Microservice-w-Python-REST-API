Feature: The product store service back-end

    As a Product Store Manager
    I need a RESTful catalog service
    So that I can keep track of all my products

    Background:
        Given the following products
            | name        | description | price | available | category    |
            | Fedora      | A fine hat  | 12.50 | True      | CLOTHS      |
            | Steak       | Delicious   | 20.00 | True      | FOOD        |
            | Waffle Maker| Kitchen app | 35.00 | False     | HOUSEWARES  |
            | Drill       | Power tool  | 50.00 | True      | TOOLS       |

    Scenario: Create a Product
        When I visit the "Home Page"
        And I set the "Name" to "Hammer"
        And I set the "Description" to "For nails"
        And I set the "Price" to "15.00"
        And I select "True" in the "Available" dropdown
        And I select "Tools" in the "Category" dropdown
        And I press the "Create" button
        Then I should see the message "Success"
        When I copy the "Id" field
        And I press the "Clear" button
        And I paste the "Id" field
        And I press the "Retrieve" button
        Then I should see "Hammer" in the "Name" field
        And I should see "For nails" in the "Description" field
        And I should see "15.00" in the "Price" field

    Scenario: Read a Product
        When I visit the "Home Page"
        And I set the "Name" to "Fedora"
        And I press the "Search" button
        Then I should see the message "Success"
        When I copy the "Id" field
        And I press the "Clear" button
        And I paste the "Id" field
        And I press the "Retrieve" button
        Then I should see "Fedora" in the "Name" field
        And I should see "A fine hat" in the "Description" field

    Scenario: Update a Product
        When I visit the "Home Page"
        And I set the "Name" to "Fedora"
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Fedora" in the "Name" field
        When I set the "Name" to "Hat"
        And I press the "Update" button
        Then I should see the message "Success"
        When I press the "Clear" button
        And I set the "Name" to "Hat"
        And I press the "Search" button
        Then I should see "Hat" in the "Name" field
        And I should not see "Fedora" in the results

    Scenario: Delete a Product
        When I visit the "Home Page"
        And I set the "Name" to "Fedora"
        And I press the "Search" button
        Then I should see the message "Success"
        When I copy the "Id" field
        And I press the "Delete" button
        Then I should see the message "Product has been Deleted!"
        When I press the "Clear" button
        And I paste the "Id" field
        And I press the "Retrieve" button
        Then I should see the message "404 Not Found"

    Scenario: List All Products
        When I visit the "Home Page"
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Fedora" in the results
        And I should see "Steak" in the results
        And I should see "Waffle Maker" in the results
        And I should see "Drill" in the results

    Scenario: Search by Category
        When I visit the "Home Page"
        And I select "Cloths" in the "Category" dropdown
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Fedora" in the results
        And I should not see "Steak" in the results

    Scenario: Search by Availability
        When I visit the "Home Page"
        And I select "False" in the "Available" dropdown
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Waffle Maker" in the results
        And I should not see "Fedora" in the results

    Scenario: Search by Name
        When I visit the "Home Page"
        And I set the "Name" to "Fedora"
        And I press the "Search" button
        Then I should see the message "Success"
        And I should see "Fedora" in the results
        And I should not see "Steak" in the results
