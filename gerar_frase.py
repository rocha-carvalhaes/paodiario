"""
Script para gerar frase do dia.
Pode ser executado manualmente ou via cron job.
"""
import sys
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente PRIMEIRO
load_dotenv()

# Debug: verifica se as variáveis foram carregadas
print("🔍 Verificando variáveis de ambiente...", flush=True)
gemini_key = os.getenv('GEMINI_API_KEY')
firebase_creds = os.getenv('FIREBASE_CREDENTIALS_JSON')
firebase_url = os.getenv('FIREBASE_URL')

print(f"🔑 GEMINI_API_KEY: {'***' if gemini_key else 'NÃO DEFINIDA'}", flush=True)
print(f"🔑 FIREBASE_CREDENTIALS_JSON: {'***' if firebase_creds else 'NÃO DEFINIDA'}", flush=True)
print(f"🔑 FIREBASE_URL: {firebase_url or 'NÃO DEFINIDA'}", flush=True)

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.frase_service import FraseService


def main():
    """Função principal para gerar frase do dia."""
    import sys
    
    try:
        print("🥖 Iniciando geração da frase do dia...", flush=True)
        sys.stdout.flush()
        
        frase_service = FraseService()
        frase = frase_service.gerar_frase_do_dia()
        
        print(f"✅ Frase gerada com sucesso!", flush=True)
        print(f"📝 Texto: {frase.texto}", flush=True)
        print(f"📅 Data: {frase.ano}-{frase.mes}-{frase.dia}", flush=True)
        print(f"🔑 Chave: {frase.chave}", flush=True)
        sys.stdout.flush()
        
    except Exception as e:
        print(f"❌ Erro ao gerar frase: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
