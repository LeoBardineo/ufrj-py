def soma_fatorial(n):
    """ Dado um número n, retorna a soma dos fatoriais de 1 a n.
    int -> int
	"""
    resultado = 0
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        resultado += fatorial
    return resultado

def qtd_divisores(n):
    """ Dado um número n, retorna a quantidade de divisores desse número.
    int -> int
    """
    count = 0
    for i in range(1, n + 1):
        if(not n % i):
            count += 1
    return count

def primo(n):
    """ Dado um número n, retorna se ele é primo ou não.
    int -> boolean
    """
    if(n <= 1):
        return False
    for i in range(2, n):
        if(not n % i):
            return False
    return True

def soma_h(n):
    """ Dado um número de termos n, retorna a soma de 1/i com n termos, sendo i o enésimo termo.
    int -> float
    """
    resultado = 0
    for i in range(1, n + 1):
        divisao = 1/i
        resultado += divisao
    return round(resultado, 2)

def soma():
    """ Realiza a soma apresentada de 10/1! - 9/2! + 8/3! - 7/4! + ... - 1/10!, e retorna seu resultado.
    A função não apresenta entradas e retorna um float, 6.59
    """
    n = 10
    resultado = 0
    sinal = 1
    for i in range(1, n+1):
        fatorial = 1
        for j in range(1, i+1):
            fatorial *= j
        if(not i % 2):
            sinal = -1
        else:
            sinal = 1
        s = ((n+1 - i) / fatorial) * sinal
        resultado += s
    return round(resultado, 2)

def lingua_p(palavra):
    """ Dado uma string palavra, retorna ela na lingua do P,
    que consiste na mesma palavra porém com um p antes e depois de cada vogal.
    string -> string
    """
    resultado = ''
    for i in palavra:
        if i.lower() in 'aeiouáéíóúãõ': # isso aqui seria tão melhor em regex
            resultado += i + 'p' + i
        else:
            resultado += i
    return resultado
