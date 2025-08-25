import os
import requests
import datetime
import google.generativeai as genai
from scrapper_mensagem import ScrapperMensagem

# Variáveis de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FIREBASE_URL = os.getenv("FIREBASE_URL")

# Configuração da API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-pro")

mensagem_base = ScrapperMensagem().coletar_mensagem()

# Prompt
prompt = f"""
Gere uma mensagem de bom dia no estilo de uma "tia do zap".
A mensagem deve começar com uma frase inicial curta e significativa, em torno de 6 palavras, que traga impacto e sentido.
Em seguida, desenvolva o ensinamento do dia de forma motivacional, amorosa e ecumênica, inspirado no texto a seguir mas em tom ecumênico:
{mensagem_base}
Inclua emojis para transmitir carinho e leveza.
Termine sempre com "Bom dia!" seguido da referência bíblica no formato (Livro capítulo, versículo).
Use no máximo 300 caracteres.
"""

# Pega a resposta do modelo
response = model.generate_content(prompt)
frase = response.text.strip().replace("\n", "")

# Estrutura a chave para o Firebase
hoje = datetime.datetime.now()
ano = str(hoje.year)
mes = f"{hoje.month:02d}"
dia = f"{hoje.day:02d}"
horaminuto = f"{hoje.hour:02d}{hoje.minute:02d}"
chave = f"{ano}{mes}{dia}-{horaminuto}"

# Estrutura o payload
payload = {
    "ano": ano,
    "mes": mes,
    "dia": dia,
    "texto": frase
}

# Salva no Firebase
url = f"{FIREBASE_URL}/frases/{chave}.json"
res = requests.put(url, json=payload)

# Verifica se a requisição foi bem-sucedida
if res.ok:
    print(f"✅ Frase salva: {frase}")
else:
    print(f"❌ Erro ao salvar: {res.status_code} - {res.text}")
