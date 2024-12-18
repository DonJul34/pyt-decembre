# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    nombre_employes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Client {self.nom}>'
