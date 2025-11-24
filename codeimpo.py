import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("global_disaster_response_2018_2024.csv")

with st.sidebar:
    st.write("opciones")
    div = st.slider ("nuemero de bins(histograma):", 1,10,3)
    st.write ("Bins seleccionados:", div)
    st.selectbox ("paises", "tipo de desastres")
fig, ax = plt.subplots(1, 2, figsize=(10, 3))

st.subheader("Histograma basado en tus datos")

numeric_columns = [
        "severity_index", "casualties", "economic_loss_usd", "response_time_hours",
        "aid_amount_usd", "response_efficiency_score", "recovery_days",
        "latitude", "longitude"
    ]
col_hist = st.selectbox("Selecciona columna numérica", numeric_columns)
fig, ax = plt.subplots()
ax.hist(df[col_hist].dropna(), bins=20)
ax.set_title(f"Histograma de {col_hist}")
st.pyplot(fig)