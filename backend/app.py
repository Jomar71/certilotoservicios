from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from routes.admin import admin_bp
from routes.certificate import certificate_bp
from db import db
from config import Config

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(certificate_bp, url_prefix='/certificate')

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a Certilotoservicios API"}), 200

if __name__ == '__main__':
    app.run(debug=True)