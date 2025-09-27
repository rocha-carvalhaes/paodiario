import os
import requests
import datetime
import google.generativeai as genai
from scrapper_mensagem import ScrapperMensagem

# Desenvolvimento local
from dotenv import load_dotenv
load_dotenv()

# Variáveis de ambiente
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FIREBASE_URL = os.getenv("FIREBASE_URL")

# Validação das variáveis de ambiente
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não está definida nas variáveis de ambiente")
if not FIREBASE_URL:
    raise ValueError("FIREBASE_URL não está definida nas variáveis de ambiente")

# Configuração da API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Coleta a mensagem base com tratamento de erro
try:
    mensagem_base = ScrapperMensagem().coletar_mensagem()
    print(f"✅ Mensagem coletada com sucesso: {mensagem_base[:50]}...")
except Exception as e:
    print(f"❌ Erro ao coletar mensagem: {e}")
    mensagem_base = "Que este dia seja abençoado com paz, amor e sabedoria."

# Prompt
prompt = f"""
Gere uma mensagem de bom dia no estilo de uma "tia do zap".
A mensagem deve começar com uma frase inicial curta e significativa, em torno de 6 palavras, que traga impacto e sentido.
Em seguida, desenvolva o ensinamento do dia de forma motivacional, amorosa e ecumênica, inspirado no texto a seguir mas em tom ecumênico:
{mensagem_base}
Inclua emojis para transmitir carinho e leveza.
Termine sempre com "Bom dia!" seguido da referência bíblica no formato (Livro por extenso, capítulo, versículo).
Use no máximo 300 caracteres.
"""

# Pega a resposta do modelo
try:
    response = model.generate_content(prompt)
    if not response.text:
        raise ValueError("Resposta vazia do modelo Gemini")
    frase = response.text.strip().replace("\n", "")
    print(f"✅ Frase gerada com sucesso: {frase[:50]}...")
except Exception as e:
    print(f"❌ Erro ao gerar frase: {e}")
    frase = "🌅 Que este novo dia traga paz, amor e muitas bênçãos! Bom dia! (Salmos 118:24)"

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
try:
    url = f"{FIREBASE_URL}/frases/{chave}.json"
    res = requests.put(url, json=payload, timeout=10)
    
    # Verifica se a requisição foi bem-sucedida
    if res.ok:
        print(f"✅ Frase salva com sucesso no Firebase: {frase}")
        print(f"📅 Chave: {chave}")
    else:
        print(f"❌ Erro ao salvar no Firebase: {res.status_code} - {res.text}")
        
except requests.RequestException as e:
    print(f"❌ Erro de conexão com Firebase: {e}")
except Exception as e:
    print(f"❌ Erro inesperado ao salvar: {e}")
