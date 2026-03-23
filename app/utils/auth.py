from flask import current_app
import jwt
from functools import wraps
from flask import request, jsonify

# Generate token
def generate_token(user_id):
    SECRET_KEY = current_app.config["SECRET_KEY"]

    token = jwt.encode(
        {"user_id": user_id},
        SECRET_KEY,
        algorithm="HS256"
    )
    return token


# Verify token
def verify_token(token):
    SECRET_KEY = current_app.config["SECRET_KEY"]

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded["user_id"]
    except:
        return None


# Auth decorator
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token missing"}), 401

        user_id = verify_token(token)

        if not user_id:
            return jsonify({"message": "Invalid token"}), 401

        return f(user_id, *args, **kwargs)

    return decorated