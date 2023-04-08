from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt


from db import db
from models import UserModel, DailyRecordModel
from schemas import UserSchema, UserLoginSchema, DailyRecordSchema

blp = Blueprint("Users", __name__, description="Operations on Users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.doc(summary="Rota para registrar um usuário")
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

@blp.route("/login")
class UserLogin(MethodView):
    @blp.doc(summary="Rota para realizar o login de um usuário")
    @blp.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data['email']
        ).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token, "user_id": user.id}

        abort(401, message="Invalid cedentials.")



@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.doc(summary="Rota para pegar um único usuário pelo id")
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user


@blp.route("/user/<int:user_id>/daily_records")
class UserRecordsList(MethodView):
    @blp.doc(summary="Rota para pegar todos os daily_records de um único usuário")
    @jwt_required()
    @blp.response(200, DailyRecordSchema(many=True))
    def get(self, user_id):
        daily_records = DailyRecordModel.query.filter_by(user_id=user_id).all()
        return daily_records
