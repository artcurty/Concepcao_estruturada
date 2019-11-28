import sys
sys.path.append('utils')
from manipulaArquivo import *


def SomaSub1Bit(a,b,cin_):
    c_out = ''
    auxSum = ''
    result = ''
    saida = []    
    if(a == '0' and b == '0' and cin_ == '0'): #000
        auxSum += '0';
        c_out = '0';     
    
    elif(a == '0' and b == '0' and cin_ == '1'): #001
        auxSum += '1';
        c_out = '0';   
    
    elif(a == '0' and b == '1' and cin_ == '0'): #010
        auxSum += '1';
        c_out = '0';  
    
    elif (a == '0' and b == '1' and cin_ == '1'): #011
        auxSum += '0';
        c_out = '1';
    
    elif(a== '1' and b == '0' and cin_ == '0'): #100
        auxSum += '1';
        c_out = '0'; 
    
    elif(a == '1' and b == '0' and cin_ == '1'): #101
        auxSum += '0';
        c_out = '1';            
    
    elif(a == '1' and b == '1' and cin_ == '0'): #110
        auxSum += '0';
        c_out = '1';      
    
    elif(a == '1' and b == '1' and cin_ == '1'): #111
        auxSum += '1';
        c_out = '1';  
    saida = auxSum + c_out   
    return saida

def ColetaVariavel(a,b,cin_):
    c_out = ''
    auxSum = ''
    result = ''
    saida = []
    
    for i in range(len(a)):     
        if(a[i] == '0' and b[i] == '0' and cin_ == '0'): #000
            auxSum += '0';
            c_out = '0';     
        
        elif(a[i] == '0' and b[i] == '0' and cin_ == '1'): #001
            auxSum += '1';
            c_out = '0';   
        
        elif(a[i] == '0' and b[i] == '1' and cin_ == '0'): #010
            auxSum += '1';
            c_out = '0';  
        
        elif (a[i] == '0' and b[i] == '1' and cin_ == '1'): #011
            auxSum += '0';
            c_out = '1';
       
        elif(a[i] == '1' and b[i] == '0' and cin_ == '0'): #100
            auxSum += '1';
            c_out = '0'; 
        
        elif(a[i] == '1' and b[i] == '0' and cin_ == '1'): #101
            auxSum += '0';
            c_out = '1';            
        
        elif(a[i] == '1' and b[i] == '1' and cin_ == '0'): #110
            auxSum += '0';
            c_out = '1';      
        
        elif(a[i] == '1' and b[i] == '1' and cin_ == '1'): #111
            auxSum += '1';
            c_out = '1';  
    saida = auxSum + c_out
    return saida

def SomaSubGoldenModel(lista):
    cin =[]
    A = []
    B = []
    saida = []
    for i in range(len(lista)):  
        cin = lista[i][2:3]
        A = lista[i][:1] 
        B = lista[i][1:2]
        resultado = ColetaVariavel(A,B,cin)
        saida.append(resultado)
    entra_Sainda(lista,saida)

#função que cria a estilização do arquivo de saida
def entra_Sainda(lista, Y):
    entrada_saida = []
    entrada = list(map(lambda x:x.strip(),lista))  #Remove a quebra de linha da primeira lista
    entrada_saida.append("ABcin_SC \n") #Cabeçalho
    for elemA, elemB in zip(entrada, Y):
        entrada_saida.append(elemA +'_'+ elemB+'\n') 
    GeraArquivo('./SOMASUB/GoldenModel/SOMASUB.tv', entrada_saida)

lista = LerArquivo('utils/entrada_somaSub.txt')
listaSaida = SomaSubGoldenModel(lista)
