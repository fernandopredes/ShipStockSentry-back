from db import db
import datetime

class DailyRecordModel(db.Model):
    __tablename__ = 'daily_records'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.date.today)
    diesel = db.Column(db.Float, nullable=False)
    drill_water = db.Column(db.Float, nullable=False)
    fresh_water = db.Column(db.Float, nullable=False)
    bentonite = db.Column(db.Float, nullable=False)
    barite = db.Column(db.Float, nullable=False)
    limestone = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False)

    # Relationship with UserModel
    user = db.relationship("UserModel", back_populates="daily_records")
