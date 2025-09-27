"""
Serviço responsável por interagir com o Firebase.
"""
import requests
from typing import Dict, Any, Optional
from config.settings import Config
from models.frase import Frase


class FirebaseService:
    """Serviço para interagir com o Firebase Realtime Database."""
    
    def __init__(self):
        self.base_url = Config.FIREBASE_URL.rstrip('/')
        self.session = requests.Session()
    
    def salvar_frase(self, frase: Frase) -> bool:
        """
        Salva uma frase no Firebase.
        
        Args:
            frase (Frase): Instância da frase a ser salva.
            
        Returns:
            bool: True se salvou com sucesso, False caso contrário.
        """
        try:
            url = f"{self.base_url}/frases/{frase.chave}.json"
            payload = frase.to_dict()
            
            response = self.session.put(url, json=payload, timeout=10)
            
            if response.ok:
                print(f"✅ Frase salva com sucesso no Firebase: {frase.texto}")
                print(f"📅 Chave: {frase.chave}")
                return True
            else:
                print(f"❌ Erro ao salvar no Firebase: {response.status_code} - {response.text}")
                return False
                
        except requests.RequestException as e:
            print(f"❌ Erro de conexão com Firebase: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado ao salvar: {e}")
            return False
    
    def buscar_frase(self, ano: str, mes: str, dia: str) -> Optional[Dict[str, Any]]:
        """
        Busca uma frase específica por data.
        
        Args:
            ano (str): Ano da frase.
            mes (str): Mês da frase.
            dia (str): Dia da frase.
            
        Returns:
            Optional[Dict[str, Any]]: Dados da frase ou None se não encontrada.
        """
        try:
            url = f"{self.base_url}/frases.json"
            response = self.session.get(url, timeout=10)
            
            if not response.ok:
                print(f"❌ Erro ao buscar frases: {response.status_code}")
                return None
            
            frases = response.json() or {}
            
            # Busca por ano, mês e dia
            for key, frase_data in frases.items():
                if (frase_data.get("ano") == ano and 
                    frase_data.get("mes") == mes and 
                    frase_data.get("dia") == dia):
                    return frase_data
            
            return None
            
        except requests.RequestException as e:
            print(f"❌ Erro de conexão ao buscar frase: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado ao buscar frase: {e}")
            return None
    
    def listar_todas_frases(self) -> Dict[str, Any]:
        """
        Lista todas as frases do Firebase.
        
        Returns:
            Dict[str, Any]: Dicionário com todas as frases.
        """
        try:
            url = f"{self.base_url}/frases.json"
            response = self.session.get(url, timeout=10)
            
            if response.ok:
                return response.json() or {}
            else:
                print(f"❌ Erro ao listar frases: {response.status_code}")
                return {}
                
        except requests.RequestException as e:
            print(f"❌ Erro de conexão ao listar frases: {e}")
            return {}
        except Exception as e:
            print(f"❌ Erro inesperado ao listar frases: {e}")
            return {}
