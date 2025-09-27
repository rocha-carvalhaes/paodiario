"""
Rotas da API do Pão Diário.
"""
from flask import Blueprint, request, jsonify
from services.frase_service import FraseService
from models.frase import Frase

frases_blueprint = Blueprint("frases", __name__)
frases_blueprint.db = None  # será injetado em app.py

# Instância do serviço de frases
frase_service = FraseService()


@frases_blueprint.route("/frases", methods=["GET"])
def get_frase():
    """Busca uma frase específica por data."""
    ano = request.args.get("ano")
    mes = request.args.get("mes")
    dia = request.args.get("dia")
    
    if not all([ano, mes, dia]):
        return jsonify({"erro": "Parâmetros ano, mes e dia são obrigatórios"}), 400
    
    try:
        frase = frase_service.buscar_frase_por_data(ano, mes, dia)
        return jsonify(frase.to_dict())
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


@frases_blueprint.route('/todas-frases', methods=["GET"])
def todas_frases():
    """Lista todas as frases disponíveis."""
    try:
        frases = frase_service.listar_todas_frases()
        return jsonify(frases)
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


@frases_blueprint.route("/frases", methods=["POST"])
def post_frase():
    """Adiciona uma nova frase."""
    data = request.json
    
    if not data:
        return jsonify({"erro": "Dados JSON são obrigatórios"}), 400
    
    if not all(k in data for k in ("ano", "mes", "dia", "texto")):
        return jsonify({"erro": "Dados incompletos. Campos obrigatórios: ano, mes, dia, texto"}), 400
    
    try:
        frase = Frase.from_dict(data)
        sucesso = frase_service.firebase.salvar_frase(frase)
        
        if sucesso:
            return jsonify({"mensagem": "Frase adicionada com sucesso", "chave": frase.chave}), 201
        else:
            return jsonify({"erro": "Erro ao salvar frase"}), 500
            
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


@frases_blueprint.route("/gerar-frase", methods=["POST"])
def gerar_frase():
    """Gera uma nova frase do dia automaticamente."""
    try:
        frase = frase_service.gerar_frase_do_dia()
        return jsonify({
            "mensagem": "Frase gerada com sucesso",
            "frase": frase.to_dict(),
            "chave": frase.chave
        }), 201
    except Exception as e:
        return jsonify({"erro": f"Erro ao gerar frase: {str(e)}"}), 500
