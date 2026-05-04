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
This project maintains **100% logic coverage** and over **60+ automated test cases** across the following testing methodologies:
- **Unit Tests**: 13+ assertions covering model validations and error edge cases.
- **Rest-API-tests**: 14+ scenarios validating HTTP status codes and payloads.
- **Integration-Tests**: 6+ full-lifecycle scenarios from API to DB persistence.
- **Smoke-Tests**: 8+ instant "Sanity" checks for deployment health.
- **Stress-Tests**: 7+ scenarios determining system breaking points.
- **Compatibility-Tests**: 7+ cross-platform and cross-client proofs.
- **System-Tests**: 8+ hardware-software interaction proofs.
- **BDD-Tests & Cucumber-Tests**: Gherkin-based behavioral scenarios.

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
- `/CI-CD-GitLab/`: GitLab-specific pipeline definitions.
- `/CI-CD-GitHub/`: GitHub Actions workflow definitions.
- `/CI-CD-Azure-DevOps/`: Azure Pipeline YAML configurations.
- `/CI-CD-Jenkins/`: Jenkinsfile and automation scripts.
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
