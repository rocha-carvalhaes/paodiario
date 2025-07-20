import os
import json
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
from routes import frases_blueprint

app = Flask(__name__)
CORS(app)

# Detecta ambiente (DEV ou PROD)
FLASK_ENV = os.getenv("FLASK_ENV", "development")

if FLASK_ENV == "production":
    # Lê variável de ambiente com o conteúdo do JSON
    firebase_config = os.getenv("FIREBASE_CREDENTIALS_JSON")
    if not firebase_config:
        raise ValueError("A variável de ambiente FIREBASE_CREDENTIALS_JSON não está definida.")
    cred_dict = json.loads(firebase_config)
    cred = credentials.Certificate(cred_dict)
else:
    # Modo desenvolvimento: lê do arquivo local
    cred = credentials.Certificate("serviceAccountKey.json")

# Inicializa Firebase
firebase_admin.initialize_app(cred)
db = firestore.client()

# Injeta db nas rotas
frases_blueprint.db = db
app.register_blueprint(frases_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
