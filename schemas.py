from marshmallow import Schema, fields

class DailyRecordSchema(Schema):
    """
    Define como deve ser a estrutura do dado após a criação de um novo daily record.
    """
    id = fields.Integer(description="id do daily record")
    date = fields.Date(required=False, missing=None, description="data de criação do daily record")
    diesel = fields.Float(required=True, description="volume de diesel")
    drill_water = fields.Float(required=True, description="volume de drill water")
    fresh_water = fields.Float(required=True, description="volume de fresh water")
    bentonite = fields.Float(required=True, description="volume de bentonita")
    barite = fields.Float(required=True, description="volume de baritina")
    limestone = fields.Float(required=True, description="volume de calcário")
    user_id = fields.Integer(required=True, description="id do usuário que criou o daily record")

    class Meta:
        description = "Define como um novo daily record a ser inserido deve ser representado"

class UpdateRecordSchema(Schema):
    """
    Define como deve ser a estrutura do dado após a edição de um daily record.
    """
    date = fields.Date(required=False, missing=None, description="data de criação do daily record")
    diesel = fields.Float(required=True, description="volume de diesel")
    drill_water = fields.Float(required=True, description="volume de drill water")
    fresh_water = fields.Float(required=True, description="volume de fresh water")
    bentonite = fields.Float(required=True, description="volume de bentonita")
    barite = fields.Float(required=True, description="volume de baritina")
    limestone = fields.Float(required=True, description="volume de calcário")

    class Meta:
        description = "Define como um daily record que foi editado deve ser representado"


class UserSchema(Schema):
    """
    Define como deve ser a estrutura do dado após criação de um novo usuário.
    """
    id = fields.Int(dump_only=True, description="id do usuário")
    name = fields.Str(required=True, description="nome do usuário")
    password = fields.Str(required=True, load_only=True, description="password do usuário")
    email = fields.Email(required=True, description="e-mail do usuário")
    ship_name = fields.Str(required=True, description="nome da embarcação do usuário")
    daily_records = fields.List(fields.Nested(DailyRecordSchema()), dump_only=True, description="todos os daily records criados pelo usuário")

    class Meta:
        description = "Define como um novo usuário a ser inserido deve ser representado"

class UserLoginSchema(Schema):
    """
    Define como deve ser a estrutura para realizar o login de um usuário.
    """
    email = fields.Email(required=True, description="e-mail do usuário")
    password = fields.Str(required=True, load_only=True, description="password do usuário")

    class Meta:
        description = "Define como um login de usuário deve ser representado"

class DailyRecordDelSchema(Schema):
    """
    Define como deve ser a estrutura do dado após uma requisição de remoção do daily record.
    """
    message = fields.String(description="Mensagem de status da operação")
    id = fields.Int(description="Id do daily record removido")

    class Meta:
        description = "Esquema para resposta da rota de remoção de daily record"

class CreateUserSchema(Schema):
    """
    Define como deve ser a estrutura do dado após criação de usuário.
    """
    message = fields.String(description="Mensagem de usuário criado")

    class Meta:
        description = "Esquema de mensagem após a criação de usuário."

class UserTokenSchema(Schema):
    """
    Define como deve ser a estrutura do dado após um login.
    """
    access_token = fields.String(description="Token de acesso")
    user_id = fields.Int(description="Id do usuário")

    class Meta:
        description = "Esquema para resposta da rota de login do usuário"
