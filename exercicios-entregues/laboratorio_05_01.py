# Retorna a quantidade de palavras de uma frase
# string -> int
def quant_palavras(frase):
    return len(frase.strip().split(' '))

# Retorna o número de frases em um texto, sendo
# cada frase podendo ser terminada por
# um ponto, exclamação, ponto de interrogação e reticências
# string -> int
def conta_frases(frase):
    count = frase.count('...')
    frase = frase.replace('...','')
    count += frase.count('.') + frase.count('!') + frase.count('?')
    return count

# Retorna uma lista intercalando os elementos das listas lista1 e lista2
# list, list -> list
def intercala(lista1, lista2):
    return [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]

# Dada uma frase, retorna a frase substituindo caracteres de pontuação em espaço.
# string -> string
def retira_pontuacao(frase):
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ')

# Dada uma frase, retorna ela com a posição das palavras invertidas
# string -> string
def inverte(frase):
    frase = retira_pontuacao(frase).lower()
    frase = frase.split(' ')[::-1]
    return str.strip(str.join(' ', frase))

# Dado dois números inteiros, é feito uma pirãmida de números,
# que é uma sequência de números sendo o primeiro valor o primeiro e o último elemento
# da sequência, cada valor tendo uma diferença absoluta de um ao vizinho da esquerda ou direita,
# o maior número, o segundo argumento, estará no meio da sequência
#   int, int -> list
def piramide_num(n1, n2):
    if(n1 > n2):
        lista = list(range(n1, n2 - 1, -1))
    else:
        lista = list(range(n1, n2 + 1,))
    lista += lista[-2::-1]
    return lista

# Dada as medidas de um colchão, A, B e C, em uma lista,
# retorna se é possível passa-lo por uma porta de altura H e largura L
# lista, int, int -> boolean
def colchao(medidas, H, L):
    B, C = medidas[1], medidas[2]
    if((B > H and B > L) and (C > H and C > L)):
        return False
    return True


print(colchao([25,200,220], 200, 100))
