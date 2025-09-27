"""
Modelo de dados para frases.
"""
from datetime import datetime
from typing import Optional, Dict, Any


class Frase:
    """Modelo que representa uma frase do dia."""
    
    def __init__(self, texto: str, ano: Optional[str] = None, 
                 mes: Optional[str] = None, dia: Optional[str] = None):
        self.texto = texto
        self.ano = ano or str(datetime.now().year)
        self.mes = mes or f"{datetime.now().month:02d}"
        self.dia = dia or f"{datetime.now().day:02d}"
        self._timestamp = datetime.now()
    
    @property
    def chave(self) -> str:
        """Gera chave única para o Firebase baseada na data e hora."""
        horaminuto = f"{self._timestamp.hour:02d}{self._timestamp.minute:02d}"
        return f"{self.ano}{self.mes}{self.dia}-{horaminuto}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte a frase para dicionário (formato Firebase)."""
        return {
            "ano": self.ano,
            "mes": self.mes,
            "dia": self.dia,
            "texto": self.texto
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Frase':
        """Cria uma instância de Frase a partir de um dicionário."""
        return cls(
            texto=data["texto"],
            ano=data.get("ano"),
            mes=data.get("mes"),
            dia=data.get("dia")
        )
    
    def __str__(self) -> str:
        return f"Frase({self.ano}-{self.mes}-{self.dia}): {self.texto[:50]}..."
    
    def __repr__(self) -> str:
        return self.__str__()
