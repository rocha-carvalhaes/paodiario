"""
Aplicação principal do Pão Diário.
"""
import os
import firebase_admin
from firebase_admin import credentials, db as realtime_db
from flask import Flask
from flask_cors import CORS

from config.settings import Config
from api.routes import frases_blueprint


def create_app():
    """Factory function para criar a aplicação Flask."""
    app = Flask(__name__)
    CORS(app)
    
    # Valida configurações
    Config.validate_config()
    
    # Configura Firebase
    _setup_firebase()
    
    # Registra blueprints
    app.register_blueprint(frases_blueprint)
    
    return app


def _setup_firebase():
    """Configura e inicializa o Firebase."""
    try:
        cred_dict = Config.get_firebase_credentials()
        cred = credentials.Certificate(cred_dict)
        
        firebase_admin.initialize_app(cred, {
            'databaseURL': Config.FIREBASE_URL
        })
        
        # Injeta o db nas rotas
        frases_blueprint.db = realtime_db
        print("✅ Firebase configurado com sucesso")
        
    except Exception as e:
        print(f"⚠️ Aviso: Firebase não configurado: {e}")
        print("⚠️ A aplicação funcionará, mas sem persistência de dados")
        # Não falha a aplicação, apenas avisa


# Cria a aplicação
app = create_app()

# Roda o app na porta 5000 por padrão
if __name__ == "__main__":
    port = Config.PORT
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=port)
