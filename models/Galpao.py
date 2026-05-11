from marshmallow import Schema, fields

class Galpao:
    def __init__(self, id, identificacao, capacidade, aviario_id):
        self.id = id
        self.identificacao = identificacao # Ex: "Galpão A1"
        self.capacidade = capacidade
        self.aviario_id = aviario_id

    def toDict(self):
        return {
            "id": self.id,
            "identificacao": self.identificacao,
            "capacidade": self.capacidade,
            "aviario_id": self.aviario_id
        }

class GalpaoSchema(Schema):
    identificacao = fields.Str(required=True)
    capacidade = fields.Int(required=True)
    aviario_id = fields.Int(required=True)

