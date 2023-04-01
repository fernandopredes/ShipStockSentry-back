from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from db import db
from models import DailyRecordModel
from schemas import DailyRecordSchema

blp = Blueprint("daily_records", __name__, description="Operations on daily_records")

@blp.route('/daily_record')
class DailyRecordList(MethodView):
    @blp.arguments(DailyRecordSchema)
    @blp.response(201, DailyRecordSchema)
    def post(self, daily_record_data):
        daily_record = DailyRecordModel(**daily_record_data)

        try:
            db.session.add(daily_record)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting a Daily Record.")

        return daily_record

@blp.route('/daily_record/<int:daily_record_id>')
class DailyRecord(MethodView):
    @blp.response(200, DailyRecordSchema)
    def get(self, daily_record_id):
        daily_record = DailyRecordModel.query.get_or_404(daily_record_id)
        return daily_record
