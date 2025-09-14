from pydantic import BaseModel

class CertificateSchema(BaseModel):
    name: str
    last_name: str
    cedula: str
    expedida_en: str
    mes: str

    class Config:
        orm_mode = True