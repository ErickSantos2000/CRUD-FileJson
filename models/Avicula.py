from marshmallow import Schema, fields

class Avicula:
    def __init__(self, id, especie, linhagem):
        self.id = id
        self.especie = especie
        self.linhagem = linhagem

    def toDict(self):
        return {
            "id": self.id,
            "especie": self.especie,
            "linhagem": self.linhagem
        }

class AviculaSchema(Schema):
    especie = fields.Str(required=True)
    linhagem = fields.Str(required=True)
