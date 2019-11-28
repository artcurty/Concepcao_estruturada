#função pra ler arquivo de entrada
def LerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    lista_4_bit = []
    linhaBinario = arquivo.readlines()
    for linha in linhaBinario :
        lista_4_bit.append(linha)
    arquivo.close()
    return lista_4_bit

#função para escrever em arquivo
def GeraArquivo(local,conteudo):
    arquivo = open(local, 'w')   
    arquivo.writelines(conteudo)
    arquivo.close()


