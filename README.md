#### Autodimensionamento elétrico residencial 
*Autores:* Daniel Bravin, Emelyn Alves, Gustavo Matos, José David Alves.  

#### Introdução: 
O trabalho técnico referente ao dimensionamento elétrico costuma ocorrer por análise manual de dados. Essa análise geralmente é realizada com base no número de circuitos, métodos de instalação e outras condições identificadas na planta elétrica do local. Por isso, quando não realizada por profissionais a instalação está passível à riscos, que comprometem a segurança do local e da própria instalação. Com o objetivo de evitar possíveis acidentes ocasionados por desinstrução ou falha humana e facilitar o cálculo de dimensionamento elétrico, pretendemos criar um código em python, que utilize a bilioteca Pandas, para analizar as variáveis necessárias para o dimesionamento, compara-las com a Norma Regulamentadora vigente (NBR5410) e retornar as especificações do disjuntor e da seção transversal do fio a serem utilizados.

#### Sobre a ANBT NBR5410:
A ABNT NBR5410 é uma Norma Brasileira elaborada pelo Comitê Brasileiro de Eletricidade, pela Comissão de Estudo de Intalações Elétricas de Baixa Tensão, que vigora desde 31 de março de 2005. O objetivo dessa norma é garantir: segurança de pessoas e animais, bom funcionamento das instalações elétricas e conservação de bens.  A 
A NBR5410 disponibiliza uma série de tabelas com importantes dados para o correto dimensionamento elétrico, como tabelas de corrente máxima até o aquecimento de uma determinada seção. Essas tabelas se relacionam entre si, de forma que, por exemplo, uma temperatura mais alta ou mais baixa que o normal que um fio possa estar exposto faz com que a corrente que o fio suporta, sem aquecer, aumente ou diminua em função em um fator de correção determinado em uma outra tabela que é aplicado na tabela referente a corrente limite e seção. Ou seja, os dados se relacionam diretamente e uma pequena alteração de uma variável muda completamente o resultado final, o que gera um grande risco por falhas humanas. 

Nosso programa em si, é dividido em duas principais partes: 
  - Interface: Será a face do nosso programa e a responsável por coletar os dados do esquema elétrico do usuário. Utilizaremos o site Streamlit para criá-la. Pretendemos fazer uma interface acessível e intuitiva. 
  - Análise de dados: Usando as variáveis disponibilizadas pelo usuário, relacionará estas com a NBR5410. Esta comparação, nos indicará qual será o disjuntor e a seção transversal do condutor mais indicados para o tipo de instalação especificado. 

#### O QUE JÁ DESENVOLVEMOS E COMO USAR O CÓDIGO):
Até o momento, já conseguimos desenvolver um código funcional que recebe uma potência, uma tensão, um método de instalação, um número de circuitos no mesmo eletrodulto e uma temperatura no ambiente para conseguir fazer o dimensionamento com base nesses diversos dados. Isso ocorre por meio da biblioteca Pandas. Baixando a pasta "Programa" é possível fazer uso do que já desenvolvemos até o momento. O arquivo princípal é o Autodimencionamento.ipynb", ele ainda não está no formato python. Entrando nesse notebook, o usuário pode alterar a potência(P), a tensão(V) o número de circuitos no mesmo eletrodulto e a temperatura do ambiente para descobrir o disjuntor e a seção nominal correta do fio para a instalação dessa carga. Ainda não é possível entregar claramente o método e o isolamento do fio, mas depois que a interface for desenvolvida será possível fazer isso facilemnte.

#### A SER DESENVOLDIDO:

##### INTERFACE (Front-end):
![image](https://github.com/emelyn23017/autodimensionamentoeletrico/assets/135053736/968dcd4e-403c-4dc9-87de-beb39a8ca194)

A imagem acima nos mostra uma base de iriamos trabalhar no nosso layout final, contudo devido a nova ferramenta que começamos a usar o "Streamlit" nosso desig teve de ser alterado em partes. 
Como dito estamos usando o Streamlit, ele permite criar uma página web e altera-lá diretamente pelo github. Algumas das configurações são um tanto limitantes mas ele nos permite trabalhar de maneira bem simples e rapida.
O código que ainda passa por desenvolvimento carece de polimento e organização, contudo se mostra funcional. 

##### ANÁLISE (Back-end):
Ainda é preciso organizar corretamente as funções em um arquivo definitivo em .py e comentar o código.

Observações do James: *Apagar depois* 
Melhorar a descrição 
Link com resumo da NBR5410
Link do streamit não abriu - Adicionar o link certo no readme 
Nome dos Autores no Readme
Código não foi rodado: ft não estava definida
