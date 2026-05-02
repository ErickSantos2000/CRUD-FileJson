from flask import Flask, request
from models.Avicultor import Avicultor
import os, json

app = Flask(__name__)

@app.get("/avicultores")
def getAvicultores():
    # nome do arquivo JSON
    arquivo_json = "avicultores.json"

    # verifica se o arquivo JSON existe
    if os.path.exists(arquivo_json):
        # abre o arquivo no modo leitura "r" read
        # with é um gerenciador de contexto, ele garante que o arquivo seja fechado assim que o codigo terminar a execução
        # as f cria um apelido para o arquivo aberto 
        with open(arquivo_json, "r") as f:
            # le o arquivo JSON e converte para um OBJ Python, neste caso uma lista ou dicionario
            lista_avicultores = json.load(f)
    
    else:
        lista_avicultores = []

    return lista_avicultores, 200


@app.post("/avicultores")
def postAvicultores():
    # recebe dados enviados pelo Thunder Client
    dados = request.get_json()

    # transforma dados em um OBJ da classe Avicultor
    novo_avicultor = Avicultor (
        nome=dados.get("nome"),
        nascimento=dados.get("nascimento"),
        cpf=dados.get("cpf"),
        caf=dados.get("caf")
    )

    # nome do arquivo JSON
    arquivo_json = "avicultores.json"

    # verifica se o arquivo JSON existe
    if os.path.exists(arquivo_json):
        # abre o arquivo no modo leitura "r" read
        # with é um gerenciador de contexto, ele garante que o arquivo seja fechado assim que o codigo terminar a execução
        # as f cria um apelido para o arquivo aberto 
        with open(arquivo_json, "r") as f:
            # le o arquivo JSON e converte para um OBJ Python, neste caso uma lista ou dicionario
            lista_avicultores = json.load(f)
    
    else:
        lista_avicultores = []

    # converte o novo avicultor em um dicionario e adiciona a lista de avicultores
    lista_avicultores.append(novo_avicultor.toDict())

    # "w" write, abre o arquivo no modo de escrita
    # o modo "w" apaga tudo que existia no arquivo e escreve a lista atualizada
    with open(arquivo_json, "w") as f:
        # pega lista de diciorios e a traduz para o formato JSON
        json.dump(lista_avicultores, f, indent=4, ensure_ascii=False)

    return {"mensagem": f"Avicultor {novo_avicultor.nome} cadastrado"}, 201

@app.put("/avicultores/<nome>")
def putAvicultores(nome):

    dados = request.get_json()
    arquivo_json = "avicultores.json"

    with open(arquivo_json, "r") as f:
        lista_avicultores = json.load(f)

    for avicultor in lista_avicultores:
        if avicultor["nome"] == nome:
            avicultor["nome"] = dados.get("nome")
            avicultor["nascimento"] =dados.get("nascimento")
            avicultor["cpf"] =dados.get("cpf")
            avicultor["caf"] =dados.get("caf")
            break
    with open(arquivo_json, "w") as f:
        # pega lista de diciorios e a traduz para o formato JSON
        json.dump(lista_avicultores, f, indent=4, ensure_ascii=False)

    return {"mensagem": f"Dados de {nome} atualizados com sucesso"}, 200

@app.delete("/avicultores/<nome>")
def deleteAvicultores(nome):
    
    arquivo_json = "avicultores.json"

    if os.path.exists(arquivo_json):
        with open(arquivo_json, "r") as f:
            lista_avicultores = json.load(f)

    else:
        return {"erro": "nenhum avicultor cadastrado"}

    nova_lista = [a for a in lista_avicultores if a["nome"] != nome]

    with open(arquivo_json, "w") as f:
        json.dump(nova_lista, f,indent=4, ensure_ascii=False)

    return {"mensagem": f"Avicultor {nome} deletado"}, 200

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200