"""
Serviço principal para gerenciar frases do dia.
"""
from services.scraper_service import ScraperService
from services.ai_service import AIService
from services.firebase_service import FirebaseService
from models.frase import Frase


class FraseService:
    """Serviço principal para gerenciar o ciclo completo de geração de frases."""
    
    def __init__(self):
        self.scraper = ScraperService()
        self.ai = AIService()
        self.firebase = FirebaseService()
    
    def gerar_frase_do_dia(self) -> Frase:
        """
        Gera uma nova frase do dia seguindo todo o processo:
        1. Coleta mensagem base do Vatican News
        2. Gera frase usando IA
        3. Salva no Firebase
        
        Returns:
            Frase: Instância da frase gerada.
        """
        # 1. Coleta mensagem base
        print("🔄 Coletando mensagem base...")
        mensagem_base = self.scraper.coletar_mensagem()
        print(f"✅ Mensagem coletada: {mensagem_base[:50]}...")
        
        # 2. Gera frase usando IA
        print("🤖 Gerando frase com IA...")
        texto_frase = self.ai.gerar_frase(mensagem_base)
        print(f"✅ Frase gerada: {texto_frase[:50]}...")
        
        # 3. Cria objeto Frase
        frase = Frase(texto=texto_frase)
        
        # 4. Salva no Firebase
        print("💾 Salvando no Firebase...")
        sucesso = self.firebase.salvar_frase(frase)
        
        if sucesso:
            print("🎉 Frase do dia gerada com sucesso!")
        else:
            print("⚠️ Frase gerada mas não foi possível salvar no Firebase")
        
        return frase
    
    def gerar_frase_para_data(self, ano: str, mes: str, dia: str) -> Frase:
        """
        Gera uma frase do dia para uma data específica (útil para preencher datas retroativas).
        1. Coleta mensagem base do Vatican News
        2. Gera frase usando IA
        3. Salva no Firebase com a data informada
        
        Args:
            ano: Ano (ex: "2026")
            mes: Mês com 2 dígitos (ex: "01")
            dia: Dia com 2 dígitos (ex: "29")
        
        Returns:
            Frase: Instância da frase gerada.
        """
        # 1. Coleta mensagem base
        print(f"🔄 Coletando mensagem base para {ano}-{mes}-{dia}...")
        mensagem_base = self.scraper.coletar_mensagem()
        print(f"✅ Mensagem coletada: {mensagem_base[:50]}...")
        
        # 2. Gera frase usando IA
        print("🤖 Gerando frase com IA...")
        texto_frase = self.ai.gerar_frase(mensagem_base)
        print(f"✅ Frase gerada: {texto_frase[:50]}...")
        
        # 3. Cria objeto Frase com a data informada
        frase = Frase(texto=texto_frase, ano=ano, mes=mes, dia=dia)
        
        # 4. Salva no Firebase
        print("💾 Salvando no Firebase...")
        sucesso = self.firebase.salvar_frase(frase)
        
        if sucesso:
            print(f"🎉 Frase do dia {ano}-{mes}-{dia} gerada com sucesso!")
        else:
            print(f"⚠️ Frase gerada mas não foi possível salvar no Firebase para {ano}-{mes}-{dia}")
        
        return frase
    
    def buscar_frase_por_data(self, ano: str, mes: str, dia: str) -> Frase:
        """
        Busca uma frase específica por data.
        
        Args:
            ano (str): Ano da frase.
            mes (str): Mês da frase.
            dia (str): Dia da frase.
            
        Returns:
            Frase: Instância da frase encontrada.
            
        Raises:
            ValueError: Se a frase não for encontrada.
        """
        dados = self.firebase.buscar_frase(ano, mes, dia)
        
        if not dados:
            raise ValueError(f"Frase não encontrada para {ano}-{mes}-{dia}")
        
        return Frase.from_dict(dados)
    
    def listar_todas_frases(self) -> dict:
        """
        Lista todas as frases disponíveis.
        
        Returns:
            dict: Dicionário com todas as frases.
        """
        return self.firebase.listar_todas_frases()
