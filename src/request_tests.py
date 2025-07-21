import requests

# BASE_URL = "http://127.0.0.1:5000/todas-frases"
BASE_URL = "https://paodiario.onrender.com/frases"

params = {
    "ano": "2025",
    "mes": "07",
    "dia": "20"
}

response = requests.get(BASE_URL)

if response.status_code == 200:
    frases = response.json()
    print("Frases recebidas:", frases)
    # for ano in frases:
    #     for mes in frases[ano]:
    #         for dia in frases[ano][mes]:
    #             print(f"{dia}/{mes}/{ano}: {frases[int(ano)][int(mes)][int(dia)]}")
else:
    print("Erro:", response.status_code, response.text)