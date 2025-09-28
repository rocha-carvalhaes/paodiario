#!/usr/bin/env python3
"""
Teste simples do Firebase.
"""
import sys
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente PRIMEIRO
load_dotenv()

print("🔍 Teste Simples do Firebase", flush=True)

# Debug: verifica se as variáveis foram carregadas
gemini_key = os.getenv('GEMINI_API_KEY')
firebase_creds = os.getenv('FIREBASE_CREDENTIALS_JSON')
firebase_url = os.getenv('FIREBASE_URL')

print(f"🔑 GEMINI_API_KEY: {'***' if gemini_key else 'NÃO DEFINIDA'}", flush=True)
print(f"🔑 FIREBASE_CREDENTIALS_JSON: {'***' if firebase_creds else 'NÃO DEFINIDA'}", flush=True)
print(f"🔑 FIREBASE_URL: {firebase_url or 'NÃO DEFINIDA'}", flush=True)

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    print("📦 Importando FirebaseService...", flush=True)
    from services.firebase_service import FirebaseService
    print("✅ FirebaseService importado", flush=True)
    
    print("🏗️ Criando instância...", flush=True)
    firebase_service = FirebaseService()
    print("✅ Instância criada", flush=True)
    
    print("🎉 Teste concluído com sucesso!", flush=True)
    
except Exception as e:
    print(f"❌ Erro: {e}", flush=True)
    import traceback
    traceback.print_exc()
