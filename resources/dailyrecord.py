from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from flask_jwt_extended import jwt_required

from db import db
from models import DailyRecordModel
from schemas import DailyRecordSchema, UpdateRecordSchema, DailyRecordDelSchema

blp = Blueprint("Daily Records", __name__, description="Operações de vizualização, adição, remoção e edição com Daily Records")

@blp.route('/daily_record')
class DailyRecordList(MethodView):
    @jwt_required()
    @blp.arguments(DailyRecordSchema)
    @blp.response(201, DailyRecordSchema, description="Sucesso. Retorna as informações do daily_record criado.")
    def post(self, daily_record_data):
        """Rota para postar um daily_record

        Retorna uma representação das informações enviadas de um daily record.

        """
        daily_record = DailyRecordModel(**daily_record_data)

        try:
            db.session.add(daily_record)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Um erro ocorreu ao tentar criar um Daily Record.")

        return daily_record

@blp.route('/daily_record/<int:daily_record_id>')
class DailyRecord(MethodView):
    @blp.response(200, DailyRecordSchema, description="Sucesso. Retorna as informações recebidas do daily_record referente ao id escolhido.")
    @jwt_required()
    def get(self, daily_record_id):
        """ Rota para pegar um daily_record pelo id

        Retorna uma representação das informações recebidas de um daily record.

        """
        daily_record = DailyRecordModel.query.get_or_404(daily_record_id)
        return daily_record

    @jwt_required()
    @blp.arguments(UpdateRecordSchema)
    @blp.response(200, DailyRecordSchema, description="Sucesso. Retorna as novas informações editadas do daily_record referente ao id escolhido.")
    def put(self, daily_record_data, daily_record_id):
        """ Rota para editar um daily_record de acordo com o id

        Retorna uma representação das informações editadas de um daily record.

        """
        daily_record = DailyRecordModel.query.get(daily_record_id)
        if daily_record:
            if daily_record_data.get('date') is not None:
                daily_record.date = daily_record_data['date']
            daily_record.diesel = daily_record_data['diesel']
            daily_record.drill_water = daily_record_data['drill_water']
            daily_record.fresh_water = daily_record_data['fresh_water']
            daily_record.bentonite = daily_record_data['bentonite']
            daily_record.barite = daily_record_data['barite']
            daily_record.limestone = daily_record_data['limestone']
        else:
            daily_record = DailyRecordModel(id=daily_record_id, **daily_record_data)

        db.session.add(daily_record)
        db.session.commit()

        return daily_record

    @jwt_required()
    @blp.response(200, DailyRecordDelSchema, description="Retorna uma mensagem de sucesso e o daily_record removido")
    @blp.response(404, description="O id não foi encontrado.")
    def delete(self, daily_record_id):
        """ Rota para deletar um daily_record pelo id

        Retorna uma mensagem confirmando que o daily_record selecionado foi deletado.

        """
        daily_record = DailyRecordModel.query.get_or_404(daily_record_id)
        db.session.delete(daily_record)
        db.session.commit()
        return {"message":"ROB deletado"}, 200
