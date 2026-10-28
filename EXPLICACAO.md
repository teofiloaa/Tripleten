# Explicação do projeto — Sprint 5

## 1. O objetivo

Transformar uma análise Python em um aplicativo acessível no navegador. O projeto reúne ambiente virtual, pandas, gráficos Plotly, interface Streamlit, versionamento Git/GitHub e configuração de implantação no Render.

## 2. Ambiente virtual e bibliotecas

Foi criado um ambiente chamado `vehicles_env`. Ele isola as bibliotecas deste projeto das usadas por outros projetos. A pasta do ambiente não deve ser enviada para o GitHub: outras pessoas a recriam usando os arquivos de dependências.

- **pandas:** lê o CSV como DataFrame, seleciona linhas e calcula indicadores.
- **plotly:** contém `plotly.express`, que cria os gráficos interativos.
- **streamlit:** transforma o script Python em uma interface web.
- **nbformat, nbclient e ipykernel:** ferramentas de notebook no ambiente de desenvolvimento.

As dependências principais ficam sem versões, conforme a proposta didática. Para uma aplicação de produção, fixar versões testadas ajudaria a reproduzir o ambiente com maior rigor.

## 3. Aquisição e inspeção dos dados

O arquivo fornecido pela TripleTen foi baixado e salvo como `vehicles_us.csv`. O conteúdo original foi preservado. O notebook usa `head()` para conhecer as primeiras linhas, `info()` para tipos e preenchimento, `isna().sum()` para ausências, `duplicated().sum()` para repetição completa e `describe()` para estatísticas.

Encontramos 51.525 linhas e 13 colunas. Não há duplicados completos. Existem 7.892 ausências no odômetro, além de ausências no ano, cilindros, cor e tração.

Não há justificativa para transformar todas as ausências em zero: um odômetro desconhecido não significa um veículo sem uso. Por isso `dropna(subset=[...])` é aplicado apenas às colunas necessárias para cada gráfico. Os dados originais e os demais registros continuam disponíveis.

## 4. O que os gráficos mostram

O **histograma** divide o odômetro em intervalos e conta anúncios em cada um. Ele ajuda a ver concentrações e valores extremos. A mediana é 113.000 milhas. O máximo é 990.000, o que amplia a escala; esses valores não foram apagados sem evidência de erro.

O **gráfico de dispersão** coloca odômetro no eixo X e preço no Y. Cada ponto é um anúncio. A transparência facilita perceber pontos sobrepostos; a cor distingue condições do veículo. Passar o cursor mostra modelo e ano. O gráfico tem zoom.

A correlação de Pearson é aproximadamente −0,420, calculada nos 43.633 anúncios com as duas variáveis. Há associação negativa moderada: veículos mais rodados tendem a ter preços menores neste conjunto. Isso não prova causalidade, e outras características influenciam o preço. Não foi criado um modelo preditivo.

## 5. Como `app.py` funciona

1. Importa `Path`, pandas, Plotly Express e Streamlit.
2. Define título, ícone e layout da página com `st.set_page_config`.
3. `load_data()` localiza o CSV a partir da pasta do próprio script. Assim, não depende da pasta de onde o comando foi iniciado.
4. `@st.cache_data` evita reler o CSV desnecessariamente a cada interação.
5. A barra lateral contém filtro, duas caixas de seleção e um controle do número de intervalos.
6. O filtro gera um DataFrame com o tipo escolhido; a opção Todos mantém o conjunto inteiro.
7. Os indicadores contam anúncios, calculam a mediana do preço e contam ausências no filtro.
8. As caixas de seleção decidem quais figuras criar com `px.histogram` e `px.scatter`.
9. `st.plotly_chart` coloca as figuras na página. O aplicativo usa `width="stretch"`, conforme a API atual.
10. Uma seção expansível mostra os critérios e uma prévia de 500 linhas. O limite da tabela não limita os gráficos.

Streamlit executa novamente o script quando um controle muda. O cache torna a leitura eficiente, enquanto indicadores e figuras são recalculados para a seleção atual. As caixas de seleção são a alternativa permitida pelo enunciado aos botões.

## 6. Configuração do servidor

`.streamlit/config.toml` define execução sem interface de desktop, endereço `0.0.0.0` e porta local 10000. O endereço permite ao servidor receber conexões no ambiente de hospedagem. No Render, o comando usa `$PORT`, a porta fornecida pela plataforma, que prevalece sobre a configuração local.

`render.yaml` descreve um serviço Python, o comando para instalar bibliotecas, o comando de inicialização e a rota de saúde. Ele prepara a publicação, mas não cria sozinho um aplicativo online.

## 7. Git e GitHub

Foi aproveitado o repositório existente `teofiloaa/Tripleten`, inicialmente com README e `.gitignore`. O código, notebook, CSV e documentação são versionados juntos. O ambiente virtual fica fora do repositório. Um commit registra o estado dos arquivos; o envio ao GitHub permite compartilhar e usar esse estado no Render.

## 8. Verificações realizadas

O teste com `streamlit.testing.v1.AppTest` confirmou abertura sem exceções, dois gráficos iniciais, ocultação e reexibição de cada gráfico, aviso quando ambos estão ocultos, todos os tipos de veículo e mudança dos intervalos.

Todas as células do notebook foram executadas sequencialmente com IPython, com saídas guardadas no arquivo. O kernel Jupyter separado não iniciou devido à restrição de sockets deste ambiente; isso foi contornado pela execução no mesmo processo, sem inventar resultados.

Ainda é necessário publicar no Render, abrir a URL pública e conferir o comportamento no navegador. O acesso ao Render pelo navegador não foi concluído nesta execução. Portanto, não é correto afirmar que o deploy foi testado ou que o projeto já foi entregue para avaliação.

## 9. Como explicar o trabalho ao revisor

“Desenvolvi um dashboard em Streamlit usando dados de anúncios de veículos. Fiz uma inspeção inicial no notebook, preservei o CSV e tratei valores ausentes apenas quando necessários aos gráficos. Construí um histograma do odômetro e uma dispersão de preço versus odômetro com Plotly Express. Adicionei caixas de seleção, filtro por tipo e indicadores. Organizei dependências e configuração de hospedagem e testei os controles do aplicativo.”

Só acrescentar que o aplicativo foi publicado e testado no Render depois de concluir essa etapa e verificar a URL real.
