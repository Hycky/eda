import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/data.csv')
profile = ProfileReport(df, title="Análise Exploratória de Dados - APAE")	
profile.to_file("eda_apae.html")
