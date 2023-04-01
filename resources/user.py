from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt


from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", __name__, description="Operations on Users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.name == user_data["name"]).first():
            abort(409, message="Já existe um usuário com esse nome.")

        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message="Já existe um usuário com esse e-mail.")

        user = UserModel(
            name = user_data["name"],
            email = user_data["email"],
            password = pbkdf2_sha256.hash(user_data["password"]),
            ship_name = user_data["ship_name"]
        )
        db.session.add(user)
        db.session.commit()

        return {"message" : "Usuário criado."}, 201
