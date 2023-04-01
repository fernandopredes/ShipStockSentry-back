from marshmallow import Schema, fields

class DailyRecordSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=False, missing=None)
    diesel = fields.Float(required=True)
    drill_water = fields.Float(required=True)
    fresh_water = fields.Float(required=True)
    bentonite = fields.Float(required=True)
    barite = fields.Float(required=True)
    limestone = fields.Float(required=True)
    user_id = fields.Integer(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True)
    ship_name = fields.Str(required=True)
    daily_records = fields.List(fields.Nested(DailyRecordSchema()), dump_only=True)

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
