from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = Path(__file__).resolve().parent / "vehicles_us.csv"

st.set_page_config(page_title="Anúncios de Automóveis", page_icon="🚗", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_FILE)
    data["price"] = pd.to_numeric(data["price"], errors="coerce")
    data["odometer"] = pd.to_numeric(data["odometer"], errors="coerce")
    return data

st.title("🚗 Análise de anúncios de automóveis")
st.write("Explore os veículos anunciados e a relação entre quilometragem e preço.")
try:
    car_data = load_data()
except FileNotFoundError:
    st.error("Falta o ficheiro vehicles_us.csv. Execute: python scripts/download_data.py")
    st.stop()
except (OSError, ValueError, KeyError, pd.errors.ParserError) as error:
    st.error(f"Não foi possível ler o CSV: {error}")
    st.stop()

st.sidebar.header("Filtros")
vehicle_types = sorted(car_data["type"].dropna().unique().tolist())
selected_types = st.sidebar.multiselect("Tipo de veículo", vehicle_types, default=vehicle_types)
filtered = car_data[car_data["type"].isin(selected_types)].copy()
if filtered.empty:
    st.warning("Não existem anúncios para os tipos selecionados.")
    st.stop()

a, b, c = st.columns(3)
a.metric("Anúncios", f"{len(filtered):,}")
b.metric("Preço mediano", f"US$ {filtered['price'].median():,.0f}")
c.metric("Quilometragem mediana", f"{filtered['odometer'].median():,.0f} mi")

st.header("Gráficos interativos")
show_histogram = st.checkbox("Mostrar histograma da quilometragem", value=True)
show_scatter = st.checkbox("Mostrar gráfico de dispersão: quilometragem e preço", value=True)

if show_histogram:
    fig_hist = px.histogram(
        filtered.dropna(subset=["odometer"]),
        x="odometer",
        nbins=50,
        title="Distribuição da quilometragem",
        labels={"odometer": "Quilometragem (milhas)"},
    )
    fig_hist.update_layout(yaxis_title="Número de anúncios")
    st.plotly_chart(fig_hist, width="stretch")

if show_scatter:
    fig_scatter = px.scatter(
        filtered.dropna(subset=["odometer", "price"]),
        x="odometer", y="price", color="condition", hover_name="model", opacity=0.55,
        title="Quilometragem vs. preço",
        labels={
            "odometer": "Quilometragem (milhas)",
            "price": "Preço (USD)",
            "condition": "Estado",
        },
    )
    st.plotly_chart(fig_scatter, width="stretch")

with st.expander("Pré-visualizar os dados"):
    st.dataframe(filtered.head(100), width="stretch")

st.caption("Fonte: anúncios de veículos do Sprint 5 da TripleTen; preços em USD e quilometragem em milhas.")
