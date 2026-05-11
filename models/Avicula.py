from marshmallow import Schema, fields

class Avicula:
    def __init__(self, id, especie, linhagem, galpao_id):
        self.id = id
        self.especie = especie # Ex: "Frango de Corte"
        self.linhagem = linhagem # Ex: "Cobb", "Ross"
        self.galpao_id = galpao_id

    def toDict(self):
        return {
            "id": self.id,
            "especie": self.especie,
            "linhagem": self.linhagem,
            "galpao_id": self.galpao_id
        }

class AviculaSchema(Schema):
    especie = fields.Str(required=True)
    linhagem = fields.Str(required=True)
    galpao_id = fields.Int(required=True)
