from app import app, db
from models import AdminUser

with app.app_context():
    admin = AdminUser(username="admin", password="admin_password")
    db.session.add(admin)
    db.session.commit()
    print("Administrador creado exitosamente.")