#auth/utils.py
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request, get_jwt

#crea una lista vacia para guardar los tokens revocados 
revoked_tokens = []

# definir la funcion revoke_token que recibe un toke y lo agrega a la lista de tokens revocados
def revoke_token(token):
    #obtener el jti (identificador unico ) del token
    jti = token["jti"]
    #agregar el jti a la lista de tokens revocados
    revoke_tokens.append(jti)

# definir la funcion is_token_revoked que recibe un token y verifica si esta revocado o no 
def is_token_revoked(token):
    jti = token["jti"]

    if jti in revoked_tokens:
        return True
    return False

# definir la funcion admin_required que verifica si el usuario tiene el rol de administrador o no

def admin_required():
    # verifica si el token es valido en el request
    verify_jwt_in_request()
    #obtener la identidad del token (el id del usuario)
    user_id = get_jwt_identity()
    #busca el usuario por su id en la base de datos
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"message":"User not Found"}), 404
    
    #si encuentra al usuario verifica si tiene el role de administrador entre sus roles

    if admin_role in user.roles:
        #si tiene el rol de administrador, devolver true
        return True
    else:
        return jsonify({"message":"Admind role required"}), 403