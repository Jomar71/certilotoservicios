from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

def generate_pdf(name, last_name, cedula, expedida_en, mes):
    filename = f"certificado_{name}_{last_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Certilotoservicios")

    # Contenido
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Nombre completo: {name} {last_name}")
    c.drawString(50, height - 120, f"Cédula: {cedula}")
    c.drawString(50, height - 140, f"Expedida en: {expedida_en}")
    c.drawString(50, height - 160, f"Mes: {mes}")

    c.save()
    return filename