from pdf_generator import generate_pdf
from models import Certificate
from app import app, db

with app.app_context():
    certificates = Certificate.query.all()
    for cert in certificates:
        generate_pdf(cert.name, cert.last_name, cert.cedula, cert.expedida_en, cert.mes)
    print("Todos los PDFs generados.")