import pandas as pd
import os

# Pasta com os CSVs sujos
PASTA_CSV = "./"
PASTA_SAIDA = "./arquivos_limpos/"

os.makedirs(PASTA_SAIDA, exist_ok=True)

# Lista arquivos CSV da pasta
for arquivo in os.listdir(PASTA_CSV):
    if arquivo.endswith(".csv"):
        print(f"🔄 Limpando: {arquivo}")
        df = pd.read_csv(os.path.join(PASTA_CSV, arquivo))

        # Remover espaços dos nomes das colunas
        df.columns = df.columns.str.strip()

        # Remover espaços dos valores
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Remover colunas completamente vazias ou com só espaços
        df = df.dropna(axis=1, how="all")
        df = df.loc[:, ~(df.apply(lambda col: col.astype(str).str.strip().eq('').all()))]

        # Salvar arquivo limpo
        novo_nome = f"{os.path.splitext(arquivo)[0]}_limpo.csv"
        df.to_csv(os.path.join(PASTA_SAIDA, novo_nome), index=False)
        print(f"✅ Salvo: {novo_nome}")
