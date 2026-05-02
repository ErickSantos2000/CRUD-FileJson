from flask import Flask, jsonify
from models.Avicultor import Avicultor

app = Flask(__name__)

@app.get("/avicultores")
def getAvicultores():
    pass


@app.post("/avicultores")
def postAvicultores():
    pass


@app.put("/avicultores")
def putAvicultores():
    pass


@app.delete("/avicultores")
def deleteAvicultores():
    pass

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200