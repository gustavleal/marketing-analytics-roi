import pandas as pd
import numpy as np

print("Iniciando extração de dados de Marketing...")

caminho_datalake = "s3://datalake-marketing-corp/raw/spend_data_2026.csv"
print(f"Conectando à fonte bruta: {caminho_datalake}")

dados_mock = {
    'id_campanha': ['CMP-001', 'CMP-002', 'CMP-003', 'CMP-004'],
    'data_campanha': ['2026-04-01', '2026-04-01', '2026-04-02', '2026-04-02'],
    'canal_aquisicao': [' Google Ads ', 'META ADS', 'google ads', 'Meta Ads'],
    'investimento': [150.50, 200.00, np.nan, 250.00],
    'cliques': [300, 450, 100, 500]
}
df_spend = pd.DataFrame(dados_mock)

print("\nExecutando Data Prep (Limpeza e Padronização via Pandas)...")

# 1. Limpeza: Padronização de strings para evitar duplicação no SQL
df_spend['canal_aquisicao'] = df_spend['canal_aquisicao'].str.strip().str.upper()

# 2. Tratamento de Nulos: Preenchendo falta de dados financeiros com zero
df_spend['investimento'] = df_spend['investimento'].fillna(0)

# 3. Conversão de Tipos: Garantindo formato de data correto
df_spend['data_campanha'] = pd.to_datetime(df_spend['data_campanha'])

print("\nAmostra dos dados processados:")
print(df_spend.head())

# Simulando a carga (Load) para a tabela de modelagem do banco de dados
tabela_destino = "analytics_db.marketing_spend_data"
print(f"\nCarregando dados limpos no Data Warehouse, tabela: {tabela_destino}")

# Em um ambiente real, o código seria algo como:
# from sqlalchemy import create_engine
# df_spend.to_sql('marketing_spend_data', con=engine, if_exists='replace', index=False)

print("Pipeline em Python finalizado. Dados prontos para consumo no script SQL.")
