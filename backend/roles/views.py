from flask import blueprints, jsonify
from roles import roles_bp
from models import Role
from schemas import RoleSchema

@roles_bp.route("/roles", methods=['POST'])
def create_role():
    return

@roles_bp.route("/roles", methods=['GET'])
def get_roles():
    roles = Role.query.all()
    role_schema = RoleSchema(many=True)
    result = role_schema.dump(roles)
    return jsonify(result), 200