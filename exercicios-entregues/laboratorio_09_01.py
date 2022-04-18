def multiplica_matriz(matriz, num):
    """ Dada uma matriz e um número, retorna a multiplicação da matriz pelo número.
    list, int -> list
    """
    lista = []
    for i in range(len(matriz)):
        lista.append([])
        for j in range(len(matriz[0])):
            lista[i].append(matriz[i][j] * num)
    return lista

def quem_ligou(telefone, contatos):
    """ Dado um telefone e uma lista de contatos, retorna os dados do contato correspondente aquele número.
    string, list -> list
    """
    contato_achado = []
    for i in contatos:
        if(telefone in i[1]):
            contato_achado.append(i)
    return contato_achado
