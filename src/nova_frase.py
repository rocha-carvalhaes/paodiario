import os
import requests
import datetime
import google.generativeai as genai

# Variáveis de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "development")
FIREBASE_URL = os.getenv("FIREBASE_URL", "development")

# Configuração da API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Prompt estilo tia do zap
prompt = """
Gere uma mensagem de bom dia no estilo de uma 'tia do zap'. A mensagem deve ser amorosa, motivacional, incluir emojis e opcionalmente uma citação bíblica curta.
Use no máximo 300 caracteres. Não repita mensagens anteriores.
"""

response = model.generate_content(prompt)
frase = response.text.strip().replace("\n", " ")

# Data atual
hoje = datetime.date.today()
ano = str(hoje.year)
mes = f"{hoje.month:02d}"
dia = f"{hoje.day:02d}"
chave = f"{ano}{mes}{dia}"

payload = {
    "ano": ano,
    "mes": mes,
    "dia": dia,
    "texto": frase
}

# Salva no Firebase
url = f"{FIREBASE_URL}/frases/{chave}.json"
res = requests.put(url, json=payload)

if res.ok:
    print(f"✅ Frase salva: {frase}")
else:
    print(f"❌ Erro ao salvar: {res.status_code} - {res.text}")
