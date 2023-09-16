from flask import blueprints, request, jsonify
from flask_jwt_extended import jwt_required
from config import db 
from models import User
from schemas import UserSchema, RoleSchema
from auth.utils import admin_required
from users import users_bp

@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    #validar y desearilizar los datos usando el esquema UserSchema con la opcion load_instance= true  para crear un objeto user
    user = User(data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "se creo correctamente el usuario"}), 201

@users_bp.route("/users", methods= ["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result), 200
    #user = User.get_user_roles(1)
    #print(user)
    #u = jsonify(user)
    #print(u)
    #return ('hola')

    