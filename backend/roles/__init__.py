from flask import Blueprint

#crear el blueprint de auth
roles_bp = Blueprint("role", __name__)

#import el blueprint desde el archivo views.py 
from roles import views