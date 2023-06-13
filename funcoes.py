import pandas as pd
import numpy as np

tabela_disjuntores = pd.read_excel("Dados\DISJUNTORES.xlsx")
tabela_agrupamento = pd.read_excel("Dados\AGRUPAMENTO.xlsx")
tabela_temperatura = pd.read_excel("Dados\TEMPERATURA.xlsx")

def condicao_de_instalacao(isolamento,local):
    if isolamento == "PVC" and (local == "Teto" or local =="Parede"):
       condicao = 'PVCAMBIENTE'
    if isolamento == "PVC" and local == "Solo":
       condicao = 'PVCSOLO'
    if (isolamento == "EPR" or isolamento == "XLPE") and (local == "Teto" or local =="Parede"):
       condicao = 'EPRAMBIENTE'
    if (isolamento == "EPR" or isolamento == "XLPE") and (local == "Solo"):
       condicao = 'EPRSOLO'
    return condicao

def tabela_a_ser_usada(isolamento):
    if isolamento == "PVC":
        tabela_usada = "DOIS_COBRE_PVC.xlsx" 
    if isolamento == "XLPE" or isolamento == "EPR":
        tabela_usada = "DOIS_COBRE_EPR_XLPE.xlsx" 
    return pd.read_excel(tabela_usada)


def disjuntor_inicial(P, V, disjuntores = tabela_disjuntores)
    """
    args:
        P: Potência 
        V: Tensão
        disjuntores: A tabela de disjuntores a ser usada na análise (opcional)
    returns: 
        O disjuntor adequado para as condições especificadas.
    """
    I = P/V
    for linha in disjuntores.itertuples():
        coluna = "DISJUNTOR"
        if getattr(linha, coluna) > I:
            return getattr(linha, coluna)



# def dimensionar(tabela, metodo = 'B1', Bitola_min = 2.5, FT = 0.5, P = 1550, V = 220):
def fator_temperatura(condicao, temperatura_ambiente, temperaturas = tabela_temperatura):
    """
    args:
        condicao: Condição de instalação
        temperatura_ambiente: Temperatura média do amibiente. 
        temperaturas: A tabela de temperatura a ser usada na análise.
    returns: 
        Fator de temperatura.
    """
    for temperatura in temperaturas.itertuples():
        temperatura_usada = getattr(temperatura, condicao)
        if temperatura_usada > temperatura_ambiente:
            return temperatura_usada


def fator_agrupamento(n_circuitos, metodo, agrupamentos = tabela_agrupamento):
    """
    args:
        n_circuitos: Número de circuitos a serem considerados.
        Método: Método de instalação usado.
        agrupamentos: A tabela de agrupamento a ser usada na análise.
    returns: 
        Fator de temperatura.
    """
    return agrupamentos.loc[n_circuitos+1][metodo]

def fator_correcao(agrupamento, temperatura):
    """
    args:
        agrupamento: O fator de agrupamento.
        temperatura: O fator de temperatura
    returns: 
        Fator de agrupamento.
    """
    return agrupamento*temperatura

def bitola(disjuntor, bitola_min, metodo, correcao, isolamento):
    """
    args:
        disjuntor: 
        bitola_min: 
        metodo: Método de instalação
        correcao: 
        isolamento:
    returns: 
        finais: lista com disjuntor final e tamanho ideal de bitola.
    """
    tabela = tabela_a_ser_usada(isolamento)
    bit = 'SEÇÃO'
    I_max = correcao * tabela[metodo].values
    fios = tabela[bit].values
    finais = []
    for valor in I_max:
        if valor > disjuntor:
            finais.append(valor)
            break
    for valor in fios:
        if valor >= bitola_min:
            finais.append(valor)
            break
    return finais


if __name__ == "__main__":
    
    P=1550
    V=220
    print(disjuntor_inicial(P,V))
    fator_temperatura('PVCSOLO', 30)