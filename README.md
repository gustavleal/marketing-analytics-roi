# Marketing Analytics: Data Pipeline e Análise de ROI

## Visão Geral do Projeto
Este projeto demonstra um fluxo analítico de ponta a ponta voltado para **Marketing Analytics**. 

O objetivo de negócio aqui é sair do dado bruto de campanhas de Ads, realizar o tratamento e estruturar uma modelagem relacional capaz de cruzar custos de mídia com transações aprovadas, revelando o verdadeiro **Retorno Sobre Investimento (ROI)** por canal de aquisição.

## Stack Tecnológica
* **Linguagem:** Python (Pandas) & SQL Avançado.
* **Conceitos Aplicados:** Data Lake (AWS S3 mock), ETL/Data Prep, Modelagem de Dados, CTEs, Window Functions.
* **Visualização:** Estrutura pronta para consumo em ferramentas como Looker Studio.

## Estrutura do Repositório

### 1. Data Prep e Ingestão (`scripts/data_preparation.py`)
Script em Python que simula a extração de dados brutos armazenados em um Data Lake (ex: AWS S3). 
* **O que foi feito:** Limpeza de strings para evitar duplicidade dimensional, tratamento de valores nulos em métricas financeiras e tipagem de datas.
* **Saída:** Tabela padronizada simulando a carga (`analytics_db.marketing_spend_data`) em um Data Warehouse.

### 2. Modelagem Analítica (`scripts/roi_analysis.sql`)
Query projetada para atuar no Data Warehouse, consolidando as métricas de performance.
* **O que foi feito:** Utilização de *Common Table Expressions (CTEs)* para isolar lógicas de custo e receita. Aplicação de *Window Functions* para criar um ranking automatizado de lucratividade das campanhas.
* **Métricas Entregues:** Custo Total, Receita Gerada, Total de Conversões, Lucro Bruto e ROI (%).

## Impacto para o Negócio
*(Exemplo de insight gerado por esta modelagem)*
A estruturação destes dados permite que a equipe de Growth/Marketing identifique rapidamente quais canais estão com ROI negativo (queimando caixa) e realoque o orçamento para campanhas de alta lucratividade baseadas em transações reais, e não apenas em volume de cliques.
