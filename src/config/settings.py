"""
Configurações centralizadas da aplicação.
"""
import os
import json
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


class Config:
    """Configurações base da aplicação."""
    
    # Flask
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = FLASK_ENV == "development"
    
    # Firebase
    FIREBASE_URL = os.getenv("FIREBASE_URL")
    FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON")
    
    # APIs Externas
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    @classmethod
    def validate_config(cls):
        """Valida se todas as configurações necessárias estão definidas."""
        required_vars = [
            ("FIREBASE_URL", cls.FIREBASE_URL),
            ("FIREBASE_CREDENTIALS_JSON", cls.FIREBASE_CREDENTIALS_JSON),
            ("GEMINI_API_KEY", cls.GEMINI_API_KEY)
        ]
        
        missing_vars = []
        for var_name, var_value in required_vars:
            if not var_value:
                missing_vars.append(var_name)
        
        if missing_vars:
            print(f"⚠️ Aviso: Variáveis de ambiente não definidas: {', '.join(missing_vars)}")
            print("⚠️ Algumas funcionalidades podem não funcionar corretamente")
            # Não falha mais, apenas avisa
    
    @classmethod
    def get_firebase_credentials(cls):
        """Retorna as credenciais do Firebase como dicionário."""
        try:
            return json.loads(cls.FIREBASE_CREDENTIALS_JSON)
        except json.JSONDecodeError as e:
            raise ValueError(f"FIREBASE_CREDENTIALS_JSON contém JSON inválido: {e}")


class DevelopmentConfig(Config):
    """Configurações para desenvolvimento."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurações para produção."""
    DEBUG = False


# Configuração baseada no ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
