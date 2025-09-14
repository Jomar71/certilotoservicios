from flask import Blueprint, request, jsonify, send_file
from pdf_generator import generate_pdf
from models import Certificate

certificate_bp = Blueprint('certificate', __name__)

@certificate_bp.route('/generate', methods=['POST'])
def generate_certificate():
    data = request.json
    name = data.get('name')
    last_name = data.get('last_name')
    cedula = data.get('cedula')
    expedida_en = data.get('expedida_en')
    mes = data.get('mes')

    if not all([name, last_name, cedula, expedida_en, mes]):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # Generar PDF
    pdf_path = generate_pdf(name, last_name, cedula, expedida_en, mes)

    # Guardar en la base de datos
    new_certificate = Certificate(
        name=name,
        last_name=last_name,
        cedula=cedula,
        expedida_en=expedida_en,
        mes=mes
    )
    db.session.add(new_certificate)
    db.session.commit()

    return send_file(pdf_path, as_attachment=True)

@certificate_bp.route('/list', methods=['GET'])
def list_certificates():
    certificates = Certificate.query.all()
    result = [{"id": cert.id, "name": cert.name, "last_name": cert.last_name} for cert in certificates]
    return jsonify(result), 200