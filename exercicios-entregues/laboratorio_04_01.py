# Concatena as strings a e b no formato abba.
# str, str -> str
def concatenacao(a, b):
    return a + b + b + a

# Fatia a string até a posição i, concatena com o caractere x,
# e concatena com a string fatiada até o final, sem o caractere da posição i,
# retornando assim, a string com o caractere x na posição i.
# string, string, int -> string
def substitui(s,x,i):
    return s[:i] + x + s[i+1:]

# Retorna a string com ela no meio dela mesma.
# É pego metade do comprimento da string e fatiado a string até essa posição,
# para então concatenar com a string e depois concatenar com a string fatiada até o final.
# str -> str
def recursiva(s):
    metadeString = len(s) // 2
    return s[:metadeString] + s + s[metadeString:]

# Retorna a string com # (hashtag) no  início, meio e final dela.
# É colocado a hashtag no começo, concatenado a string até o meio dela, concatenado outra hashtag,
# concatenado a string até o final dela, e então concatenado outra hashtag
# str-> str
def hashtag(s):
    metadeString = len(s) // 2
    return '#' + s[:metadeString] + '#' + s[metadeString:] + '#'

# É calculado a quantidade de dias de data1 e data2, e então retornado a diferença entre elas,
# calculando assim a diferença de dias entre as duas datas
# str, str -> int
def diff_datas(data1,data2):
    dias1 = int(data1[0:2]) + int(data1[3:5]) * 30 + int(data1[6:]) * 365
    dias2 = int(data2[0:2]) + int(data2[3:5]) * 30 + int(data2[6:]) * 365
    return dias2 - dias1

# Filtra a tupla t e retorna seus elementos pares
# tuple -> tuple
def filtra_pares(t):
    tuplaPares = ()

    if(t[0] % 2 == 0):
        tuplaPares = (t[0],)

    if(t[1] % 2 == 0):
        tuplaPares += (t[1],)

    if(t[2] % 2 == 0):
        tuplaPares += (t[2],)

    if(t[3] % 2 == 0):
        tuplaPares += (t[3],)

    return tuplaPares

def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    return not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2)
