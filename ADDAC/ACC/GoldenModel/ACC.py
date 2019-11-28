import sys
sys.path.append('utils')
from manipulaArquivo import *

   
def AccGoldenModel(lista):
    resultadoS = []
    
    for i in range(len(lista)):  
        if lista[i][1:2] == '0' and i == 0:#clk = 0
            resultadoS.append("x\n");
        elif lista[i-1][1:2] == '0' and lista[i][1:2] == '1':
            resultadoS.append(lista[i][:1]+'\n');
        else: 
            resultadoS.append(resultadoS[-1]);
    entra_Sainda(lista,resultadoS)

#função que cria a estilização do arquivo de saida
def entra_Sainda(lista, Y):
    entrada_saida = []
    entrada = list(map(lambda x:x.strip(),lista))  #Remove a quebra de linha da primeira lista
    # entrada_saida.append("A_Clk_S \n") #Cabeçalho
    for elemA, elemB in zip(entrada, Y):
        entrada_saida.append('_'.join(elemA) +'_'+ elemB) 
    GeraArquivo('./ACC/GoldenModel/ACC.tv', entrada_saida)

lista = LerArquivo('utils/entrada_acc.txt')
listaSaida = AccGoldenModel(lista)