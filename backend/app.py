from flask import Flask
from flask_cors import CORS
from routes.admin import admin_bp
from routes.certificate import certificate_bp
from db import db, init_db

app = Flask(__name__)
CORS(app)

# Inicializar la base de datos
init_db(app)

# Registrar blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(certificate_bp, url_prefix='/certificate')

@app.route('/')
def home():
    return {"message": "Bienvenido a Certilotoservicios API"}, 200

if __name__ == '__main__':
    app.run(debug=True)