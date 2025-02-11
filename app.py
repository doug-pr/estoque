import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def mostra_qntd_linhas(dataframe):
    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.head(qntd_linhas).style.format(subset = ['Valor'], formatter = '{:.2f}'))

def plot_estoque(dataframe, categoria):

    dados_plot = dataframe.query('Categoria == @categoria')

    fig, ax = plt.subplots(figsize = (8,6))
    ax = sns.barplot(x = 'Produto', y = 'Quantidade', data = dados_plot)
    ax.set_title(f'Quantidade em Estoque dos Produtos de {categoria}', fontsize = 16)
    ax.set_xlabel('Produtos', fontsize = 12)
    ax.tick_params(rotation = 20, axis = 'x')
    ax.set_ylabel('Quantidade', fontsize = 12)

    return fig

# Importando os Dados
dados = pd.read_csv('estoque.csv')

st.title('Análise de Estoque\n')
st.write('Nesse Projeto Vamos Analisar a Quantidade de Produtos em Estoque, por Categoria, de uma Base de Dados de Produtos de Supermercado')

checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar Tabela')
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro Para a Tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a Categoria Para Apresentar na Tabela', options = categorias)

    if categoria != 'Todas':
        df_categoria = dados.query('Categoria == @categoria')
        mostra_qntd_linhas(df_categoria)

    else:
        mostra_qntd_linhas(dados)

st.sidebar.markdown('## Filtro Para o Gráfico')

categoria_grafico = st.sidebar.selectbox('Selecione a Categoria Para Apresentar no Gráfico', options = dados['Categoria'].unique())
figura = plot_estoque(dados, categoria_grafico)
st.pyplot(figura)