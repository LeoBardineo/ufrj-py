def filtraMultiplos(numeros, n):
    """ Dada uma lista de números e um número n,
    itera por meio da lista de números, achando os números que são múltimos do número n,
    e adicionando a uma lista de números múltiplos.
    list, int -> list
    """
    i = 0
    numerosMultiplos = []
    quantidadeNumeros = len(numeros)
    while i < quantidadeNumeros:
        if(numeros[i] % n == 0):
            numerosMultiplos.append(numeros[i])
        i += 1
    return numerosMultiplos

def uppCons(frase):
    """ Dada uma frase, itera por meio dela e
    concatena cada consoante a uma frase em maíusculo, e as outras da forma que estão,
    ao final da iteração, retorna a frase com todas as consoantes em maíusculo.
    str -> str
    """
    i = 0
    tamanhoFrase = len(frase)
    fraseNova = ''
    while i < tamanhoFrase:
        if(not frase[i].lower() in 'aeiouãõáéíóúàèòù'):
            fraseNova += frase[i].upper()
        else:
            fraseNova += frase[i]
        i += 1
    return fraseNova

def posLetra(frase, letra, ocorrencia):
    """ Dada uma frase, uma letra, e um número representando uma ocorrência,
    itera por meio da frase verificando se aquele caractere é igual a letra,
    se for, vai ser adicionado +1 ao contador, e se o contador for igual ao
    número de ocorrência passado, retorna a posição do caractere, caso contrário,
    realiza mais uma iteração realizando as mesmas operações, e retorna -1 ao final da iteração.
    str, str, int -> int
    """
    tamanhoFrase = len(frase)
    contador = 0
    i = 0
    while i != tamanhoFrase:
        if(frase[i] == letra):
            contador += 1
            if(contador == ocorrencia):
                return i
        i += 1
    return -1

def repetidos(numeros):
    """ Dada uma lista de números, itera por meio dessa lista e
    verifica se o número em questão é igual ao número anterior da lista,
    se for, adiciona +1 ao contador, ao final da iteração, retorna esse contador.
    list -> int
    """
    i = 1
    contador = 0
    tamanhoNumeros = len(numeros)
    while i < tamanhoNumeros:
        if(numeros[i] == numeros[i-1]):
            contador += 1
        i += 1
    return contador

def fatorial(numero):
    """ Dado um número, retorna a fatorial desse número, ao
    iterar uma quantidade de número vezes, e multiplicar o número
    em questão pela variável resultado, que armazena o fatorial do número,
    assim iterando de 1 até o número, e a cada iteração realizando a multiplicação,
    para ao final retornar a fatorial do número passado.
    int -> int
    """
    i = 1
    resultado = 1
    while i <= numero:
        resultado *= i
        i += 1
    return resultado

def faltante(listaFaltante):
    """ Dada uma lista de números com um número faltante,
    essa lista faltante é ordenada corretamente e
    é feito uma lista correta com todos os números por meio do range(1, n+1),
    é feito iterações na lista faltante verificando se o número da lista dos faltantes em questão é
    diferente do número da lista correta, e se for, é retornado o número da lista correta que falta na lista faltante.
    Após essas iterações, é retornado o último número da lista faltante + 1.
    list -> int
    """
    listaFaltante.sort()
    n = max(listaFaltante)
    listaCorreta = list(range(1, n+1))
    i = 0
    while i < len(listaFaltante):
        if(listaFaltante[i] != listaCorreta[i]):
            return listaCorreta[i]
        i += 1
    return listaFaltante.pop() + 1
