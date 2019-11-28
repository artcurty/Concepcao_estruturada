import sys
sys.path.append('utils')
from manipulaArquivo import *

   
def MuxGoldenModel(lista):
    resultadoY = []
    for i in range(len(lista)):        
         if lista[i][:1] == '0': #Se S for 
             resultadoY.append(lista[i][1:2]+'\n') #A
         else:
             resultadoY.append(lista[i][2:3]+'\n') #B   
    entra_Sainda(lista, resultadoY)

#função que cria a estilização do arquivo de saida
def entra_Sainda(lista, Y):
    entrada_saida = []
    entrada = list(map(lambda x:x.strip(),lista))  #Remove a quebra de linha da primeira lista
    # entrada_saida.append(" S_A_B_Y \n") #Cabeçalho
    for elemA, elemB in zip(entrada, Y):
        entrada_saida.append(elemA +'_'+ elemB) 
    GeraArquivo('./MUX/GoldenModel/MUX.tv', entrada_saida)

lista = LerArquivo('utils/mux_entradas.txt')
listaSaida = MuxGoldenModel(lista)
