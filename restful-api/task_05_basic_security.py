#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'super-secret-key-1234!'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for basic authentication."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protected by basic authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and return JWT access token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={'role': user['role']}
    )
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected by JWT authentication."""
    return "JWT Auth: Access Granted"


def admin_required(fn):
    """Decorator to restrict access to admin users only."""
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get('role') != 'admin':
            return jsonify({"error": "Admin access required"}), 401
        return fn(*args, **kwargs)
    return wrapper


@app.route('/admin-only')
@admin_required
def admin_only():
    """Route accessible only by admin users."""
    return "Admin Access: Granted"


if __name__ == '__main__':
    """Run the Flask application."""
    app.run(debug=True)
