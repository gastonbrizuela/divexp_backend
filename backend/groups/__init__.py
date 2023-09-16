from flask import Blueprint

#crear el blueprint de auth
groups_bp = Blueprint("groups", __name__)

#import el blueprint desde el archivo views.py 
from groups import views