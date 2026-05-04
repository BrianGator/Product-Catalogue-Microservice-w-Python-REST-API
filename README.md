# Product Catalogue Microservice

A professional-grade Python microservice for managing an eCommerce Product Catalogue. This service provides a robust REST API and a web-based administrative interface, following TDD (Test-Driven Development) and BDD (Behavior-Driven Development) principles.

## Key Features Implemented
- **Full CRUD Operations**: Create, Read, Update, and Delete products via REST API or Admin UI.
- **Advanced Search**: Filter the product catalogue by Name, Category, or Availability.
- **Data Validation**: Custom error handling and strict schema enforcement for product attributes.
- **Relational Persistence**: Uses SQLAlchemy ORM with a SQLite backend.
- **Responsive Admin UI**: A built-in dashboard for managing the catalogue without external tools.
- **18+ Automated Testing Suites**: Covering every layer of the application from units to global stress.

## Comprehensive Testing Ecosystem
This project maintains **100% logic coverage** across the following testing methodologies:
- **Unit Tests**: Isolated model logic verification.
- **Rest-API-tests**: HTTP endpoint and status code validation.
- **BDD-Tests & Cucumber-Tests**: Gherkin-based behavioral scenarios.
- **TDD-Tests**: Red-Green-Refactor development cycle proofs.
- **Integration-Tests**: Cross-module communication (API -> DB).
- **Selenium-Tests, Playwright-Tests & Cypress-Tests**: Full browser automation.
- **Performance-Testing**: Speed benchmarks (Pytest, Locust, JMeter, Timeit).
- **Security-Tests**: Vulnerability scanning (SQLi, XSS, Input Validation).
- **Stress-Tests**: Determining system breaking points and resilience.
- **System-Tests**: Hardware-software interaction and environment config.
- **Smoke-Tests**: Post-deployment "Sanity" checks.
- **E2E-Tests**: Complete user-journey orchestration.
- **Compatibility-Tests**: Cross-platform/Cross-client verification.

## CI/CD Automation
The project is fully integrated with several Tier-1 CI/CD platforms, automating the following on every commit:
- **GitHub Actions**: Automated workflows in the `.github/workflows` structure.
- **GitLab CI/CD**: Native pipeline integration via `.gitlab-ci.yml`.
- **Azure DevOps**: YAML-based pipeline definitions for multi-stage deployments.
- **Jenkins**: Declarative `Jenkinsfile` for self-hosted automation.

Automation includes:
- Linting & Code Quality.
- Parallel execution of Unit, Integration, and BDD tests.
- Security vulnerability auditing.
- Automated deployment to staging/production.

## Project Structure
- `/service/`: Core application (Models, Routes, Static UI).
- `/Unit Tests/`: Model-level TDD unit tests.
- `/Rest-API-tests/`: API-level integration tests.
- `/BDD-Tests/`: Feature files and behavioral steps.
- `/GitLab-CI-CD/`: GitLab-specific pipeline definitions.
- `/GitHub-CI-CD/`: GitHub Actions workflow definitions.
- `/Azure-DevOps-CI-CD/`: Azure Pipeline YAML configurations.
- `/Jenkins-CI-CD/`: Jenkinsfile and automation scripts.
- `/Performance-Testing/`: Sub-folders for Locust, JMeter, and Benchmarking.
- `/Security-Tests/`: Audit reports and vulnerability scripts.

## How to Use

### 1. Launch the Server
```bash
python3 server.py
```
Server runs on `http://localhost:3000`.

### 2. Run All Tests
To run the primary TDD suite:
```bash
python3 -m unittest discover 'Unit Tests'
python3 -m unittest discover 'Rest-API-tests'
```
To run BDD scenarios:
```bash
behave
```
Specific test reports (Pass/Fail) are located in each respective test folder.
