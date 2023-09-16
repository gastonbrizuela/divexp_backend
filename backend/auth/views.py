#auth/views.py 
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required,get_jwt_identity, get_jwt
from config import db
from models import User
from schemas import UserSchema
from auth.utils import revoke_token
from auth import auth_bp
from datetime import datetime, timedelta


# crear el blueprint de auth

@auth_bp.route("/login", methods = ["get"])
def login():
    # obtener los datos de la peticion en formato json
    data = request.get_json()
    # validar los datos usando el esquema Username
    user_schema = UserSchema()
    #error = user_schema.validate(data)
    
    #if error:
     #   return jsonify(error),400
    #si no hay error obtener el username y la password de los datos validadoes
    username = data["username"]
    password = data["password"]
    # buscar al usuario por username en la base de datos
    user = User.query.filter_by(username=username).first()
    #si no encuentra al usuario o la contraseña no coincide, vevolver una respuesta con el error correspondiente
    print(user.username)
    print(user.password)
    if not user or not user.check_password(password):
        return jsonify({"message":"invalid username or password"}), 401
    
    #sei encuentra al usuario y la contraseña es correcta, generar los tokens de acceso y de refresco usando su id de identidad
    access_token = create_access_token(identity=user.id)
    #refresh_token = create_refresh_token(identity=user.id,expires_delta=timedelta(hours=72))
    # generar una respuesta con los tokens y los codigos generados 
    return jsonify({"access_token": access_token})

#definir la ruta /logout con el metodo DELETE
@auth_bp.route("/logout", methods=["DELETE"])
#proteger la ruta con el decorador jwt_required para requerir un token valido
@jwt_required()
def logout():
    #obtener el token
    token = get_jwt()
    #revoka el token usando la funcion revoke_token
    revoke_token(token)
    #devoler respuesta con el codigo 200 y un mensaje exito
    return jsonify({"message":"Token revoke successfully"}), 200

#definir la ruta /register con el metodo post
@auth_bp.route("/register", methods=["post"])
def register():
    data = request.get_json()
    #validar y deserializar los datos usando el esquema username
    user_schema = UserSchema()
    user = user_schema.load(data)
    error = user_schema.error_messages
    if error:
        return jsonify(error), 400
    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)
    return jsonify(result), 201
