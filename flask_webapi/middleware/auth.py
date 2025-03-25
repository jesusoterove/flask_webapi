from functools import wraps
from flask import request, jsonify
from werkzeug.local import LocalProxy
import jwt
from datetime import datetime, timedelta
from exceptions.api_exception import ApiException
from flask import current_app

SECRET_KEY = current_app.config['JWT_SECRET_KEY']

def get_auth_token_data(request: LocalProxy):
    token = None
    # Check if token exists in headers
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        try:
            token = auth_header.split(" ")[1]  # Bearer <token>
        except IndexError:
            raise ApiException('Invalid token format', 401)

    if not token:
        raise ApiException('message': 'Token is missing', 401)

    try:
        # Decode token
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise ApiException('Token has expired', 401)
    except jwt.InvalidTokenError:
        raise ApiException('Invalid token', 401)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            data = get_auth_token_data(request)
            current_user = data['sub']
            return f(current_user, *args, **kwargs)
        except ApiException as e:
            return jsonify({'message': e.message}), e.status_code
    
    return decorator

def role_required(f, role: str):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            data = get_auth_token_data(request)

            if data['role'] != role:
                return jsonify({'message': 'Unauthorized'}), 403
            
            return f(*args, **kwargs)
        except ApiException as e:
            return jsonify({'message': e.message}), e.status_code
    
    return decorator