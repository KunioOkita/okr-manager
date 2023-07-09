from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the intermediate table for the many-to-many relationship
key_result_member = db.Table('key_result_member',
    db.Column('key_result_id', db.Integer, db.ForeignKey('key_result.id'), primary_key=True),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'), primary_key=True)
)

from .objective import Objective
from .key_result import KeyResult
from .member import Member
from .organization import Organization
