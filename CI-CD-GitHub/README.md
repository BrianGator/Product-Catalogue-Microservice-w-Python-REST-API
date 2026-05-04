# GitHub Actions CI/CD Integration

This directory contains the configurations required to automate the testing and deployment of the Product Catalogue Microservice using GitHub Actions.

## Contents
- `github-actions.yml`: The primary workflow definition file.

## Pipeline Steps
1. **Checkout**: Pulls the latest code from the repository.
2. **Setup Python**: Configures the Python 3.8 environment.
3. **Install Dependencies**: Installs requirements from `Requirements.txt`.
4. **Unit Tests**: Runs TDD tests in the `Unit Tests` folder.
5. **API Tests**: Runs integration tests in the `Rest-API-tests` folder.
6. **BDD Scenarios**: Executes Gherkin scenarios using Behave and a headless Chrome service.
