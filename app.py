"""Dashboard do Sprint 5: exploração de anúncios de veículos."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="AutoScope | Sprint 5", page_icon="🚘", layout="wide")

@st.cache_data
def load_data():
    # Caminho relativo ao script: funciona mesmo fora da pasta do projeto.
    return pd.read_csv(Path(__file__).resolve().parent / "vehicles_us.csv")

st.caption("TRIPLETEN · SPRINT 5 · FERRAMENTAS DE DESENVOLVIMENTO DE SOFTWARE")
st.header("AutoScope — anúncios de veículos")
st.write("Explore a distribuição da quilometragem e a relação entre uso e preço anunciado.")
data = load_data()
with st.sidebar:
    st.header("Explorar os dados")
    vehicle_type = st.selectbox("Tipo de veículo", ["Todos"] + sorted(data["type"].dropna().unique().tolist()))
    show_hist = st.checkbox("Mostrar histograma", value=True)
    show_scatter = st.checkbox("Mostrar gráfico de dispersão", value=True)
    bins = st.slider("Número de intervalos do histograma", 10, 100, 50, 10)
    st.caption("Fonte: conjunto de anúncios fornecido pela TripleTen. Preços em USD; odômetro em milhas.")

filtered = data if vehicle_type == "Todos" else data[data["type"] == vehicle_type]
valid = filtered.dropna(subset=["odometer", "price"])
a, b, c = st.columns(3)
a.metric("Anúncios selecionados", f"{len(filtered):,}".replace(",", "."))
b.metric("Preço mediano (USD)", f"{filtered['price'].median():,.0f}".replace(",", "."))
c.metric("Sem odômetro informado", f"{filtered['odometer'].isna().sum():,}".replace(",", "."))
st.caption("As métricas consideram todos os anúncios do filtro. Os gráficos usam somente registros com os campos necessários preenchidos, sem imputar valores.")
labels = {"odometer": "Odômetro (milhas)", "price": "Preço anunciado (USD)", "condition": "Condição"}
if valid.empty:
    st.warning("Não há registros com preço e odômetro disponíveis para este filtro.")
else:
    if show_hist:
        st.subheader("Quanto estes veículos já rodaram?")
        fig = px.histogram(valid, x="odometer", nbins=bins, labels=labels,
                           color_discrete_sequence=["#2563eb"])
        fig.update_layout(yaxis_title="Quantidade de anúncios", bargap=0.04)
        st.plotly_chart(fig, width="stretch")
        st.caption(f"{len(valid):,} anúncios com odômetro informado. Passe o cursor sobre as barras para ver a contagem.")
    if show_scatter:
        st.subheader("Como o preço varia com o uso?")
        fig = px.scatter(valid, x="odometer", y="price", color="condition",
                         hover_data=["model", "model_year"], labels=labels,
                         opacity=0.45, render_mode="webgl")
        st.plotly_chart(fig, width="stretch")
        st.caption("Cada ponto representa um anúncio. Use o zoom para explorar concentrações; os valores extremos foram mantidos. Associação não implica causalidade.")
if not show_hist and not show_scatter:
    st.info("Selecione um gráfico na barra lateral para começar.")
with st.expander("Consultar dados e critérios"):
    st.write("O CSV original é preservado. Valores ausentes não são substituídos por zero. Preços são valores pedidos, não vendas confirmadas. O conjunto não representa necessariamente todo o mercado.")
    st.dataframe(filtered.head(500), hide_index=True, width="stretch")
    st.caption("Prévia limitada aos primeiros 500 anúncios do filtro; os gráficos usam todos os registros válidos.")
