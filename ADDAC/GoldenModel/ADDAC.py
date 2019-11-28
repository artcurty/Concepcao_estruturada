import sys
sys.path.append('utils')
sys.path.append('SOMASUB/GoldenModel')
from manipulaArquivo import *
from SOMASUB import *


def Inv(A):   
    if A == '1':
       A = '0'
    else:
       A = '1'
    return(A)

def AddacGoldenModel(lista):
    resultado = []
    for i in range(len(lista)):  
        sel0 = lista[i][:1]
        sel1 = lista[i][1:2]
        A    = lista[i][2:3]
        ACC  = '0'        
        if (sel0=='0' and sel1=='0'):
            resultado.append(A)
        elif(sel0=='0' and sel1=='1'):
            SomaSub1Bit(A, ACC, sel0)
        elif(sel0=='1' and sel1=='0'):
            A = Inv(A)
            resultado.append(A)            
        else:
            A = Inv(A)            
            S = SomaSub1Bit(A, ACC, sel0)        
            resultado.append(S)
    entra_Sainda(lista,resultado)


#função que cria a estilização do arquivo de saida
def entra_Sainda(lista, Y):
    entrada_saida = []
    entrada = list(map(lambda x:x.strip(),lista))  #Remove a quebra de linha da primeira lista
    entrada_saida.append("Sl0_Sel1_A_Saida\n") #Cabeçalho
    for elemA, elemB in zip(entrada, Y):
        entrada_saida.append(elemA +'_'+ elemB+'\n') 
    GeraArquivo('./GoldenModel/ADDAC.tv', entrada_saida)


lista_entrada =  list(map(lambda x:x.strip(),LerArquivo('utils/entrada_addac.txt')))
# print(lista_entrada)

AddacGoldenModel(lista_entrada)







