def soma_serie(n):
    """ Dado um número n de termos,
    realiza e retorna a somatório de n termos da fórmula (-1)^n / 2n + 1, sendo n o enésimo termo.
    int -> float
    """
    resultado = 0
    for i in range(n + 1):
        calc = (-1) ** i / (2 * i + 1)
        resultado += calc
    return resultado

from math import pi, fabs

def erro_soma_serie():
    """ Enquanto o módulo da diferença do somatório de i termos e a soma dos termos infinitos, que converge para pi/4,
    for maior que 0.01, adiciona +1 ao número de termos i, para que então, ao achar uma diferença na qual der menor que 0.01,
    retorne o número de termos i para chegar a esse resultado, e a soma de termos com esse número de termos i.
    int -> float
    """
    i = 0
    while fabs(soma_serie(i) - pi/4) > 0.01:
        i += 1
    return i, soma_serie(i)

print(erro_soma_serie())

def buscaDados(contatos, nome):
    """Dada uma lista de contatos e um nome,
    procura pelo nome na lista de contatos,
    iterando pela lista de contatos e
    verificando se o nome passado existe na string do nome do contato,
    caso exista, é adicionado o contato a uma lista, e ao final da iteração,
    retorna a lista.
    list, str -> list
    """
    contatosAchados = []
    for i in contatos:
        if(nome.lower() in i[0].lower()):
            contatosAchados.append(i)
    return contatosAchados
