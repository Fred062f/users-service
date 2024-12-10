## Flask JWT Authentication API

This is a Flask application that implements user registration, login, and account deletion with JWT-based authentication. It also provides an endpoint to list all available API routes with their descriptions and access requirements.

**Features:**

* User registration
* User login with JWT token generation
* Account deletion (requires JWT)
* Restricted route accessible only with a valid JWT token
* API endpoint documentation with Swagger
* Endpoint listing with descriptions and JWT requirements

**Environment Variables:**

* `DATABASE`: Path to the SQLite database file.
* `SECRET_KEY`: Secret key used for JWT signing. 

**Running the Application:**

1. Create a `.env` file in your project directory containing:

```
DATABASE=path/to/your/database.db
SECRET_KEY=your_secret_key
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application in debug mode:

```
python app.py
```

**API Endpoints:**

| Endpoint | Method | Description | JWT Required |
|---|---|---|---|
| /register | POST | Register a new user | No |
| /login | POST | Login and get JWT token | No |
| /delete | DELETE | Delete the logged-in user's account | Yes |
| /restricted | GET | Test route accessible only with JWT | Yes |
| /endpoints | GET | List all available API endpoints | No |

**Using Swagger Documentation:**

Swagger documentation is available at `http://localhost:5000/apidocs`. You can explore API endpoints, their parameters, responses, and authorization requirements.
