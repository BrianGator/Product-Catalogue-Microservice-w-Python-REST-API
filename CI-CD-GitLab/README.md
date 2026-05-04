# GitLab CI/CD Integration

This directory contains the configurations required to automate the testing and deployment of the Product Catalogue Microservice using GitLab's CI/CD pipelines.

## Contents
- `.gitlab-ci.yml`: The primary pipeline definition file.
- `setup_gitlab.sh`: Helper script for setting up runner environments.

## Pipeline Stages
1. **Lint**: Checks for PEP8 compliance.
2. **Unit-Test**: Runs TDD tests in the `Unit Tests` folder.
3. **Integration**: Runs the API integration suite.
4. **Security**: Runs security scans and vulnerability tests.
5. **BDD**: Executes Selenium scenarios in a headless environment.
6. **Deploy**: Simulated deployment to production environment.
