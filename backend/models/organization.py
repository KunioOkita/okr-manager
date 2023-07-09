from flask_sqlalchemy import SQLAlchemy
from models import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=True)
    children = db.relationship('Organization', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')
    members = db.relationship('Member', backref='organization', lazy=True)

    def __repr__(self):
        return f'<Organization {self.name}>'
