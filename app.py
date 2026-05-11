from flask import Flask, request, jsonify
from models.Avicultor import Avicultor, AvicultorSchema
from models.Aviario import Aviario, AviarioSchema
from models.Galpao import Galpao, GalpaoSchema
from models.Avicula import Avicula, AviculaSchema
from marshmallow import ValidationError
import sqlite3
from helpers.database import get_conn


app = Flask(__name__)

# --- ENDPOINTS AVICULTORES ---

@app.get("/avicultores")
def getAvicultores():
    avicultores = []
    # DB
    conn = None

    # 1 - Abrir a conexão
    conn = get_conn()

    # 2 - Recuperar o cursor
    cursor = conn.cursor()

    # 3 - Preparar a consultar: query | statement
    cursor.execute("select * from tb_avicultor")

    # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
    rows = cursor.fetchall()

    for row in rows:
        id = row[0]
        nome = row[1]
        nascimento = row[2]
        cpf = row[3]
        caf = row[4]
        avicultor = Avicultor(id, nome, nascimento, cpf, caf)
        avicultores.append(avicultor.toDict())

    # 5 - Fechar a conexão
    if conn:
        conn.close()

    return avicultores, 200


@app.post("/avicultores")
def postAvicultores():
    try:
        avicultorJson = request.get_json()
        schema = AvicultorSchema()
        # Valida os dados de entrada
        dados_validados = schema.load(avicultorJson)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # DB
    conn = None

    # 1 - Abrir a conexão
    conn = get_conn()

    # 2 - Recuperar o cursor
    cursor = conn.cursor()

    # 3 - Preparar a consultar: query | statement
    cursor.execute(
        "INSERT INTO tb_avicultor(nome, nascimento, cpf, caf) VALUES(?, ?, ?, ?)", 
        (dados_validados["nome"], str(dados_validados["nascimento"]), dados_validados["cpf"], dados_validados["caf"]))

    # 4.2 - Confirmar operação.
    conn.commit()

    # 5 - Fechar a conexão
    if conn:
        conn.close()

    return dados_validados, 201


@app.put("/avicultores/<int:id>")
def putAvicultores(id):
    try:
        avicultorJson = request.get_json()
        schema = AvicultorSchema()
        # Valida os dados recebidos conforme as regras do Marshmallow
        dados_validados = schema.load(avicultorJson)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # DB
    conn = None
 
    # 1 - Abrir a conexão
    conn = get_conn()

    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    
    # 3 - Preparar a consultar: query | statement
    cursor.execute(
        "UPDATE tb_avicultor SET nome=?, nascimento=?, cpf=?, caf=? WHERE id=?",
        (dados_validados["nome"], str(dados_validados["nascimento"]), dados_validados["cpf"], dados_validados["caf"], id)
    )

    # 4.2 - Confirmar operação.
    conn.commit()
    
    # Verifica se algum registro foi de fato alterado
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Avicultor não encontrado"}, 404

    # 5 - Fechar a conexão
    if conn:
        conn.close()

    return dados_validados, 200


@app.delete("/avicultores/<int:id>")
def deleteAvicultores(id):
    # DB
    conn = None
   
    # 1 - Abrir a conexão
    conn = get_conn()

    # 2 - Recuperar o cursor
    cursor = conn.cursor()

    # 3 - Preparar a consultar: query | statement
    cursor.execute("DELETE FROM tb_avicultor WHERE id=?", (id,))

    # 4.2 - Confirmar operação.
    conn.commit()
    
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Avicultor não encontrado"}, 404
        
    # 5 - Fechar a conexão
    if conn:
        conn.close()

    return {"message": "Avicultor deletado com sucesso"}, 200


# --- ENDPOINTS AVÍCULAS ---

@app.get("/aviculas")
def getAviculas():
    aviculas = []
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("select * from tb_avicula")
    # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        especie = row[1]
        linhagem = row[2]
        obj = Avicula(id, especie, linhagem)
        aviculas.append(obj.toDict())
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return aviculas, 200

