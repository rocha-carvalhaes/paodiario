import os
import json
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, db as realtime_db
from routes import frases_blueprint

# Configura aplicação Flask
app = Flask(__name__)
CORS(app)

# Declara as variáveis de ambiente
FLASK_ENV = os.getenv("FLASK_ENV", "development")
FIREBASE_URL = os.getenv("FIREBASE_URL")
FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON")

# Estrutura as credenciais do Firebase
cred_dict = json.loads(FIREBASE_CREDENTIALS_JSON)
cred = credentials.Certificate(cred_dict)

# Inicializa Firebase com Realtime Database
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_URL
})

# Injeta o db (cliente) nas rotas
frases_blueprint.db = realtime_db
app.register_blueprint(frases_blueprint)

# Roda o app na porta 5000 por padrão
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
