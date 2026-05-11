from marshmallow import Schema, fields, validate

class Avicultor():
    def __init__(self, id, nome, nascimento, cpf, caf):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.caf = caf

    def toDict(self):
        return {
            "id": self.id, 
            "nome": self.nome, 
            "nascimento": self.nascimento, 
            "cpf": self.cpf, 
            "caf": self.caf
            }

class AvicultorSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "Adicione um nome."})
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(max=11, error="Tamanho do CPF inválido."), error_messages={"required": "Adicione um CPF.", "invalid": "Valor inválido."})
    caf = fields.Str(required=True)