"""Testes funcionais do dashboard (sem browser)."""
from pathlib import Path
import unittest

import nbformat
import pandas as pd
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


class ProjectTests(unittest.TestCase):
    def test_dataset_integrity(self):
        data = pd.read_csv(ROOT / "vehicles_us.csv")
        self.assertGreaterEqual(len(data), 50000)
        self.assertTrue({"price", "odometer", "model", "type", "condition"}.issubset(data.columns))

    def test_notebook_structure(self):
        notebook = nbformat.read(ROOT / "notebooks" / "EDA.ipynb", as_version=4)
        nbformat.validate(notebook)
        cells = "\n".join("".join(cell.source) for cell in notebook.cells if cell.cell_type == "code")
        self.assertIn("px.histogram", cells)
        self.assertIn("px.scatter", cells)

    def test_streamlit_initial_render(self):
        app = AppTest.from_file(ROOT / "app.py", default_timeout=120).run()
        self.assertEqual(len(app.exception), 0, [str(e) for e in app.exception])
        self.assertGreaterEqual(len(app.title), 1)
        self.assertGreaterEqual(len(app.checkbox), 1)
        self.assertGreaterEqual(len(app.get("plotly_chart")), 2)

    def test_streamlit_checkbox(self):
        app = AppTest.from_file(ROOT / "app.py", default_timeout=120).run()
        self.assertEqual(len(app.exception), 0)
        app.checkbox[0].set_value(False).run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.get("plotly_chart")), 1)


if __name__ == "__main__":
    unittest.main()
