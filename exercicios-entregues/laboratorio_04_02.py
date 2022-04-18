import math

def SIGA(t):
    '''Recebe uma tupla contendo respectivamente o nome e três notas, e é calculado
       sua média com uma casa decimal, se a média for maior que 7, será retornado
       uma tupla com seu nome, sua média, 'aprovado' e 'Parabéns!', em outros casos
       retornará seu nome, sua média, e se a média for maior que 5, retornará junto 'aprovado',
       e se não for, retornará junto 'reprovado'.
       tupla -> tupla
    '''
    nome, n1, n2, n3 = t
    media = round((n1 + n2 + n3) / 3, 1)
    if(media >= 7):
        return nome, media, 'aprovado', 'Parabéns!'
    elif(media >=5):
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    return nome, media, situacao

def quadrante(angulos, graus):
    '''Recebe um ângulo e um booleano indicando se o ângulo passado foi em graus (True) ou em radianos (False),
       e retorna em qual quadrante o ângulo se encontra, entre 1 e 4.
       int, bool -> int
    '''
    if(graus):
        if(angulos <= 90):
            quad = 1
        elif(angulos <= 180):
            quad = 2
        elif(angulos <= 270):
            quad = 3
        elif(angulos <= 360):
            quad = 4
        else:
            angulos = angulos % 360
            quad = quadrante(angulos, True)
    else:
        if(angulos <= math.pi/2):
            quad = 1
        elif(angulos <= math.pi):
            quad = 2
        elif(angulos <= (3 * math.pi)/2):
            quad = 3
        elif(angulos <= 2 * math.pi):
            quad = 4
    return quad
