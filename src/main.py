import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/data.csv')

profile = ProfileReport(df, title="Análise Exploratória de Dados", explorative=True)	
profile.to_file("eda.html")

# 🔹 1. Conversão para string (identificadores, códigos)
# Quando usar: colunas com números que representam IDs, CNPJs, códigos.
# df["COLUNA"] = df["COLUNA"].astype(str)

# 🔹 2. Conversão para datetime (datas, timestamps)
# Quando usar: colunas com datas no formato string (ex: yyyy-mm-dd, dd/mm/yyyy etc).
# df["COLUNA"] = pd.to_datetime(df["COLUNA"], errors="coerce")

# 🔹 3. Remover espaços em branco extras
# Quando usar: textos com espaços no início/fim (ex: nomes, cidades, categorias).
# df["COLUNA"] = df["COLUNA"].astype(str).str.strip()

# 🔹 4. Texto para maiúsculas/minúsculas (normalização)
# Quando usar: padronizar textos categóricos (ex: sexo, uf, tipo).
# df["COLUNA"] = df["COLUNA"].str.upper()
# df["COLUNA"] = df["COLUNA"].str.lower()

# 🔹 5. Preenchimento de valores ausentes com string
# Quando usar: substituir NaNs em colunas de texto.
# df["COLUNA"] = df["COLUNA"].fillna("DESCONHECIDO")

# 🔹 6. Preenchimento de valores ausentes com datas
# Quando usar: preencher datas faltantes com uma data padrão.
# df["COLUNA"] = df["COLUNA"].fillna(pd.Timestamp("1900-01-01"))

# 🔹 7. Conversão para booleano (sim/não, ativo/inativo)
# Quando usar: colunas com valores como "Sim", "Não", "sim", "nao", etc.
# df["COLUNA"] = df["COLUNA"].str.strip().str.upper().map({"SIM": True, "NÃO": False, "NAO": False})

# 🔹 8. Mapeamento de categorias padronizadas
# Quando usar: padronizar valores como sexo, estado civil, tipo etc.
# mapa = {"M": "Masculino", "F": "Feminino", "O": "Outro"}
# df["COLUNA"] = df["COLUNA"].map(mapa).fillna("Desconhecido")

# 🔹 9. Cálculo de idade (a partir de data de nascimento)
# Quando usar: para análises de faixa etária ou perfis demográficos.
# df["IDADE"] = (pd.Timestamp.today() - df["COLUNA"]).dt.days // 365

# 🔹 10. Marcar idosos com base na idade
# Quando usar: segmentar população com 60+ anos.
# df["IDOSO"] = df["IDADE"].apply(lambda x: "SIM" if pd.notna(x) and x >= 60 else "NÃO")

# 🔹 11. Extração de ano, mês e dia a partir de uma data
# Quando usar: análises sazonais, agregações temporais.
# df["COLUNA_ANO"] = df["COLUNA"].dt.year
# df["COLUNA_MES"] = df["COLUNA"].dt.month
# df["COLUNA_DIA"] = df["COLUNA"].dt.day

# 🔹 12. Remover acentos (normalização avançada de texto)
# Quando usar: padronizar textos para comparações ou agrupamentos.
# import unicodedata
# df["COLUNA"] = df["COLUNA"].apply(lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', errors='ignore').decode('utf-8'))

# 🔹 13. Criar coluna condicional binária (ex: idade >= 18)
# Quando usar: criar flags como "é adulto", "é idoso", "é menor de idade".
# df["ADULTO"] = df["IDADE"].apply(lambda x: "SIM" if pd.notna(x) and x >= 18 else "NÃO")
