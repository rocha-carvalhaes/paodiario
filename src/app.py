import os
import json
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, db as realtime_db
from routes import frases_blueprint

app = Flask(__name__)
CORS(app)

FLASK_ENV = os.getenv("FLASK_ENV", "development")

if FLASK_ENV == "production":
    firebase_config = os.getenv("FIREBASE_CREDENTIALS_JSON")
    if not firebase_config:
        raise ValueError("A variável de ambiente FIREBASE_CREDENTIALS_JSON não está definida.")
    cred_dict = json.loads(firebase_config)
    cred = credentials.Certificate(cred_dict)
else:
    cred = credentials.Certificate("pao-diario-3f630-firebase-adminsdk-fbsvc-dabbcc0d41.json")

# Inicializa Firebase com Realtime Database
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pao-diario-3f630-default-rtdb.firebaseio.com/'
})

# Injeta o db (cliente) nas rotas
frases_blueprint.db = realtime_db
app.register_blueprint(frases_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
