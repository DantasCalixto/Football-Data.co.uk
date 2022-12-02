###############################################
########## Importando as Bibliotecas ##########
###############################################

import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date
import base64

######################################
########## Título da Página ##########
######################################

st.title("Jogos do Dia - FootyStats")

dia = st.date_input(
    "Data de Análise",
    date.today())

################################################
########## Importando os Jogos do Dia ##########
################################################
@st.cache
def load_data_jogos():
    # Jogos do Dia
    data_jogos = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia/"+str(dia)+"_FutPythonTrader_Jogos_do_Dia.csv?raw=true")
    
    return data_jogos

df_jogos = load_data_jogos()

df_jogos.reset_index(inplace=True, drop=True)
df_jogos.index = df_jogos.index.set_names(['Nº'])
df_jogos = df_jogos.rename(index=lambda x: x + 1)
st.dataframe(df_jogos)
st.markdown('---')

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="jogos_do_Dia_FootyStats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_jogos), unsafe_allow_html=True)