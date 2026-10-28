"""Verificação funcional dos controles e gráficos, sem navegador externo."""
from pathlib import Path
from streamlit.testing.v1 import AppTest

app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"), default_timeout=30).run()
assert not app.exception
assert len(app.get("plotly_chart")) == 2
assert app.metric[0].value == "51.525"
app.checkbox[0].uncheck().run()
assert len(app.get("plotly_chart")) == 1
app.checkbox[1].uncheck().run()
assert len(app.get("plotly_chart")) == 0
assert len(app.info) == 1
app.checkbox[0].check().run()
app.checkbox[1].check().run()
for kind in app.selectbox[0].options:
    app.selectbox[0].select(kind).run()
    assert not app.exception, kind
    assert len(app.get("plotly_chart")) == 2, kind
app.slider[0].set_value(100).run()
assert not app.exception
print("OK: abertura, dois gráficos, alternância, todos os tipos e intervalos.")
