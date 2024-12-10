# User Service API

This project is a simple Flask-based API that manages user authentication and provides JWT token-based security for certain routes. It includes the following endpoints:

- **Register a new user** (`/register`): Create a new user account.
- **Login** (`/login`): Authenticate a user and generate a JWT token.
- **Delete account** (`/delete`): Delete the authenticated user's account.
- **Restricted access** (`/restricted`): A test route to check if the user is authenticated.
- **List available endpoints** (`/endpoints`): Get a list of all available API routes with their descriptions and JWT token requirements.

## Features

- **User registration** and **login** with JWT-based authentication.
- Ability to **delete user accounts** with authentication.
- A **restricted endpoint** that requires a valid JWT token.
- **Swagger UI** for easy API documentation and interaction.

## Installation

To get started with the API, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Fred062f/users-service.git
cd users-service
pip install -r requirements.txt
```

## Configuration

Before running the application, set up the required environment variables. Create a `.env` file with the following content:

```bash
DATABASE=your_database_path.db
SECRET_KEY=your_jwt_secret_key
```

- `DATABASE`: Path to your SQLite database file.
- `SECRET_KEY`: A secret key used for JWT token encryption.

## Running the Application

To start the Flask server, run the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### `POST /register`
Register a new user. Provide a JSON payload with the following properties:
- `username` (string): The unique username.
- `password` (string): The password for the new user.

**Response:**
- `201`: User registered successfully.
- `400`: Username already exists or request is invalid.

### `POST /login`
Authenticate a user and provide a JWT token. Provide a JSON payload with the following properties:
- `username` (string): The registered username.
- `password` (string): The password for the username.

**Response:**
- `200`: Login successful, JWT token provided.
- `401`: Invalid username or password.

### `DELETE /delete`
Delete the logged-in user's account. This endpoint requires a valid JWT token in the `Authorization` header.

**Response:**
- `200`: User account deleted successfully.
- `401`: Token is invalid or expired.
- `400`: Error occurred while deleting the account.

### `GET /restricted`
A test route to check if the user is authenticated. Requires a valid JWT token.

**Response:**
- `200`: Hello message for the authenticated user.

### `GET /endpoints`
List all available API endpoints, including descriptions, methods, and whether a JWT token is required.

**Response:**
- `200`: A list of all available routes.

## Swagger UI

To interact with the API via Swagger UI, navigate to the `/apidocs/` route in your browser (e.g., `http://127.0.0.1:5000/apidocs/`).

## Requirements

- Python 3.7+
- Flask
- Flask-JWT-Extended
- Flask-Swagger
- SQLite3
- python-dotenv

Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```
