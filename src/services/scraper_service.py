"""
Serviço responsável por fazer scraping de mensagens.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Optional


class ScraperService:
    """Serviço para fazer scraping de mensagens do Vatican News."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self._fallback_message = (
            "Que este dia seja abençoado com paz, amor e sabedoria. "
            "Que possamos encontrar força em nossa fé e esperança em cada novo amanhecer."
        )
    
    def coletar_mensagem(self) -> str:
        """
        Coleta a mensagem do dia do site Vatican News.
        
        Returns:
            str: Mensagem coletada ou mensagem de fallback em caso de erro.
        """
        data = datetime.now().strftime("%Y/%m/%d")
        url = f"https://www.vaticannews.va/pt/palavra-do-dia/{data}.html"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            div_conteudo = soup.find('div', class_='section__content')
            
            if not div_conteudo:
                raise ValueError("Div de conteúdo não encontrada na página")
            
            paragrafos = div_conteudo.find_all('p')
            textos = [p.get_text().strip() for p in paragrafos if p.get_text().strip()]
            mensagem = " ".join(textos)
            
            if not mensagem:
                raise ValueError("Nenhuma mensagem encontrada na página")
            
            return mensagem
            
        except requests.RequestException as e:
            print(f"Erro na requisição HTTP: {e}")
            return self._mensagem_fallback()
        except Exception as e:
            print(f"Erro ao processar a página: {e}")
            return self._mensagem_fallback()
    
    def _mensagem_fallback(self) -> str:
        """Retorna mensagem de fallback em caso de erro."""
        return self._fallback_message
