from db import db

class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), nullable=False)
    expedida_en = db.Column(db.String(100), nullable=False)
    mes = db.Column(db.String(20), nullable=False)