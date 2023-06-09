from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    ship_name = db.Column(db.String(120), nullable=False)

    # Relationship with DailyRecordModel
    daily_records = db.relationship("DailyRecordModel", back_populates="user", lazy=True, cascade="all,delete")
