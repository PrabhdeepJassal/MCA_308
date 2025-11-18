import streamlit as st
import nbformat
from nbconvert import HTMLExporter

st.set_page_config(page_title="Project Notebook Viewer", layout="wide")

st.title("📘 Project Notebook Viewer")
st.write("Displaying your Jupyter Notebook inside Streamlit.")

# Path to your notebook
NOTEBOOK_PATH = "project-labeval.ipynb"

# Load the notebook
with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Convert to HTML
html_exporter = HTMLExporter()
html_exporter.template_name = "classic"  # cleaner output

(body, resources) = html_exporter.from_notebook_node(notebook)

# Render inside Streamlit
st.components.v1.html(body, height=1200, scrolling=True)
