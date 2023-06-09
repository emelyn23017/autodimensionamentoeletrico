#### Autodimensionamento elétrico residencial 
*Autores:* Daniel Bravin, Emelyn Alves, Gustavo Matos, José David Alves.  

#### Descrição geral: 
O código 'funcoes.py' utiliza as variáveis dadas como coordenadas para encontrar valores em tabelas através da biblioteca pandas. Já o código 'página.py', é onde estão as configurações da interface que utilizamos, além disso, ele se comunica com o código 'funcoes.py', *retornando o disjuntor e a seção tranversal do fio para utilizar no dimensionamento elétrico residencial.* A pasta Notebook contém os primeiros testes não tão bem organizados do código que apenas serve como marco do funcionamento do sistema. 
Link do Streamlit: https://emelyn23017-autodimensionamentoeletrico-pagina-ijjg9l.streamlit.app/ 

#### Introdução: 
O trabalho técnico referente ao dimensionamento elétrico costuma ocorrer por análise manual de dados. Essa análise geralmente é realizada com base no número de circuitos, métodos de instalação e outras condições identificadas na planta elétrica do local. Por isso, quando não realizada por profissionais a instalação está passível à riscos, que comprometem a segurança do local e da própria instalação. Com o objetivo de evitar possíveis acidentes ocasionados por desinstrução ou falha humana e facilitar o cálculo de dimensionamento elétrico, pretendemos criar um código em python, que utilize as biliotecas Pandas, para analisar as variáveis necessárias para o dimesionamento, compara-las com a Norma Regulamentadora vigente (NBR5410) e retornar as especificações do disjuntor e da seção transversal do fio a serem utilizados.

#### Sobre a ANBT NBR5410:
A ABNT NBR5410 é uma Norma Brasileira elaborada pelo Comitê Brasileiro de Eletricidade, pela Comissão de Estudo de Intalações Elétricas de Baixa Tensão, que vigora desde 31 de março de 2005. O objetivo dessa norma é garantir a segurança de pessoas e animais, o bom funcionamento das instalações elétricas e a conservação de bens. 
A NBR5410 é destinada à instalações elétricas de baixa tensão em edificações. Utilizaremos as normas mais específicas para edificações residenciais em nosso projeto. Para tanto, teremos como referência algumas das tabelas disponibilizadas pela norma. Link do pdf da NBR510: https://docente.ifrn.edu.br/jeangaldino/disciplinas/2015.1/instalacoes-eletricas/nbr-5410

#### Sobre as Tabelas NBR5410: 
Serão utilizadas para nosso dimensionamento elétrico 5 diferentes tabelas da NBR5410: Tabelas 33, 36, 37, 40 e 42.

*Tabela 33 - Tipos de linhas elétricas:* Essa tabela relaciona cada método de instalação, ou seja, o modo como foi instalado a rede elétrica, à um método de referência - que será utilizado na tabela 36. A tabela 33 apresenta um esquema ilustrativo do método de instalação, a descrição deste, além do método de referência. Para o projeto de autodimensionamento elétrico utilizaremos os seguintes métodos de referência: A1, A2, B1, B2, C e D (consulte a Tabela 33 - NBR5410 para mais informações). 

*Tabela 36 e 37 - Capacidades de condução de corrente, em ampères, para os métodos de referência A1, A2, B1, B2, C e D:* Ambas as tabelas relacionam cada método de referência à uma seção transversal (mm²) do fio a ser utilizado para a instalação. Para essa relação leva-se em consideração: material do condutor utilizado (cobre ou alumínio), isolação (para a tabela 36 o tipo de isolação é PVC, enquanto para a tabela 37 é a isolação de EPR ou XLPE), temperaturas de referências do: condutor (Tabela 36 - 70°C; Tabela 37 - 90°C) e ambiente (ar - 30°C; solo - 20°C) e número de condutores carregados. 

*Tabela 40 - Fatores de correção para temperaturas ambientes diferentes de 30°C para linhas não-subterrâneas e de 20ºC (temperatura do solo) para linhas subterrâneas:* Identifica o fator de correção a ser utilizado para o dimensionamento levando em consideração o tipo de isolação (PVC e EPR ou XLPE) e temperatura. 

*Tabela 42 - Fatores de correção aplicáveis a condutores agrupados em feixe (em linhas abertas ou fechadas) e a condutores agrupados num mesmo plano, em camada única:* Identifica o fator de correção a ser utilizado para o dimensionamento de acordo com a forma de agrupamentos dos condutores e o número de circuitos. 

