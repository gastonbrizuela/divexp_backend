from flask import Blueprint

#crear el blueprint de auth
users_bp = Blueprint("user", __name__)

#import el blueprint desde el archivo views.py 
from users import views