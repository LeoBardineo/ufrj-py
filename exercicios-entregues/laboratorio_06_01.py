# Dada uma frase, palavra e posição,
# retorna, caso haja a palavra na frase, a frase com a primeira ocorrência da palavra em maiúscula
# caso não haja, retorna a frase com a palavra na posição dada, sendo cada palavra uma posição
# str, str, int -> str
def altera_frase(frase, palavra, posicao):
    listaFrase = frase.split(' ')
    if(palavra in listaFrase):
        return frase.replace(palavra, palavra.upper(), 1)
    else:
        listaFrase.insert(posicao, palavra)
        return ' '.join(listaFrase).strip()

# Dada uma lista no formato [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]],
# sendo cada elemento da lista um jogo, e cada terceiro elemento de cada jogo o número de faltas de cada time,
# retorna o total de faltas do campeonato
# list -> int
def faltas(lista):
	return lista[0][2][0] + lista[0][2][1] + lista[1][2][0] + lista[1][2][1] + lista[2][2][0] + lista[2][2][1]

# Dada uma lista de números inteiros e um número inteiro n,
# retorna a lista com o n e ordenada crescentemente
# list, int -> list
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

# Dada uma lista e um número inteiro n,
# retorna todos da lista que são maiores que n
# list, int -> list
def maiores(lista, n):
    lista.append(n)
    lista.sort()
    indice = lista.index(n)
    counter = lista.count(n)
    return lista[indice + counter:]

# Dada uma lista de notas de uma turma,
# retorna uma lista ordenada com as notas que ficaram acima da média
# list -> list
def acima_da_media(lista):
    media = sum(lista) / len(lista)
    return maiores(lista, media)

# Dada uma lista não vazia de números,
# retorna True ou False se a lista for ou não ordenada,
# e crescente, decrescente, ou desordenada se a lista for
# crescente, decrescente ou desordenada respectivamente
# list -> bool, string
def eh_ordenada(lista):
    listaSorteada = lista.copy()
    listaSorteada.sort()
    if (lista == listaSorteada):
        sortBool = True
        ordem = 'crescente'
        return sortBool, ordem
    listaSorteada.reverse()
    if (lista == listaSorteada):
        sortBool = True
        ordem = 'decrescente'
        return sortBool, ordem
    return False, 'desordenada'