@app.post("/aviculas")
def postAviculas():
    try:
        json_data = request.get_json()
        schema = AviculaSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("INSERT INTO tb_avicula(especie, linhagem) VALUES(?, ?)", (dados["especie"], dados["linhagem"]))
    # 4.2 - Confirmar operação.
    conn.commit()
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 201

@app.put("/aviculas/<int:id>")
def putAviculas(id):
    try:
        json_data = request.get_json()
        schema = AviculaSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("UPDATE tb_avicula SET especie=?, linhagem=? WHERE id=?", (dados["especie"], dados["linhagem"], id))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Avícula não encontrada"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 200

@app.delete("/aviculas/<int:id>")
def deleteAviculas(id):
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("DELETE FROM tb_avicula WHERE id=?", (id,))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Avícula não encontrada"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return {"message": "Avícula deletada com sucesso"}, 200


# --- ENDPOINTS GALPÕES ---

@app.get("/galpoes")
def getGalpoes():
    galpoes = []
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("select * from tb_galpao")
    # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        identificacao = row[1]
        capacidade = row[2]
        obj = Galpao(id, identificacao, capacidade)
        galpoes.append(obj.toDict())
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return galpoes, 200

@app.post("/galpoes")
def postGalpoes():
    try:
        json_data = request.get_json()
        schema = GalpaoSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("INSERT INTO tb_galpao(identificacao, capacidade) VALUES(?, ?)", (dados["identificacao"], dados["capacidade"]))
    # 4.2 - Confirmar operação.
    conn.commit()
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 201

@app.put("/galpoes/<int:id>")
def putGalpoes(id):
    try:
        json_data = request.get_json()
        schema = GalpaoSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("UPDATE tb_galpao SET identificacao=?, capacidade=? WHERE id=?", (dados["identificacao"], dados["capacidade"], id))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Galpão não encontrado"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 200

@app.delete("/galpoes/<int:id>")
def deleteGalpoes(id):
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("DELETE FROM tb_galpao WHERE id=?", (id,))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Galpão não encontrado"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return {"message": "Galpão deletado com sucesso"}, 200


# --- ENDPOINTS AVIÁRIOS ---

@app.get("/aviarios")
def getAviarios():
    aviarios = []
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("select * from tb_aviario")
    # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        nome = row[1]
        capacidade = row[2]
        obj = Aviario(id, nome, capacidade)
        aviarios.append(obj.toDict())
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return aviarios, 200

@app.post("/aviarios")
def postAviarios():
    try:
        json_data = request.get_json()
        schema = AviarioSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("INSERT INTO tb_aviario(nome, capacidade) VALUES(?, ?)", (dados["nome"], dados["capacidade"]))
    # 4.2 - Confirmar operação.
    conn.commit()
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 201

@app.put("/aviarios/<int:id>")
def putAviarios(id):
    try:
        json_data = request.get_json()
        schema = AviarioSchema()
        dados = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("UPDATE tb_aviario SET nome=?, capacidade=? WHERE id=?", (dados["nome"], dados["capacidade"], id))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Aviário não encontrado"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return dados, 200

@app.delete("/aviarios/<int:id>")
def deleteAviarios(id):
    # DB
    conn = None
    # 1 - Abrir a conexão
    conn = get_conn()
    # 2 - Recuperar o cursor
    cursor = conn.cursor()
    # 3 - Preparar a consultar: query | statement
    cursor.execute("DELETE FROM tb_aviario WHERE id=?", (id,))
    # 4.2 - Confirmar operação.
    conn.commit()
    if cursor.rowcount == 0:
        if conn: conn.close()
        return {"error": "Aviário não encontrado"}, 404
    # 5 - Fechar a conexão
    if conn:
        conn.close()
    return {"message": "Aviário deletado com sucesso"}, 200


@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200
