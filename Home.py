import streamlit as st
import numpy as np
import pandas as pd
import datetime
import plotly.express as px


st.title('meu titulo site')


st.sidebar.title('meu titulo site')

caixinha = st.sidebar.checkbox('caixinha')


ano = np.arange(1993,2024,1)

ano_selecionado = st.sidebar.selectbox('Selecione o ano', ano)
ano_selecionado


df = pd.read_csv('data.csv', sep = ';')
df['data'] = pd.to_datetime(df['datahora'])
df.set_index('data',inplace= True)


estacoes = df['nomeEstacao'].unique()

selec_estacao = st.sidebar.selectbox('selecione uma estação', estacoes) 

df = df[df['nomeEstacao'] == selec_estacao]



dia = df.index.day.unique()

dia_selecionado = st.sidebar.selectbox('selecione o dia', dia)

df = df[df.index.day == dia_selecionado]

df


st.line_chart(df['valorMedida'])


fig = px.bar(x = df.index,
             y = df['valorMedida'])

st.plotly_chart(fig)