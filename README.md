# 🥖 Pão Diário

Uma plataforma inspiradora que gera reflexões motivacionais diárias usando inteligência artificial, baseadas em ensinamentos espirituais e mensagens do Vatican News.

## ✨ Funcionalidades

- 🤖 **Geração automática de reflexões** usando Google Gemini AI
- 📰 **Coleta inteligente** de mensagens do Vatican News como base
- 🔥 **Armazenamento seguro** no Firebase Realtime Database
- 🌐 **API REST** para consultar reflexões
- ⏰ **Automação diária** via GitHub Actions (gera reflexão às 3h UTC)
- 🎨 **Interface web elegante** para visualizar as reflexões

## 🏗️ Arquitetura

O projeto segue uma arquitetura limpa e modular:

```
src/
├── config/          # Configurações centralizadas
│   └── settings.py
├── models/          # Modelos de dados
│   └── frase.py
├── services/        # Lógica de negócio
│   ├── scraper_service.py    # Scraping do Vatican News
│   ├── ai_service.py         # Geração com IA
│   ├── firebase_service.py   # Interação com Firebase
│   └── frase_service.py      # Orquestração completa
├── api/            # Rotas e endpoints
│   └── routes.py
└── app.py          # Aplicação Flask principal
```

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd paodiario
```

### 2. Crie um ambiente virtual
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

**IMPORTANTE**: Você precisa criar um arquivo `.env` na raiz do projeto com suas credenciais reais.

Copie o conteúdo do arquivo `env.example` e crie um arquivo `.env`:

```bash
# No Windows (PowerShell)
Copy-Item env.example .env

# No Linux/Mac
cp env.example .env
```

**OU** crie manualmente o arquivo `.env` com o seguinte conteúdo:

```env
# Configurações do Firebase
FIREBASE_URL=https://seu-projeto.firebaseio.com
FIREBASE_CREDENTIALS_JSON={"type":"service_account","project_id":"..."}

# API do Google Gemini
GEMINI_API_KEY=sua_chave_do_gemini_aqui

# Configurações do Flask
FLASK_ENV=development
PORT=5000
```

### 5. Configure o Firebase

1. Crie um projeto no [Firebase Console](https://console.firebase.google.com/)
2. Ative o Realtime Database
3. Gere uma chave de serviço em "Configurações do projeto" > "Contas de serviço"
4. Copie o JSON da chave para `FIREBASE_CREDENTIALS_JSON`

### 6. Configure o Google Gemini

1. Acesse o [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma API key
3. Adicione a chave em `GEMINI_API_KEY`

## 🎯 Como Usar

### Gerar uma frase manualmente
```bash
python gerar_frase.py
```

### Executar a aplicação web
```bash
python src/app.py
```

A aplicação estará disponível em `http://localhost:5000`

### Endpoints da API

- `GET /frases?ano=2025&mes=01&dia=15` - Busca frase por data
- `GET /todas-frases` - Lista todas as frases
- `POST /frases` - Adiciona nova frase
- `POST /gerar-frase` - Gera frase automaticamente

## 🤖 Automação

O projeto inclui um workflow do GitHub Actions que:

- Executa diariamente às 3h UTC (0h BRT)
- Gera uma nova frase automaticamente
- Salva no Firebase

Para ativar, configure os secrets no GitHub:
- `GEMINI_API_KEY`
- `FIREBASE_URL`
- `FIREBASE_CREDENTIALS_JSON`

## 🛠️ Desenvolvimento

### Estrutura de Pastas
- `src/config/` - Configurações e settings
- `src/models/` - Modelos de dados
- `src/services/` - Lógica de negócio
- `src/api/` - Rotas e endpoints
- `static/` - Arquivos estáticos (CSS, JS)
- `templates/` - Templates HTML
- `data/` - Dados locais

### Adicionando Novos Serviços

1. Crie o arquivo em `src/services/`
2. Implemente a classe com métodos específicos
3. Importe no `FraseService` se necessário
4. Adicione testes se aplicável

### Exemplo de Uso dos Serviços

```python
from src.services.frase_service import FraseService

# Gerar frase completa
frase_service = FraseService()
frase = frase_service.gerar_frase_do_dia()

# Buscar frase específica
frase = frase_service.buscar_frase_por_data("2025", "01", "15")

# Listar todas as frases
todas_frases = frase_service.listar_todas_frases()
```

## 🔧 Troubleshooting

### Erro: "Variáveis de ambiente não definidas"
- Verifique se o arquivo `.env` existe e está configurado
- Confirme se as variáveis estão com os nomes corretos

### Erro: "ModuleNotFoundError"
- Ative o ambiente virtual: `env\Scripts\activate`
- Instale as dependências: `pip install -r requirements.txt`

### Erro: "Firebase credentials inválidas"
- Verifique se o JSON das credenciais está correto
- Confirme se a URL do Firebase está correta

### Erro: "Gemini API key inválida"
- Verifique se a chave da API está correta
- Confirme se a API está ativa no Google AI Studio

## 📝 Logs

O sistema gera logs informativos para debug:
- ✅ Sucesso nas operações
- ❌ Erros com detalhes
- 🔄 Status das operações

## 🚀 Deploy no Render

O projeto está configurado para deploy automático no Render:

### 1. Conecte seu repositório
- Acesse [Render Dashboard](https://dashboard.render.com/)
- Conecte seu repositório GitHub

### 2. Configure as variáveis de ambiente
No painel do Render, adicione as seguintes variáveis:
- `FIREBASE_URL` - URL do seu projeto Firebase
- `FIREBASE_CREDENTIALS_JSON` - JSON das credenciais do Firebase
- `GEMINI_API_KEY` - Chave da API do Google Gemini

### 3. Deploy automático
- O Render usará o arquivo `render.yaml` para configuração
- Build Command: `pip install -r requirements.txt`
- Start Command: `python src/app.py`

### 4. Verificação
Após o deploy, acesse a URL fornecida pelo Render para verificar se está funcionando.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🙏 Agradecimentos

- [Vatican News](https://www.vaticannews.va/) pelas mensagens inspiradoras
- [Google Gemini](https://ai.google.dev/) pela IA generativa
- [Firebase](https://firebase.google.com/) pelo banco de dados
- [Flask](https://flask.palletsprojects.com/) pelo framework web

---

**Desenvolvido com ❤️ para espalhar mensagens positivas e motivacionais!**
