"""
Script para testar se a configuração está correta.
Execute este script para verificar se tudo está funcionando.
"""
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Testa se todos os imports estão funcionando."""
    try:
        print("🔄 Testando imports...")
        
        from config.settings import Config
        print("✅ Config importado com sucesso")
        
        from models.frase import Frase
        print("✅ Model Frase importado com sucesso")
        
        from services.scraper_service import ScraperService
        print("✅ ScraperService importado com sucesso")
        
        from services.ai_service import AIService
        print("✅ AIService importado com sucesso")
        
        from services.firebase_service import FirebaseService
        print("✅ FirebaseService importado com sucesso")
        
        from services.frase_service import FraseService
        print("✅ FraseService importado com sucesso")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro de import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def test_config():
    """Testa se as configurações estão definidas."""
    try:
        print("\n🔄 Testando configurações...")
        
        from config.settings import Config
        
        # Verifica se as variáveis estão definidas
        if not Config.FIREBASE_URL:
            print("⚠️ FIREBASE_URL não está definida")
            return False
        else:
            print("✅ FIREBASE_URL configurada")
        
        if not Config.FIREBASE_CREDENTIALS_JSON:
            print("⚠️ FIREBASE_CREDENTIALS_JSON não está definida")
            return False
        else:
            print("✅ FIREBASE_CREDENTIALS_JSON configurada")
        
        if not Config.GEMINI_API_KEY:
            print("⚠️ GEMINI_API_KEY não está definida")
            return False
        else:
            print("✅ GEMINI_API_KEY configurada")
        
        # Testa validação das credenciais
        try:
            Config.get_firebase_credentials()
            print("✅ Credenciais do Firebase são válidas")
        except Exception as e:
            print(f"❌ Credenciais do Firebase inválidas: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar configurações: {e}")
        return False

def test_services():
    """Testa se os serviços podem ser instanciados."""
    try:
        print("\n🔄 Testando serviços...")
        
        from services.scraper_service import ScraperService
        from services.ai_service import AIService
        from services.firebase_service import FirebaseService
        from services.frase_service import FraseService
        
        scraper = ScraperService()
        print("✅ ScraperService instanciado")
        
        ai = AIService()
        print("✅ AIService instanciado")
        
        firebase = FirebaseService()
        print("✅ FirebaseService instanciado")
        
        frase_service = FraseService()
        print("✅ FraseService instanciado")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar serviços: {e}")
        return False

def main():
    """Função principal de teste."""
    print("🧪 Iniciando testes de configuração...\n")
    
    tests = [
        ("Imports", test_imports),
        ("Configurações", test_config),
        ("Serviços", test_services)
    ]
    
    results = []
    for test_name, test_func in tests:
        result = test_func()
        results.append((test_name, result))
    
    print("\n📊 Resultados dos testes:")
    print("=" * 40)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 40)
    
    if all_passed:
        print("🎉 Todos os testes passaram! O projeto está configurado corretamente.")
        print("\n💡 Agora você pode executar:")
        print("   python gerar_frase.py  # Para gerar uma frase")
        print("   python src/app.py      # Para executar a aplicação web")
    else:
        print("⚠️ Alguns testes falharam. Verifique a configuração.")
        print("\n💡 Dicas:")
        print("   1. Verifique se o arquivo .env existe e está configurado")
        print("   2. Confirme se todas as dependências estão instaladas")
        print("   3. Verifique se as credenciais estão corretas")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
