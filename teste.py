#Importando Bibliotecas
import streamlit as st


#Criando o titulo 
st.markdown('''
# **FOFOS DA BITOLA** 
#### APP para redimensionamento
''')
arquivo = st.file_uploader("arquivo aqui")
st.write(arquivo.type)


# Criando uma Barra Lateral 
st.sidebar.title("MENU")

st.selectbox("Qual o Metodo Utilizado",["Metodo A","Método B","Método C","Metodo D"])
st.button("B")
