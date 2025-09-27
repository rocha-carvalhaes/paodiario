"""
Teste para verificar se o app pode ser importado sem erros.
"""
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_app_import():
    """Testa se o app pode ser importado."""
    try:
        print("🔄 Testando importação do app...")
        
        # Simula variáveis de ambiente para teste
        os.environ["FIREBASE_URL"] = "https://test.firebaseio.com"
        os.environ["FIREBASE_CREDENTIALS_JSON"] = '{"type":"service_account","project_id":"test"}'
        os.environ["GEMINI_API_KEY"] = "test_key"
        
        # Tenta importar o app
        from app import app
        print("✅ App importado com sucesso")
        
        # Testa se o app foi criado
        if app:
            print("✅ App criado com sucesso")
            return True
        else:
            print("❌ App não foi criado")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao importar app: {e}")
        return False

def main():
    """Função principal."""
    print("🧪 Teste de importação do app\n")
    
    if test_app_import():
        print("\n🎉 App pode ser importado sem erros!")
        print("💡 O problema no Render deve estar resolvido.")
    else:
        print("\n❌ Ainda há problemas com o app.")
    
    return 0

if __name__ == "__main__":
    exit(main())
