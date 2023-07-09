from flask_sqlalchemy import SQLAlchemy
from models import db

class Objective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    key_results = db.relationship('KeyResult', backref='objective', lazy=True)

    def __repr__(self):
        return f'<Objective {self.name}>'
