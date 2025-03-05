from cadastro import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    datanascimento = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)
    responde = db.Column(db.Integer,default=0)