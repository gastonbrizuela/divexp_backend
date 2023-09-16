#schema.py 
from config import db
from models import User, Role, Groups
from marshmallow import fields, Schema

# definir el esquema RoleSchema que hereda SQLAlchemyAutoSchema y usa el modelo Role
class RoleSchema(Schema):
    model = Role
    sql_session = db.session 
    load_instance = True
    name = fields.String()


class UserSchema(Schema):
    class Meta:
        model = User
        sql_session = db.session
        load_instance = True
    password_hash = fields.String(load_only=True)
    password = fields.String(dump_only=True)
    username = fields.String(dump_only=True)
    email = fields.String()
    roles = fields.Nested(RoleSchema(), many=True)
    
class groupsSchema(Schema):
    class Meta:
        model = Groups
        sql_session=db.session
        load_intance = True
    name = fields.String()
    id = fields.String()
    members = fields.Nested(UserSchema(), many = True)


