# Azure DevOps CI/CD Integration

This directory contains the configurations required to automate the testing and deployment of the Product Catalogue Microservice using Azure Pipelines.

## Contents
- `azure-pipelines.yml`: The YAML-based pipeline definition.

## Pipeline Stages
1. **Build**: Installs dependencies and prepares the Python environment.
2. **Test**: Executes Unit and API integration tests.
3. **BDD**: Runs behavioral scenarios using Behave and Selenium.
