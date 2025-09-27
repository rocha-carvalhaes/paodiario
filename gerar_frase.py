"""
Script para gerar frase do dia.
Pode ser executado manualmente ou via cron job.
"""
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.frase_service import FraseService


def main():
    """Função principal para gerar frase do dia."""
    try:
        print("🥖 Iniciando geração da frase do dia...")
        
        frase_service = FraseService()
        frase = frase_service.gerar_frase_do_dia()
        
        print(f"✅ Frase gerada com sucesso!")
        print(f"📝 Texto: {frase.texto}")
        print(f"📅 Data: {frase.ano}-{frase.mes}-{frase.dia}")
        print(f"🔑 Chave: {frase.chave}")
        
    except Exception as e:
        print(f"❌ Erro ao gerar frase: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
