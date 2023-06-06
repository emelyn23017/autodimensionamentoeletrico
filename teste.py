#Importando Bibliotecas
import streamlit as st
from json import loads


#Criando a Pagina Inicial
st.markdown('''
# **!! Bem vindo !!**
### Redimensionamento de Circuito Elétricos

Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  
''')	

# Criando uma Barra Lateral 
st.sidebar.title("MENU")

st.sidebar.selecttext("Qual o Metodo Utilizado",["Metodo A","Método B","Método C","Metodo D"])
st.button("B")
