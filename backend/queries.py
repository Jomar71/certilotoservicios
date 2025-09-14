from models import Certificate

def get_certificate_by_id(certificate_id):
    return Certificate.query.get(certificate_id)

def delete_certificate(certificate_id):
    certificate = Certificate.query.get(certificate_id)
    if certificate:
        db.session.delete(certificate)
        db.session.commit()
        return True
    return False