import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("global_disaster_response_2018_2024 (1).csv")

st.title = ("desastres naturales")

with st.sidebar:
    st.write("opciones")
    div =  st.slider("Número de bins (histograma):", 1, 10, 2)
    st.write("Bins seleccionados:", div)

st.subheader("Histograma basado en tus datos")
numeric_columns = [
        "severity_index", "casualties", "economic_loss_usd", "response_time_hours",
        "aid_amount_usd", "response_efficiency_score", "recovery_days",
        "latitude", "longitude"
    ]
col_hist = st.selectbox("Selecciona columna numérica", numeric_columns)
fig, ax = plt.subplots()
ax.hist(df[col_hist].dropna(), bins= div)
ax.set_title(f"Histograma de {col_hist}")
st.pyplot(fig)

with st.sidebar:
    st.write("opciones")
    dev = st.selectbox( "Tipo de desastre", "países")
st.subheader("Gráfico de pastel (Países)")

pie_data = df["country"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
ax2.set_title("Distribución por país")

st.pyplot(fig2)

st.subheader("Gráfico de pastel (Tipo de desastre)")

pie_data2 = df["disaster_type"].value_counts()

fig3, ax3 = plt.subplots()
ax3.pie(pie_data2, labels=pie_data2.index, autopct="%1.1f%%")
ax3.set_title("Distribución por tipo de desastre")

st.pyplot(fig3)

