import sys
sys.path.append('utils')
from manipulaArquivo import *

#Verifica as condições do inversor
def InvGoldenModel(lista):
    for i in range(len(lista)):
        lista[i]=lista[i].replace('0','x')
        lista[i]=lista[i].replace('1','0')
        lista[i]=lista[i].replace('x','1')
        lista 
    return lista

#função que cria a estilização do arquivo de saida
def entra_Sainda(entrada,saida):
    entrada_saida = []
    entrada = list(map(lambda x:x.strip(),entrada)) 
    for elemA, elemB in zip(entrada, saida):
        entrada_saida.append(elemA + '_' + elemB) 
    GeraArquivo('./inv/GoldenModel/inv.tv', entrada_saida)


listaEntradas4Bit = InvGoldenModel(LerArquivo('utils/combina_binario.txt'));

listaEntrada = LerArquivo('utils/combina_binario.txt');  
entra_Sainda(listaEntrada,listaEntradas4Bit)

