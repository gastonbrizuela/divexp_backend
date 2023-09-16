from flask import blueprints, jsonify
from groups import groups_bp
from models import Groups
from schemas import groupsSchema

@groups_bp.route("/groups", methods=['POST'])
def create_groups():
    return

@groups_bp.route("/groups", methods=['GET'])
def get_groups():
    groups = Groups.query.all()
    groups_schema = groupsSchema(many=True)
    result = groups_schema.dump(groups)
    return jsonify(result), 200