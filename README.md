# LOB1266-PUB - Introdução à Ciência de Dados e Aprendizado de Máquinas
Este repositório contém material didático desenvolvido para a disciplina **LOB1266 - Introdução à Ciência de Dados e Aprendizado de Máquinas** da *Escola de Engenharia de Lorena*, *Universidade de São Paulo*.

# 📚 Sobre o Projeto

**Projeto:** `APRIMORAMENTO DE CONTEÚDOS DIDÁTICOS DA DISCIPLINA LOB1266 - INTRODUÇÃO À CIÊNCIA DE DADOS E APRENDIZADO DE MÁQUINAS`  
**Orientador:** Prof. Dr. Fabiano Fernandes Bargos  
**Bolsista:** João Vitor Fernandes Gomes  
**Programa:** Programa Unificado de Bolsas (PUB) - Vertente de Ensino

# ⚙️ Como usar
1. Instale [`git`](https://git-scm.com/downloads) e [Python](https://www.python.org/downloads/) (3.12) em sua máquina.
2. Clone o repositório em um local desejado:  
`git clone https://github.com/JCFDGG/LOB1266-PUB.git`
3. Instale as dependências:  
`pip install -r requirements.txt`
4. Abra o notebook na pasta `aulas/`:  
`cd aulas && jupyter notebook`

# 🗂️ Estrutura do Projeto
```
├── aulas/
│   ├── aula_03_pandas/         
│   ├── aula_04_scraping/       
│   ├── aula_05_visualizacao/   
│   ├── aula_06_classifiers/    
│   ├── aula_07_regressao/      
│   ├── aula_08_clustering/     
│   └── aula_09_geodados/       
└── dados/                      
    ├── 03_pandas/
    ├── 04_scraping/
    ├── 05_visualizacao/
    ├── 06_classifiers/
    ├── 07_regressao/
    ├── 08_clustering/
    └── 09_geodados/
```

# 📖 Conteúdo das Aulas


## Aula 03 - Pandas
- Introdução à biblioteca Pandas
-  Manipulação de DataFrames
- Operações básicas com dados tabulares
- Limpeza e preprocessamento de dados
## Aula 04 - Web Scraping
- Técnicas de coleta de dados da web
- Bibliotecas para web scraping
- Tratamento de dados do INMET
## Aula 05 - Visualização
- Criação de gráficos e visualizações
- Bibliotecas de visualização (matplotlib, seaborn)
- Análise exploratória de dados (INMET)
- Relatórios automatizados com ydata-profiling
## Aula 06 - Classificadores
- Algoritmos de classificação
- Avaliação de modelos
- Métricas de performance
## Aula 07 - Regressão
- Modelos de regressão
- Pipelines
- *Feature selection* e *feature engineering*
- *Cross Validation*
- Redes neurais (MLP)
## Aula 08 - Clustering
- Algoritmos de agrupamento
- Análise de *clusters*
- Métodos não supervisionados
## Aula 09 - Geodados
- Dados Raster vs dados Vector
- As bibliotecas **Rasterio** e **Geopandas**
- Análise de dados geográficos
- Visualização de mapas
- Processamento de dados espaciais


# 🛠️ Tecnologias Utilizadas
- Python:
    - pandas
    - numPy 
    - matplotlib
    - jsonl
    - beautifulsoup
    - scikit-learn
    - jupyter Notebooks
    - ydata-profiling
    - geopandas
    - rasterio
    - folium
    - geoviews

- JSON: arquivos e estruturas.
- HTML: arquivos e estruturas.
- APIs do INMET.
- CRISP-DM.

# ✒️ Direitos Autorais:
## Código
A ser determinado.

## Datasets:
### Aula 3:
- Todos arquivos adquiridos ou pela API do INMET ou pelos Dados Históricos do [INMET](https://portal.inmet.gov.br/dadoshistoricos) 
### Aula 4:
- Dados adquiridos pela API do INMET.
### Aula 5:
- Dados Históricos adquiridos do [INMET](https://portal.inmet.gov.br/dadoshistoricos).
### Aula 6:
- Dados Históricos adquiridos do [INMET](https://portal.inmet.gov.br/dadoshistoricos).
### Aula 7:
- Todos dados disponibilizados pela UC Irvine: Machine Learning Repository  (https://doi.org/10.24432/C59K76)
### Aula 8:
 - Todos dados disponibilizados pela UC Irvine: Machine Learning Repository ([doi.org/10.24432/C5R88H](doi.org/10.24432/C5R88H))
 ```
 The original data set (hosted at https://www.synapse.org/#!Synapse:syn4301332) is maintained by the cancer genome atlas pan-cancer analysis project.
 ```
### Aula 9:
- `biomas.geojson` e `brazil_states.geojson`: biblioteca [**geobr**](https://github.com/ipeaGIT/geobr)
- `bdq_tratado` e `df_bdq_nan.geojson`: [Brasil Queimadas](https://terrabrasilis.dpi.inpe.br/queimadas/bdqueimadas/)



---

**Universidade de São Paulo  
Escola de Engenharia de Lorena  
LOB1266 - Introdução à Ciência de Dados e Aprendizado de Máquinas**