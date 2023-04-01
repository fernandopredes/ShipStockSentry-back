from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.Email(required=True, unique=True)
    password = fields.String(required=True)
    ship_name = fields.String(required=True, unique=True)
    daily_records = fields.Nested("DailyRecordSchema", many=True)

class DailyRecordSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=True)
    diesel = fields.Float(required=True)
    drill_water = fields.Float(required=True)
    fresh_water = fields.Float(required=True)
    bentonite = fields.Float(required=True)
    barite = fields.Float(required=True)
    limestone = fields.Float(required=True)
    user_id = fields.Integer(required=True)
    user = fields.Nested(UserSchema, exclude=("daily_records"))
