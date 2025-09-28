"""
Serviço responsável por gerar frases usando IA.
"""
import google.generativeai as genai
from typing import Optional
from config.settings import Config


class AIService:
    """Serviço para gerar frases usando Google Gemini."""
    
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")
        self._fallback_frase = (
            "🌅 Que este novo dia traga paz, amor e muitas bênçãos! "
            "Bom dia! (Salmos 118:24)"
        )
    
    def gerar_frase(self, mensagem_base: str) -> str:
        """
        Gera uma frase motivacional baseada na mensagem fornecida.
        
        Args:
            mensagem_base (str): Mensagem base para gerar a frase.
            
        Returns:
            str: Frase gerada ou frase de fallback em caso de erro.
        """
        prompt = self._criar_prompt(mensagem_base)
        
        try:
            print("🔄 Enviando prompt para o Gemini...")
            response = self.model.generate_content(prompt)
            
            if not response.text:
                raise ValueError("Resposta vazia do modelo Gemini")
            
            frase = response.text.strip().replace("\n", "")
            print(f"✅ Resposta recebida do Gemini: {len(frase)} caracteres")
            return frase
            
        except Exception as e:
            print(f"❌ Erro ao gerar frase: {e}")
            print("🔄 Usando frase de fallback...")
            return self._frase_fallback()
    
    def _criar_prompt(self, mensagem_base: str) -> str:
        """Cria o prompt para o modelo de IA."""
        return f"""
        Gere uma mensagem de bom dia no estilo de uma "tia do zap".
        A mensagem deve começar com uma frase inicial curta e significativa, em torno de 6 palavras, que traga impacto e sentido.
        Em seguida, desenvolva o ensinamento do dia de forma motivacional, amorosa e ecumênica, inspirado no texto a seguir mas em tom ecumênico:
        {mensagem_base}
        Inclua emojis para transmitir carinho e leveza.
        Termine sempre com "Bom dia!" seguido da referência bíblica no formato (Livro por extenso, capítulo, versículo).
        Use no máximo 300 caracteres.
        """
    
    def _frase_fallback(self) -> str:
        """Retorna frase de fallback em caso de erro."""
        return self._fallback_frase
