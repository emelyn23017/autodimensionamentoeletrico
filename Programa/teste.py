#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#__________________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar

bar.title("MENU")

pagina_inicial = bar.button("Página Inicial", type="primary")
pagina_redi = bar.button("Redimensionamento", type="primary")
pagina_sobre = bar.button("Sobre o Projeto", type="primary")


inicial = st.container()
redi = st.container()
sobre = st.container()

#_______________________________________________________________________________________________________________________________________________________________________________


# Criando a Pagina Inicial____________________________________________________________________________________________________________________________________________________________
if pagina_inicial:
  inicial.empty()
  with inicial:
    st.markdown('''

    # Bem vindo
    ### Redimensionamento de Circuito Elétricos

    Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
    Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
    Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  

    ''')
#______________________________________________________________________________________________________________________________________________________________________________


# Criando a Aba de Redimencionamento______________________________________________________________________________________________________________________________________________
metodo = ""

if pagina_redi:
  redi.empty()
  with redi:
    st.title("Redimensionamento de Circuitos")
    st.write('<font size="6">Selecione as variáveis do seu circuito:</font>', unsafe_allow_html=True)
    with st.form(key='redimensionamento_form'):
      metodo = st.selectbox("Método", ["", "Método A1","Método A2" "Método B1","Método B2", "Método C", "Método D", "Método E"])
      tensao = st.selectbox("Tensão", ["127V", "220V", "380V"])
      potencia = st.slider("Potência Total do Circuito", min_value=0, max_value=26000)
      num_circuitos = st.slider("Circuitos no mesmo eletrodulto", min_value=1, max_value=30)
      temperatura = st.slider("Temperatura", min_value=0, max_value=50)
      botao_metodo = st.form_submit_button("?")
      if botao_metodo:
        st.write("Metodos de Dimencionamento")
      
      
#_______________________________________________________________________________________________________________________________________________________________________________


# Criando Pagina "Sobre"_________________________________________________________________________________________________________________________________________________________
if pagina_sobre:
  sobre.empty()
  with sobre:
    st.markdown("""
    # Sobre o Projeto:
    
    ### Esse projeto foi criado para ajudar no dicimencionamento de circuitos elétricos. 
    
   Criadores e Idealizadores:  
    -Emelyn  
    -José David  
    -Daniel Bravin  
    -Gustavo Matos  
    
    """)
#________________________________________________________________________________________________________________________________________________________________________________

