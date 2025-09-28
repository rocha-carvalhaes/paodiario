"""
Serviço responsável por interagir com o Firebase.
"""
import requests
from typing import Dict, Any, Optional
from config.settings import Config
from models.frase import Frase
import firebase_admin
from firebase_admin import db as realtime_db


class FirebaseService:
    """Serviço para interagir com o Firebase Realtime Database."""
    
    def __init__(self):
        self.base_url = Config.FIREBASE_URL.rstrip('/')
        self.session = requests.Session()
        
        # Verifica se o Firebase já foi inicializado
        try:
            # Tenta acessar o app padrão
            firebase_admin.get_app()
        except ValueError:
            # Se não existe, inicializa
            try:
                cred_dict = Config.get_firebase_credentials()
                cred = firebase_admin.credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': Config.FIREBASE_URL
                })
            except Exception as e:
                print(f"⚠️ Aviso: Firebase não configurado: {e}")
                print("⚠️ Operações de escrita podem falhar")
    
    def salvar_frase(self, frase: Frase) -> bool:
        """
        Salva uma frase no Firebase usando o SDK oficial.
        
        Args:
            frase (Frase): Instância da frase a ser salva.
            
        Returns:
            bool: True se salvou com sucesso, False caso contrário.
        """
        try:
            # Usa o SDK oficial do Firebase (autenticado via service account)
            ref = realtime_db.reference(f'/frases/{frase.chave}')
            ref.set(frase.to_dict())
            
            print(f"✅ Frase salva com sucesso no Firebase: {frase.texto}")
            print(f"📅 Chave: {frase.chave}")
            return True
                
        except Exception as e:
            print(f"❌ Erro ao salvar no Firebase: {e}")
            return False
    
    def buscar_frase(self, ano: str, mes: str, dia: str) -> Optional[Dict[str, Any]]:
        """
        Busca uma frase específica por data usando o SDK oficial.
        
        Args:
            ano (str): Ano da frase.
            mes (str): Mês da frase.
            dia (str): Dia da frase.
            
        Returns:
            Optional[Dict[str, Any]]: Dados da frase ou None se não encontrada.
        """
        try:
            # Usa o SDK oficial do Firebase
            ref = realtime_db.reference('/frases')
            frases = ref.get()
            
            if not frases:
                return None
            
            # Busca por ano, mês e dia
            for key, frase_data in frases.items():
                if (frase_data.get("ano") == ano and 
                    frase_data.get("mes") == mes and 
                    frase_data.get("dia") == dia):
                    return frase_data
            
            return None
            
        except Exception as e:
            print(f"❌ Erro ao buscar frase: {e}")
            return None
    
    def listar_todas_frases(self) -> Dict[str, Any]:
        """
        Lista todas as frases do Firebase usando o SDK oficial.
        
        Returns:
            Dict[str, Any]: Dicionário com todas as frases.
        """
        try:
            # Usa o SDK oficial do Firebase
            ref = realtime_db.reference('/frases')
            frases = ref.get()
            
            return frases or {}
                
        except Exception as e:
            print(f"❌ Erro ao listar frases: {e}")
            return {}
