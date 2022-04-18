def absoluto(x):
    ''' Retorna o valor absoluto de um número X fornecido.
        int -> int ou float -> float ou complex -> float
    '''
    if(type(x) == complex):
        return (x.real ** 2 + x.imag ** 2) ** (1/2)
    else:
        if(x >= 0):
            return x
        else:
            return x * -1

def delta(a, b, c):
  return b ** 2 - 4 * a * c

def quantidadeRaizes(a, b, c):
    ''' Retorna a quantidade de raízes de uma função do segundo grau, dada os coeficientes a, b, c.
        int, int, int -> string
    '''
    if(delta(a, b, c) > 0):
        return 'Duas'
    elif(delta(a, b, c) == 0):
        return 'Uma'
    else:
        return 'Nenhuma'

def spamTexto(texto, n):
    ''' Retorna um texto repetido n vezes.
        string, int -> string
    '''
    return texto * n

def dataFormatada(d, m, a):
    ''' Retorna uma data no formato "DD/MM/AAAA"
        int, int, int -> string
    '''
    return str(d) + '/' + str(m) + '/' + str(a)

def funcaoGrafico(x):
    ''' Retorna y baseado no gráfico apresentado na questão 5.
        int -> int
    '''
    if(x <= 2 and x > 0):
        return x
    elif(x <= 3.5):
        return 2
    elif(x <= 5):
        return 3
    else:
        return x ** 2 - 10 * x + 28

def descontoINSS(bruto):
    ''' Retorna a taxa de desconto do INSS ao salario bruto.
        float -> float
    '''
    if(bruto <= 2000):
        return 0.06
    elif(bruto <= 3000):
        return 0.08
    else:
        return 0.1

def descontoIR(bruto):
    ''' Retorna a taxa de desconto do IR ao salario bruto.
        float -> float
    '''
    if(bruto <= 2500):
        return 0.11
    elif(bruto <= 5000):
        return 0.15
    else:
        return 0.22

def salarioLiquido(bruto):
    ''' Retorna o salario líquido ao tirar os descontos do INSS e do IR do bruto passado como argumento.
        float -> float
    '''
    return bruto - (bruto * descontoINSS(bruto) + bruto * descontoIR(bruto))
