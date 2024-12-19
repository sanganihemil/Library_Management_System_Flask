# Library API

This project is a simple RESTful API built with Flask that allows users to manage books and members in a library. It supports basic CRUD operations for both books and members.

## Project Structure

The project consists of three main files:
1. `app.py`: The main Flask application containing all the routes and logic for interacting with books and members.
2. `models.py`: Contains the database models (Books and Member) and SQLAlchemy setup.
3. `test.py`: Unit tests to ensure the functionality of the API endpoints.

## How to Run the Project

### Prerequisites:
- **Python 3.x** is required.
- **Flask** and **SQLAlchemy** libraries are required.

### Steps to Run:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanganihemil/Library_Management_System_Flask.git
   cd Library_Management_System_Flask
   ```

2. **Install Dependencies**:
   ```bash
   pip install Flask SQLAlchemy
   ```

3. **Setup the Database**:
   * The application uses SQLite. The database is created automatically when the app starts.
  
4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the API**: 
   * The app will run on `http://127.0.0.1:5000/`
   * To view all books, visit: `http://127.0.0.1:5000/books`
   * Note: The root URL (`/`) doesn't have a webpage interface. You must use the specific endpoints like `/books` to interact with the API.
   * You can use tools like Postman or cURL to interact with the API endpoints.

   Available endpoints:
   * GET `/books` - View all books
   * GET `/books/<id>` - View a specific book
   * POST `/books` - Add a new book
   * PUT `/books/<id>` - Update a book
   * DELETE `/books/<id>` - Delete a book

## Design Choices

1. **Flask**:
   * Flask was chosen for its simplicity and flexibility. It is a lightweight framework ideal for building RESTful APIs.

2. **SQLite with SQLAlchemy ORM**:
   * SQLite is used as the database, which is ideal for development and small-scale applications.
   * SQLAlchemy provides an ORM for interacting with the SQLite database using Python objects.

3. **Date Handling**:
   * The `published` field for books is managed using Python's `datetime` module, and the date format is expected to be `YYYY-MM-DD`.

4. **API Design**:
   * RESTful endpoints (`GET`, `POST`, `PUT`, `DELETE`) are used for managing books and members.
   * Each resource (book/member) has its own set of endpoints for CRUD operations.

## Assumptions & Limitations

### Assumptions:
1. **Unique Book Titles**: Books must have unique titles. Adding a book with the same title as an existing one will return an error.
2. **Unique Member Emails**: Each member must have a unique email address.

### Limitations:
1. **No Authentication**: The API does not implement any form of authentication (e.g., JWT or OAuth).
2. **Basic Error Handling**: Error handling is minimal, and additional checks for invalid input or edge cases could be added.
3. **SQLite**: While SQLite is used for simplicity, it is not recommended for production with large-scale data or high traffic. A more robust database like PostgreSQL is recommended for production.

## Unit Tests

The `test.py` file contains unit tests for all the API endpoints. These tests ensure that the application behaves as expected for basic CRUD operations.

To run the tests:

1. Install `unittest`:
   ```bash
   pip install unittest
   ```

2. Run the tests:
   ```bash
   python -m unittest test.py
   ```
