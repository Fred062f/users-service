from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3
import os
from dotenv import load_dotenv
from flasgger import Swagger
from db import init_db

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app)

DATABASE = os.getenv('DATABASE')
SECRET_KEY = os.getenv('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    
    This endpoint allows a user to create an account by providing a username and password.
    ---
    tags:
      - User Management
    parameters:
      - in: body
        name: user
        required: true
        description: User credentials for registration.
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: A unique username for the new user.
            password:
              type: string
              description: A secure password for the new user.
    responses:
      201:
        description: User registered successfully.
      400:
        description: Username is already taken or request is invalid.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'User already exists'}), 400


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and provide a JWT token.
    
    This endpoint validates the username and password of a user. If successful, a JWT token is returned
    for accessing protected endpoints.
    ---
    tags:
      - User Management
    parameters:
      - in: body
        name: user
        required: true
        description: User credentials for login.
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: The registered username of the user.
            password:
              type: string
              description: The password corresponding to the username.
    responses:
      200:
        description: Login successful, JWT token provided.
        schema:
          type: object
          properties:
            token:
              type: string
              description: A JWT token for authentication.
      401:
        description: Invalid username or password.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        access_token = create_access_token(identity=username, fresh=True)
        return jsonify({'token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_account():
    """
    Delete the logged-in user's account.
    
    This endpoint deletes the user's account from the database. Requires a valid JWT token in the Authorization header.
    ---
    tags:
      - User Management
    parameters:
      - in: header
        name: Authorization
        required: true
        type: string
        description: Bearer token for user authentication.
    responses:
      200:
        description: User account deleted successfully.
      401:
        description: Token is invalid or expired.
      400:
        description: Error occurred while deleting the account.
    """
    current_user = get_jwt_identity()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (current_user,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User account deleted successfully'}), 200


@app.route('/restricted', methods=['GET'])
@jwt_required() 
def restricted():
    """A test route to check if the user is authenticated."""
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}! You have access to this restricted route.'}), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