*Observação:* Tais tabelas apresentam importantes dados para o correto dimensionamento elétrico, como tabelas de corrente máxima e de aquecimento de uma determinada seção. Essas tabelas se relacionam, de forma que, por exemplo: uma temperatura mais alta ou mais baixa que o normal faz com que a corrente que o fio suporta, sem aquecer, aumente ou diminua em função de um fator de correção determinado em uma outra tabela, que, por sua vez, é aplicado na tabela referente à corrente limite e seção. Ou seja, os dados se relacionam diretamente e uma pequena alteração de uma variável pode mudar completamente o resultado final, o que gera um grande risco por falhas humanas.

#### Sobre o projeto de autodimensionamento elétrico: 

Nosso projeto é dividido em duas principais partes: 

  A) *Interface:* Será a rosto do nosso programa e a responsável por coletar os dados do esquema elétrico do usuário. Utilizaremos o site Streamlit para criá-la. Pretendemos fazer uma interface acessível e intuitiva. Até o momento, pretendemos fazer a inteface dividida em três partes principais: 
  1. Apresentação do projeto - Destinada à introdução do projeto, com o objetivo deste e informações gerais sobre os integrantes. 
  2. Área de coleta de dados - Destinada à coleta de dados dos usuário. Os dados coletados serão: método de referência (baseado nos métodos de instalação), tensão, potência total, temperatura do ambiente (°C), tipo de isolameto (PCV, EPR ou XLEP), número de circuitos no eletroduto e local de instalação (chão, teto ou parede). 
  3. Resposta às variáveis dadas pelo usuário - Área designada somente para fornecer o disjuntor e a área da seção transversal do fio a serem utilizados nas instalações.
  Link do site com o programa rodando parcialmente: https://emelyn23017-autodimensionamentoeletrico-pagina-ijjg9l.streamlit.app/ 
  
  B) *Análise de dados:* Usando as variáveis disponibilizadas pelo usuário, relacionará estas com a NBR5410. Esta comparação, nos indicará qual será o disjuntor e a seção transversal do condutor mais indicados para o tipo de instalação especificado. A análise de dados será realizada a partir do programa em Python. 

#### O que foi desenvolvido?
Até o momento, já conseguimos desenvolver um código funcional que recebe uma potência, uma tensão, um método de instalação, um número de circuitos no mesmo eletrodulto e uma temperatura no ambiente para conseguir fazer o dimensionamento com base nesses diversos dados. Isso ocorre por meio da biblioteca Pandas. Baixando a pasta "Programa" é possível fazer uso do que já desenvolvemos até o momento. O arquivo principal é o "Autodimencionamento.ipynb", ele ainda não está no formato python. Entrando nesse notebook, o usuário pode alterar a potência(P), a tensão(V) o número de circuitos no mesmo eletrodulto e a temperatura do ambiente para descobrir o disjuntor e a seção nominal correta do fio para a instalação dessa carga. Ainda não é possível entregar claramente o método e o isolamento do fio, mas depois que a interface for desenvolvida será possível fazer isso facilmente.

##### INTERFACE (Front-end):
![image](https://github.com/emelyn23017/autodimensionamentoeletrico/assets/135053736/968dcd4e-403c-4dc9-87de-beb39a8ca194)

*Atualizações sobre a interface (13/06):* A imagem acima nos mostra uma base de iríamos trabalhar no nosso layout final. No entanto, por recomendação, resolvermos utilizar o site "Streamlit" para montagem da nossa interface. Portanto, o design passou por alterações. Como o Streamlit permite criar uma página web e altera-lá diretamente pelo github, algumas das configurações são um tanto quanto limitantes, mas ele permite trabalhar de maneira simples e rápida. O código, que ainda passa por desenvolvimento, carece de polimento e organização, contudo se mostra funcional, tanto que, consegue retornar, até o momento o valor da intensidade de corrente (dado em Ampéres - A) no circuito dado pelo usuário.  
*Atualização sobre a interface (20/06):* 

##### INFORMAÇÕES SOBRE DADOS:
Cógido principal: 'pagina.py', esse código armazena as configurações da interface do Streamlit. Além disso, utiliza-se do código de apoio 'funcoes.py' para retornar os valores do disjuntor e seção tranversal do fio. 
Código de apoio: 'funcoes.py', esse código utiliza as variáveis dadas como coordenadas para encontrar valores em tabelas através da biblioteca pandas. Dentro desse código há 9 funções, que serão utilizadas para o dimensionamento elétrico. 
Pasta Dados: Armazena as tabelas utilizadas como referência (de acordo com a NBR5410) para os cálculos de dimensionamento elétrico. 
