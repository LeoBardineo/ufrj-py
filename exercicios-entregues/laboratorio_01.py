def areaRetangulo(largura, altura):
    '''Cálcula a área de um retângulo'''
    return largura * altura

def areaCubo(c):
    '''Cálcula a área da superfície de um cubo'''
    return c ** 2 * 6

def areaCoroa(r1, r2):
    '''Cálcula a área da coroa circular, sendo r1 > r2 e pi = 3.14'''
    return 3.14 * (r1 ** 2 - r2 ** 2)

def mediaSimples(n1, n2):
    '''Cálcula a média de dois números'''
    return (n1 + n2) / 2

def ordenada(a, b, c, x):
    '''Cálcula a ordenada de uma função do segundo grau'''
    return a * x ** 2 + b * x + c

def mediaPonderada(n1, p1, n2, p2):
    '''Cálcula a média ponderada de dois números com seus respectivos pesos,
    coloque em ordem o número e o peso do número em seguida ao chamar a função.
    Exemplo: mediaPonderada(número 1, peso 1, número 2, peso 2)'''
    return (n1 * p1 + n2 * p2) / (p1 + p2)

def erroAproximacao(q, n):
    '''Cálcula o erro de aproximação, a diferença entre a aproximação de um valor e seu valor real'''
    return 1 / (1 - q) - ((q ** n - 1) / (q - 1))

def gorjeta(conta):
    '''Cálcula a gorjeta de um garçom, sendo considerado 10% do valor da conta'''
    return conta * 0.1

def gorjetaLegislacao(conta, porcentagem):
    '''Cálcula a gorjeta do garçom segundo a legislação informada pelo usuário,
    porcentagem em %, exemplo: 10% = 10'''
    return conta * porcentagem / 100

def saldoFinal(saldoInicial, numeroMeses, jurosMensal):
    '''Calcula o saldo final de uma conta, dado o saldo inicial, número de meses e
    a taxa de juros mensal em %, exemplo: 10% = 10'''
    return saldoInicial * (1 + (jurosMensal / 100) * numeroMeses)

def distancia(velocidadeCorrenteza, larguraRio, velocidadeBarco):
    '''Calcula o arrasto que uma correnteza aplica a um barco que se move perpendicular à correnteza'''
    return velocidadeCorrenteza * larguraRio / velocidadeBarco
