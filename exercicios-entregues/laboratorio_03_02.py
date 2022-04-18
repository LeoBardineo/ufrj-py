# V = 3, E = 1, (E) > Gols, (E e Gols) > E
# Retorna qual time, Cormengo e Flaminthians, foi vencedor de um campeonato de futebol
# A escolha do vencedor é feito ao calcular a quantidade de pontos
# As vitórias de um time (cv e fv) vale 3 pontos, os empates (ce, fe) 1 ponto
# E o saldo de gols (cs, fs) serve para caso haja empate
# Se mesmo assim o empate persistir, então retornará empate
# int, int, int, int, int, int -> string
def classificacao(cv, ce, cs, fv, fe, fs):
    if(cv * 3 + ce > fv * 3 + fe):
        return 'Cormengo'
    elif(cv * 3 + ce < fv * 3 + fe):
        return 'Flaminthians'
    elif(cs > fs):
        return 'Cormengo'
    elif(cs < fs):
        return 'Flaminthians'
    else:
        return 'Empate'

# Retorna se a quantidade comprada de folhas pela Diretora é suficiente ou não
# É baseada nos seguintes parâmetros passados pelo usuário:
# número de competidores, folhas de papel compradas e quantas folhas cada competidor deve receber
# int, int, int -> string
def avioes(c, p_compr, p_compet):
    if(c * p_compet > p_compr):
        return 'Insuficiente'
    else:
        return 'Suficiente'
