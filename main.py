import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from textwrap import wrap


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#função dataframe

def mostrar_linhas(dataframe):
    qtd_linhas = st.sidebar.slider('Selecione a quantidade de linhas para visualização',
                                   min_value=1, max_value=20, step=1)
    st.write(dataframe.head(qtd_linhas))

#função gráfico

def plot_vendas(dataframe, categoria):
    vendas_plot = dataframe.query('Categoria == @categoria')
    fig, ax = plt.subplots(figsize=(14,6))
    ax = sns.barplot(x= 'Produto', y = 'Quantidade', data =vendas_plot)
    ax.set_title(f'Quantidade de vendas de  {categoria}', fontsize=18)
    ax.set_xlabel('Produto', fontsize=14)
    plt.ylim(0, 6)
    ax.tick_params(rotation=15, axis='x')
    ax.set_ylabel('Quantidade', fontsize=14)

    return fig

vendas = pd.read_excel('bd_vendas.xlsx') #, on_bad_lines='skip', encoding="latin")

st.title('Quantidades de Produtos vendidos por Categoria\n')
st.write('Período de jun/2017 a ago/2018')

# filtro para tabela
opcao_1 = st.sidebar.checkbox('Mostrar tabela')
if opcao_1:
    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(vendas['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a catedoria para apresentar a tabela', options=categorias)

    if categoria != 'Todas':
        vendas_categoria = vendas.query('Categoria == @categoria')
        mostrar_linhas(vendas_categoria)
    else:
        mostrar_linhas(vendas)

# filtro para o gráfico
st.sidebar.markdown('## Filtro para o gráfico')

categoria_grafico = st.sidebar.selectbox('Selecione a Categoria', options = vendas['Categoria'].unique())
figura = plot_vendas(vendas, categoria_grafico)
st.pyplot(figura)

