import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
import streamlit as st
import plotly_express as px



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

bd = pd.read_excel('vendas.xlsx')



ano = st.sidebar.multiselect(
    key=1,
    label="Ano",
    options=bd["Ano_compra"].unique(),
    default=bd["Ano_compra"].unique()
)

categoria = st.sidebar.multiselect(
    key=2,
    label="Categoria",
    options=bd["Categoria"].unique(),
    default=bd["Categoria"].unique()
)

bd = bd.query("Ano_compra == @ano and Categoria == @categoria")

st.header(":bar_chart: Vendas de Produtos")
st.markdown("#")
st.markdown("""---""")

quantidade_vendidas = round(bd["Quantidade"].sum())
total_vendido = round(bd["Preco_Unit"].sum(),2)

#Agrupamento para gráfico
vendas_ano = (bd.groupby(by="Ano_compra").sum(numeric_only=True)[["Quantidade"]].sort_values("Ano_compra"))
venda_categoria = (bd.groupby(by="Categoria").sum(numeric_only=True)[["Quantidade"]].sort_values("Categoria"))

fig_venda_categoria = px.area(venda_categoria, title="<b style='color: orange:'>Quantidade de Vendas por Categoria</b>")

col1, col2 = st.columns(2)
col1.metric("Quantidade vendidas", quantidade_vendidas)
col2.metric("Total Vendido", total_vendido)

st.markdown("""---""")
st.plotly_chart(fig_venda_categoria)

st.dataframe(bd)
