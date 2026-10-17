# TripleTen — Sprint 5: Dashboard de Anúncios de Automóveis

Aplicação de análise de anúncios de veículos usados com Python, Pandas, Plotly Express e Streamlit, desenvolvida para o Sprint 5 da TripleTen.

## Funcionalidades
- Indicadores de quantidade de anúncios, preço mediano e quilometragem mediana.
- Filtro por tipo de veículo.
- Histograma interativo da quilometragem.
- Gráfico de dispersão entre quilometragem e preço.
- Pré-visualização dos primeiros 100 registos.

## Estrutura
- README.md — documentação.
- app.py — aplicação Streamlit.
- vehicles_us.csv — dataset dos anúncios.
- requirements.txt — dependências.
- notebooks/EDA.ipynb — exploração inicial dos dados.
- .streamlit/config.toml — configuração do servidor.
- scripts/download_data.py — obtenção e validação do CSV.
- render.yaml — configuração opcional para Render.

## Executar localmente
1. Clonar: git clone https://github.com/teofiloaa/Tripleten.git
2. Entrar: cd Tripleten
3. Criar ambiente: python -m venv .venv
4. Ativar ambiente: no Windows, .venv\Scripts\Activate.ps1; no macOS/Linux, source .venv/bin/activate
5. Instalar: pip install -r requirements.txt
6. Se necessário, obter dados: python scripts/download_data.py
7. Executar: streamlit run app.py

## Origem dos dados
O CSV é obtido preferencialmente do [ficheiro fornecido pela TripleTen](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_NEW_4_sprint/vehicles.csv), com alternativa de uma [cópia pública do mesmo dataset](https://github.com/Pushkarski/05_used_car_sales_dashboard). O script valida as colunas e o número de registos.

## Publicação no Render
1. Criar um Web Service associado ao repositório e selecionar a branch sprint-5-dashboard.
2. Build Command: pip install --upgrade pip && pip install -r requirements.txt
3. Start Command: streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
4. Também é possível usar render.yaml com o modo Blueprint.
5. Verificar a aplicação e acrescentar a URL pública abaixo.

**URL do Render:** Pendente de implementação.

## Critérios de aprovação
- [x] README, app.py, notebooks/EDA.ipynb, requirements.txt e configuração Streamlit.
- [x] Cabeçalho, histograma, gráfico de dispersão e caixas de seleção.
- [x] Testes automáticos de dados, notebook e dashboard concluídos com sucesso no GitHub Actions.
- [x] Ficheiro vehicles_us.csv descarregado, validado e versionado.
- [ ] Confirmar que a aplicação está acessível no Render.
- [ ] Acrescentar a URL pública e enviar link do GitHub para avaliação.

O pacote moderno plotly já inclui plotly.express, utilizado pelo projeto.
