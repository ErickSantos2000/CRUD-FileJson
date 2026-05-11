from marshmallow import Schema, fields

class Galpao:
    def __init__(self, id, identificacao, capacidade):
        self.id = id
        self.identificacao = identificacao 
        self.capacidade = capacidade

    def toDict(self):
        return {
            "id": self.id,
            "identificacao": self.identificacao,
            "capacidade": self.capacidade
        }

class GalpaoSchema(Schema):
    identificacao = fields.Str(required=True)
    capacidade = fields.Int(required=True)

