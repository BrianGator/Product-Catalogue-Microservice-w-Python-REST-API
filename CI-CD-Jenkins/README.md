# Jenkins CI/CD Integration

This directory contains the configurations required to automate the testing and deployment of the Product Catalogue Microservice using Jenkins.

## Contents
- `Jenkinsfile`: The declarative pipeline definition.

## Pipeline Stages
1. **Checkout**: Retrieves source code from the SCM.
2. **Install Dependencies**: Sets up the Python environment and libraries.
3. **Static Analysis**: Runs `flake8` for code quality checks.
4. **Unit & API Tests**: Executes the main test suites.
5. **BDD Scenarios**: Runs behavioral tests.
6. **Deploy**: Simulated deployment stage for staging/production.
