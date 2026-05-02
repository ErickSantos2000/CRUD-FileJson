class Avicultor():
    def __init__(self, nome, nascimento, cpf, caf):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.caf = caf

    def toDict(self):
        return {"nome": self.nome, "nascimento": self.nascimento,
                "cpf": self.cpf, "caf": self.caf}
    

    