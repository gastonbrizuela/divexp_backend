from config import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

#definir el modelo Role que repesenta los roles del usuarios
class Role (db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship("User", secondary="user_roles", back_populates="roles")

 #definir el metodo __repre__ para mostrar luna representacion del objeto

    def __repr__(self):
        return f"<Role {self.name}>"

class Groups(db.Model):
    __tablename__ = "groups"
    name = db.Column(db.String(50), nullable=False)
    members = db.relationship("User", secondary="group_users", back_populates="groups")
    id = db.Column(db.String(50),primary_key=True)

    def __init__(self, data):
        self.id = uuid.uuid4()
        name = data['name']

    group_users = db.Table("group_users", 
                        db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                        db.Column("group_id", db.String(50),db.ForeignKey("groups.id"), primary_key=True))

    
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # corregir el nombre del campo y usar un solo guión bajo
    password_hash = db.Column("password_hash", db.String(128), nullable=False)
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")
    groups = db.relationship("Groups", secondary="group_users", back_populates="members")

    def __init__(self, data):
        self.id= data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']

    def __repr__(self):
        return f"<Role {self.username}>"
    @classmethod
    def get_user_roles(self, id):
        user = self.query.filter_by(id=id).first()
        return user 

    
    #definir una propiedad password para acceder al campo  password_hash
    @property
    def password(self):
        print('llega al password property')
        return self.password_hash

    #definir un setter password para asignar un valor al campo password_has usando un hash seguro

    @password.setter
    def password(self, value):
        print('llega al password setter')
        self.password_hash = generate_password_hash(value)

    #definir un metodo chech_password para verificar si una contraseña coincide con el hash almacenado
    def check_password(self, value):
        print(self.password_hash)
        print(value)
        result = check_password_hash(self.password_hash, value)
        print(f"resultado {result}")
        return result
    #definir las tablas intermedias de user_roles que relaciona los modes user y role usando sus claves foraneas

    user_roles = db.Table("user_roles", 
                            db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                            db.Column("role_id", db.Integer,db.ForeignKey("roles.id"), primary_key=True))
