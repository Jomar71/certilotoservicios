from flask import Blueprint, request, jsonify
from db import db
from models import AdminUser

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/create_admin', methods=['POST'])
def create_admin():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    new_admin = AdminUser(username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Administrador creado exitosamente"}), 201

@admin_bp.route('/update_template', methods=['PUT'])
def update_template():
    data = request.json
    template_fields = data.get('template_fields')

    # Lógica para actualizar la plantilla según las necesidades del administrador
    return jsonify({"message": "Plantilla actualizada", "fields": template_fields}), 200