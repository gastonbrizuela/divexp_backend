from flask import Blueprint

#crear el blueprint de auth
auth_bp = Blueprint("auth", __name__)

#import el blueprint desde el archivo views.py 
from auth import views