"""
Script TEMPORÁRIO para gerar frases do dia em datas que ficaram faltando
(workflow parado entre 2026-01-29 e 2026-02-24).

Uso: python gerar_frases_retroativas.py

Depois de rodar com sucesso, este script pode ser removido ou mantido para referência.
"""
import sys
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.frase_service import FraseService


# Datas que ficaram sem frase (inclusive início e fim)
DATA_INICIO = datetime(2026, 1, 29)
DATA_FIM = datetime(2026, 2, 24)


def listar_datas_faltantes():
    """Gera a lista de datas entre DATA_INICIO e DATA_FIM (inclusive)."""
    datas = []
    d = DATA_INICIO
    while d <= DATA_FIM:
        datas.append(d)
        d += timedelta(days=1)
    return datas


def main():
    datas = listar_datas_faltantes()
    print(f"📅 Total de datas a preencher: {len(datas)}")
    print(f"   De {DATA_INICIO.date()} a {DATA_FIM.date()}")
    print()

    frase_service = FraseService()
    erros = []
    sucesso = 0

    for i, dt in enumerate(datas, 1):
        ano = str(dt.year)
        mes = f"{dt.month:02d}"
        dia = f"{dt.day:02d}"

        # Opcional: verificar se já existe frase para essa data (evitar duplicar)
        try:
            existing = frase_service.firebase.buscar_frase(ano, mes, dia)
            if existing:
                print(f"[{i}/{len(datas)}] ⏭️  {ano}-{mes}-{dia} já existe no Firebase, pulando.")
                sucesso += 1
                continue
        except Exception as e:
            print(f"[{i}/{len(datas)}] ⚠️  Não foi possível verificar {ano}-{mes}-{dia}: {e}")

        print(f"[{i}/{len(datas)}] 🥖 Gerando frase para {ano}-{mes}-{dia}...")
        try:
            frase_service.gerar_frase_para_data(ano, mes, dia)
            sucesso += 1
        except Exception as e:
            print(f"❌ Erro em {ano}-{mes}-{dia}: {e}")
            erros.append((ano, mes, dia, str(e)))

        print()

    print("=" * 50)
    print(f"✅ Concluído: {sucesso}/{len(datas)} frases processadas.")
    if erros:
        print(f"❌ Erros ({len(erros)}):")
        for ano, mes, dia, msg in erros:
            print(f"   - {ano}-{mes}-{dia}: {msg}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
