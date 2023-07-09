from flask import Flask
from models import db
from routes import objective_routes #, key_result_routes, member_routes, organization_routes
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./okr.db'

migrate = Migrate(app, db)
db.init_app(app)

app.register_blueprint(objective_routes)
# Register additional routes as needed
# app.register_blueprint(key_result_routes)
# app.register_blueprint(member_routes)
# app.register_blueprint(organization_routes)
