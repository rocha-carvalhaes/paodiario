import requests

# BASE_URL = "http://127.0.0.1:5000/frases"
BASE_URL = "https://paodiario.onrender.com/frases"

params = {
    "ano": "2025",
    "mes": "07",
    "dia": "20"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    frase = response.json()["texto"]
    print("Frase do dia:", frase)
elif response.status_code == 500:
    print("Erro interno do servidor. Verifique os logs do Flask.")
else:
    print("Erro:", response.status_code)
    print("Mensagem:", response.json())
