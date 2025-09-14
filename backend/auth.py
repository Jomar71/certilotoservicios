from functools import wraps
from flask import request, jsonify
from models import AdminUser

def authenticate_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not AdminUser.query.filter_by(username=auth.username).first():
            return jsonify({"error": "Acceso no autorizado"}), 401
        return f(*args, **kwargs)
    return decorated_function