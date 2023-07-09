from flask_sqlalchemy import SQLAlchemy
from models import key_result_member
from models import db

class KeyResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    objective_id = db.Column(db.Integer, db.ForeignKey('objective.id'), nullable=False)
    members = db.relationship('Member', secondary=key_result_member, backref=db.backref('key_results', lazy=True))

    def __repr__(self):
        return f'<KeyResult {self.name}>'
