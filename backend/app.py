from flask import Flask
from config import Config
from config import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


# crear la aplicacion Flask
app = Flask(__name__)

#carga la configuracion desde el archivo config
app.config.from_object(Config)
migrate = Migrate(app, db)
db.init_app(app)
jwt = JWTManager(app)

from auth import auth_bp
from users import users_bp
from roles import roles_bp
from groups import groups_bp

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(groups_bp)

# ejecutar la aplicacion si se eejacuta este archivo

if __name__ == "__main__":
    app.run()