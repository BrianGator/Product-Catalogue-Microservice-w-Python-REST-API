# Product Catalogue Microservice

A professional-grade Python microservice for managing an eCommerce Product Catalogue. This service provides a robust REST API and a web-based administrative interface, following TDD (Test-Driven Development) and BDD (Behavior-Driven Development) principles.

## Key Features Implemented
- **Full CRUD Operations**: Create, Read, Update, and Delete products via REST API or Admin UI.
- **Advanced Search**: Filter the product catalogue by Name, Category, or Availability.
- **Data Validation**: Custom error handling and strict schema enforcement for product attributes.
- **Relational Persistence**: Uses SQLAlchemy ORM with a SQLite backend.
- **Automated Testing Suite**: 
    - Comprehensive unit tests (TDD) for models and routes.
    - Behavior-driven scenarios (BDD) using Selenium and Gherkin.
- **Responsive Admin UI**: A built-in dashboard for managing the catalogue without external tools.

## Project Structure & Tasks
- `/service/`: The heart of the microservice. Contains models, routes, and error handling logic.
- `/tests/`: Internal testing logic used for TDD. Includes factories for mock data.
- `/features/`: High-level feature specifications used for BDD.
- `server.py`: The entry point for starting the Flask development server.
- `Requirements.txt`: Project prompt history and Python dependency manifest.
- `Dev-Summary.txt`: Detailed technical breakdown of the codebase architecture.

## How to Use

### 1. Launch the Server
Start the application by running:
```bash
python3 server.py
```
The server will start on `http://localhost:3000`.

### 2. Access the Admin Interface
Open your web browser and navigate to `http://localhost:3000`. You can use the interface to:
- **Create**: Fill in details and click "Create".
- **Search**: Enter a name or select filters and click "Search".
- **Update/Delete**: Use the ID retrieved from a search to modify or remove products.

### 3. Run Automated Tests
- **TDD (Unit Tests)**:
  ```bash
  python3 -m unittest discover tests
  ```
- **BDD (Behavioral Scenarios)**:
  ```bash
  behave
  ```

### 4. API Endpoints
- `GET /products`: List all products or filter via query params.
- `POST /products`: Create a new product (requires JSON body).
- `GET /products/<id>`: Retrieve specific product details.
- `PUT /products/<id>`: Update an existing product.
- `DELETE /products/<id>`: Remove a product from the database.
