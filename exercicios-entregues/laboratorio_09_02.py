def melhor_volta(matriz):
    for i in range(len(matriz)):
        for j in matriz[i]:
            j = 0
    return 0

def busca(setor, matriz):
    """ Dada um setor e uma matriz de funcionários de uma empresa, retorna todos os funcionários que pertencem aquele setor.
    string, list -> list
    """
    resultado = []
    for i in range(len(matriz)):
        for j in matriz[i]:
            if(setor == j):
                resultado.append([matriz[i][0], matriz[i][1], matriz[i][3]])
    return resultado

def ordena_por_insercao(lista):
    for i in range(1, len(lista)):
        numero_atual = lista[i]
        j = i - 1
        while j >= 0 and numero_atual < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = numero_atual
    return lista

def melhor_volta(matriz):
    melhores_corredores = []
    corredor = 0
    for i in matriz:
        corredor += 1
        tempo = min(i)
        volta = i.index(tempo) + 1
        melhores_corredores.append([corredor, tempo, volta])
    return melhores_corredores


print(melhor_volta([[88, 60, 62, 26, 93, 13, 74, 9, 54, 1], [43, 64, 72, 35, 2, 65, 97, 7, 57, 84], [95, 69, 76, 94, 53, 8, 75, 96, 31, 44], [36, 98, 16, 71, 59, 99, 19, 30, 46, 100], [18, 58, 49, 89, 37, 14, 82, 66, 51, 77], [85, 87, 17, 50, 67, 90, 63, 47, 22, 101]]))
# print(melhor_volta([[88, 60, 62, 26, 93, 13, 74, 9, 54, 1], [43, 64, 72, 35, 2, 65, 97, 7, 57, 84], [95, 69, 76, 94, 53, 8, 75, 96, 31, 44], [36, 98, 16, 71, 59, 99, 19, 30, 46, 100], [18, 58, 49, 89, 37, 14, 82, 66, 51, 77], [85, 87, 17, 50, 67, 90, 63, 47, 22, 101]]) == (1, 1, 10))
