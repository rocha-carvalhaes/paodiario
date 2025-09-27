"""
Teste simples para verificar se o comando funciona.
"""
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_basic_functionality():
    """Testa funcionalidade básica sem dependências externas."""
    try:
        print("🔄 Testando funcionalidade básica...")
        
        # Testa imports
        from models.frase import Frase
        print("✅ Model Frase importado")
        
        # Testa criação de frase
        frase = Frase(texto="Teste de frase")
        print(f"✅ Frase criada: {frase.texto}")
        print(f"✅ Chave gerada: {frase.chave}")
        
        # Testa conversão para dict
        frase_dict = frase.to_dict()
        print(f"✅ Frase convertida para dict: {frase_dict}")
        
        # Testa criação a partir de dict
        frase_from_dict = Frase.from_dict(frase_dict)
        print(f"✅ Frase criada a partir de dict: {frase_from_dict.texto}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def main():
    """Função principal."""
    print("🧪 Teste básico de funcionalidade\n")
    
    if test_basic_functionality():
        print("\n🎉 Teste básico passou!")
        print("\n💡 Para usar o projeto completo:")
        print("   1. Crie um arquivo .env com suas credenciais")
        print("   2. Execute: python gerar_frase.py")
        print("   3. Ou execute: python src/app.py")
        return 0
    else:
        print("\n❌ Teste básico falhou!")
        return 1

if __name__ == "__main__":
    exit(main())
