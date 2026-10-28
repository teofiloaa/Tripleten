# AutoScope — Sprint 5 da TripleTen

Dashboard de anúncios de veículos desenvolvido com Python, pandas, Plotly Express e Streamlit. Permite explorar a distribuição do odômetro e a relação entre distância percorrida e preço anunciado.

**Aplicativo publicado:** https://tripleten-sprint5-autoscope.onrender.com/

Deploy confirmado como **Live** pelo Render em 28/10/2026, no plano gratuito. A instância pode demorar a responder após inatividade.

## Funcionalidades

- Cabeçalho e indicadores: quantidade de anúncios, preço mediano e ausências no odômetro.
- Histograma interativo do odômetro com número de intervalos ajustável.
- Dispersão de preço × odômetro, colorida pela condição do veículo.
- Caixas de seleção para mostrar ou ocultar os dois gráficos.
- Filtro por tipo de veículo, aplicado aos indicadores e gráficos.
- Prévia dos dados e explicação dos critérios adotados.

## Arquivos

| Arquivo | Papel |
|---|---|
| `app.py` | Aplicativo Streamlit |
| `vehicles_us.csv` | Dados originais fornecidos pela TripleTen |
| `notebooks/EDA.ipynb` | Análise exploratória, gráficos e conclusões em português |
| `requirements.txt` | Bibliotecas do aplicativo |
| `requirements-dev.txt` | Dependências adicionais para notebook e validação |
| `.streamlit/config.toml` | Configuração do servidor e tema |
| `render.yaml` | Receita de publicação no Render |
| `tests/test_app.py` | Teste funcional dos controles e gráficos |
| `EXPLICACAO.md` | Explicação detalhada do projeto |

## Executar no computador

Requer Python 3.12. Dentro da pasta do projeto:

```bash
python -m venv vehicles_env
```

Ativar no Windows PowerShell:

```powershell
.\vehicles_env\Scripts\Activate.ps1
```

Ativar no macOS/Linux:

```bash
source vehicles_env/bin/activate
```

Instalar e abrir:

```bash
python -m pip install -r requirements-dev.txt
streamlit run app.py
```

Abrir `http://localhost:10000`. No VS Code, selecionar o interpretador de `vehicles_env`; abrir `notebooks/EDA.ipynb`, selecionar o mesmo ambiente como kernel e executar todas as células.

`plotly.express` é importado do pacote `plotly`. O nome correto do arquivo usado na instalação é `requirements.txt`; a configuração fica em `.streamlit/config.toml`, com ponto inicial. Isso resolve inconsistências de nomenclatura no enunciado.

## Publicar no Render

1. Entrar na conta Render e criar **New → Web Service**.
2. Selecionar o repositório `teofiloaa/Tripleten` e a branch `main`.
3. Selecionar Python e deixar a pasta raiz vazia.
4. Build Command: `pip install -r requirements.txt`.
5. Start Command: `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT`.
6. Definir `PYTHON_VERSION=3.12.12` e selecionar a instância gratuita, caso disponível. Não escolher uma opção paga sem decisão expressa.
7. Publicar, esperar o estado Live e abrir a URL fornecida pelo Render.
8. Testar os dois gráficos e as caixas de seleção; adicionar a URL real ao início deste README.

O `render.yaml` também permite configurar o serviço por Blueprint. Este serviço foi publicado pela interface do Render usando os comandos acima.

## Dados e resultados

Fonte: [CSV disponibilizado pela TripleTen](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_NEW_4_sprint/vehicles.csv), salvo como `vehicles_us.csv`.

- 51.525 anúncios e 13 colunas; nenhum duplicado completo.
- 7.892 anúncios sem odômetro; os gráficos usam 43.633 observações completas.
- Preço mediano geral: US$ 9.000.
- Odômetro mediano entre os preenchidos: 113.000 milhas.
- Correlação de Pearson entre preço e odômetro: aproximadamente −0,420.

O CSV é preservado. Não imputamos zero nos valores ausentes e não removemos extremos arbitrariamente. A análise descreve anúncios, não vendas confirmadas; correlação não demonstra causalidade.

## Validação

```bash
python tests/test_app.py
```

O teste verifica abertura sem exceções, presença de dois gráficos, alternância das caixas de seleção, todos os tipos de veículo e ajuste dos intervalos. As células do notebook foram executadas sequencialmente com IPython e suas saídas foram gravadas; o kernel Jupyter separado não iniciou neste ambiente por restrição de sockets. O Render confirmou a publicação como Live. A validação interativa da página pública ainda não foi concluída, devido à interrupção da ligação de controle do navegador.

## Entrega

Link do repositório para entrega à TripleTen, após conferir a página pública:

https://github.com/teofiloaa/Tripleten

A aprovação depende da avaliação do revisor.
