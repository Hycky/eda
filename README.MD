# 🧠 Guia de Análise Exploratória com YData Profiling

Este guia ensina como:

- Instalar o YData Profiling (ex-pandas-profiling)
- Ativar ambientes virtuais com **Poetry** ou **venv**
- Rodar o `ProfileReport`
- Aplicar transformações comuns em colunas para melhorar a análise

---

## 💡 Pré requisitos:

### 🐍 Python 3.11 ou superior

**se usa pyenv, basta o comando:**

#### Caso não tenha o python 3.11 instalado no seu pyenv

```bash
pyenv install 3.11.8
```

#### caso ja possua o python 3.11

```bash
pyenv local 3.11.8
```

**Se não usa pyenv deve baixar a versão correspondente na web, porém recomendo fortemente o usao de pyenv**

#### Windows:

https://github.com/pyenv-win/pyenv-win

#### Mac/Linux:

https://github.com/pyenv/pyenv

## ✅ Instalação

### 🔹 Usando `venv`

**1. Criar ambiente virtual:**

#### Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**2. Instalar dependências via `requirements.txt`:**

```bash
pip install -r requirements.txt
```

---

### 🔹 Usando `poetry`

**1. Criar projeto e instalar dependências:**

```bash
poetry install
```

**2. Ativar o ambiente virtual:**

```bash
poetry shell
```

---

## 🚧 Edição e adaptação

Na pasta `data`, coloque seu arquivo CSV obrigatoriamente com o nome `"data.csv"` e remova o arquivo de exemplo `"data_example.csv"`:

![alt text](image.png)

## 🔧 Como ajustar colunas no seu DataFrame

No arquivo `main.py`, você encontrará **13 transformações possíveis** que podem ser ativadas conforme a necessidade do seu conjunto de dados.

Para utilizá-las:

1. Copie a transformação desejada.
2. Remova o `#` do início da linha.
3. Substitua `"COLUNA"` pelo nome real da coluna que deseja modificar.

---

### 🧪 Exemplo

Suponha que seu `DataFrame` possua uma coluna chamada `"CPF"` contendo números com 11 dígitos.

Por padrão, o YData Profiling pode interpretar essa coluna como **numérica** e tentar calcular soma, média etc.  
Porém, ela é uma informação **categórica** e deve ser convertida para `string`.

---

### ✅ Ajuste sugerido no `main.py`:

```python
# 🔹 1. Conversão para string (identificadores, códigos)
# Quando usar: colunas com números que representam IDs, CNPJs, códigos.
df["CPF"] = df["CPF"].astype(str)
```

---

## 🚀 Como rodar o YData Profiling

```bash
python src/main.py
```

---

## 🛠️ Transformações recomendadas por tipo de coluna

```python
# 🔹 1. Conversão para string (identificadores, códigos)
df["COLUNA"] = df["COLUNA"].astype(str)

# 🔹 2. Conversão para datetime (datas, timestamps)
df["COLUNA"] = pd.to_datetime(df["COLUNA"], errors="coerce")

# 🔹 3. Remover espaços em branco extras
df["COLUNA"] = df["COLUNA"].astype(str).str.strip()

# 🔹 4. Texto para maiúsculas/minúsculas (normalização)
df["COLUNA"] = df["COLUNA"].str.upper()
df["COLUNA"] = df["COLUNA"].str.lower()

# 🔹 5. Preenchimento de valores ausentes com string
df["COLUNA"] = df["COLUNA"].fillna("DESCONHECIDO")

# 🔹 6. Preenchimento de valores ausentes com datas
df["COLUNA"] = df["COLUNA"].fillna(pd.Timestamp("1900-01-01"))

# 🔹 7. Conversão para booleano (sim/não, ativo/inativo)
df["COLUNA"] = df["COLUNA"].str.strip().str.upper().map({"SIM": True, "NÃO": False, "NAO": False})

# 🔹 8. Mapeamento de categorias padronizadas
mapa = {"M": "Masculino", "F": "Feminino", "O": "Outro"}
df["COLUNA"] = df["COLUNA"].map(mapa).fillna("Desconhecido")

# 🔹 9. Cálculo de idade (a partir de data de nascimento)
df["IDADE"] = (pd.Timestamp.today() - df["COLUNA"]).dt.days // 365

# 🔹 10. Marcar idosos com base na idade
df["IDOSO"] = df["IDADE"].apply(lambda x: "SIM" if pd.notna(x) and x >= 60 else "NÃO")

# 🔹 11. Extração de ano, mês e dia a partir de uma data
df["COLUNA_ANO"] = df["COLUNA"].dt.year
df["COLUNA_MES"] = df["COLUNA"].dt.month
df["COLUNA_DIA"] = df["COLUNA"].dt.day

# 🔹 12. Remover acentos (normalização avançada de texto)
import unicodedata
df["COLUNA"] = df["COLUNA"].apply(lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', errors='ignore').decode('utf-8'))

# 🔹 13. Criar coluna condicional binária (ex: idade >= 18)
df["ADULTO"] = df["IDADE"].apply(lambda x: "SIM" if pd.notna(x) and x >= 18 else "NÃO")
```

---
