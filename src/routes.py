from flask import Blueprint, request, jsonify

frases_blueprint = Blueprint("frases", __name__)
frases_blueprint.db = None  # será injetado em app.py

@frases_blueprint.route("/frases", methods=["GET"])
def get_frase():
    db = frases_blueprint.db
    ano = request.args.get("ano")
    mes = request.args.get("mes")
    dia = request.args.get("dia")

    ref = db.reference("/frases")
    frases = ref.get()

    # Busca por ano, mês e dia
    for key, frase in frases.items():
        if frase.get("ano") == ano and frase.get("mes") == mes and frase.get("dia") == dia:
            return jsonify(frase)
    return jsonify({"erro": "Frase não encontrada"}), 404

@frases_blueprint.route("/frases", methods=["POST"])
def post_frase():
    db = frases_blueprint.db
    data = request.json
    if not all(k in data for k in ("ano", "mes", "dia", "texto")):
        return jsonify({"erro": "Dados incompletos"}), 400

    ref = db.reference("/frases")
    ref.push(data)
    return jsonify({"mensagem": "Frase adicionada com sucesso"}), 201
