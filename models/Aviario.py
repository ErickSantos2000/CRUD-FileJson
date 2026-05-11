from marshmallow import Schema, fields

class Aviario:
    def __init__(self, id, nome, endereco, avicultor_id):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.avicultor_id = avicultor_id

    def toDict(self):
        return {
            "id": self.id, 
            "nome": self.nome, 
            "endereco": self.endereco, 
            "avicultor_id": self.avicultor_id
        }

class AviarioSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "O nome do aviário é obrigatório."})
    endereco = fields.Str(required=True)
    avicultor_id = fields.Int(required=True)
