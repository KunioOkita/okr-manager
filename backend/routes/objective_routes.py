from flask import Blueprint, request, jsonify
from models import db, Objective

objective_routes = Blueprint('objective_routes', __name__)

# Create
@objective_routes.route('/objectives', methods=['POST'])
def create_objective():
    data = request.get_json()
    new_objective = Objective(name=data['name'], organization_id=data['organization_id'])
    db.session.add(new_objective)
    db.session.commit()
    return jsonify({'message': 'Objective created'}), 201

# Read
@objective_routes.route('/objectives/<objective_id>', methods=['GET'])
def read_objective(objective_id):
    objective = Objective.query.get_or_404(objective_id)
    return jsonify({'name': objective.name, 'organization_id': objective.organization_id}), 200

# Update
@objective_routes.route('/objectives/<objective_id>', methods=['PUT'])
def update_objective(objective_id):
    data = request.get_json()
    objective = Objective.query.get_or_404(objective_id)
    objective.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Objective updated'}), 200

# Delete
@objective_routes.route('/objectives/<objective_id>', methods=['DELETE'])
def delete_objective(objective_id):
    objective = Objective.query.get_or_404(objective_id)
    db.session.delete(objective)
    db.session.commit()
    return jsonify({'message': 'Objective deleted'}), 200
