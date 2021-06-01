from random import randint, seed

def tabuleiro_soma_1(tabuleiro, linha, coluna):
    # concertar os comentários as posições estão erradas provavelmente
    if linha < 8:
        if tabuleiro[linha + 1][coluna] != '*': tabuleiro[linha + 1][coluna] += 1 # topo centro

    if linha > 0:
        if tabuleiro[linha - 1][coluna] != '*': tabuleiro[linha - 1][coluna] += 1 # baixo centro

    if coluna < 8:
        if tabuleiro[linha][coluna + 1] != '*': tabuleiro[linha][coluna + 1] += 1 # direita centro

    if coluna > 0:
        if tabuleiro[linha][coluna - 1] != '*': tabuleiro[linha][coluna - 1] += 1 # esquerda centro

    if linha < 8 and coluna < 8:
        if tabuleiro[linha + 1][coluna + 1] != '*': tabuleiro[linha + 1][coluna + 1] += 1 # topo direita

    if linha < 8 and coluna > 0:
        if tabuleiro[linha + 1][coluna - 1] != '*': tabuleiro[linha + 1][coluna - 1] += 1 # topo esquerda

    if linha > 0 and coluna < 8:
        if tabuleiro[linha - 1][coluna + 1] != '*': tabuleiro[linha - 1][coluna + 1] += 1 # baixo direita

    if linha > 0 and coluna > 0:
        if tabuleiro[linha - 1][coluna - 1] != '*': tabuleiro[linha - 1][coluna - 1] += 1 # baixo esquerda

def printar_tabuleiro(tabuleiro):
    colors = {
        '*': '\033[1m\033[31m', # bold and red
        0: '\033[39m', # white
        1: '\033[34m', # blue
        2: '\033[32m', # green
        3: '\033[33m', # orange
        4: '\033[35m', # yellow
        5: '\033[36m', # cyan
        6: '\033[36m', # cyan
        7: '\033[30m', # gray
    }
    for i in range(len(tabuleiro)):
        linha = ''
        for j in tabuleiro[i]:
            j = colors[j] + str(j) + '\033[0m'
            j = str(j)
            linha += j + ' '
        print(linha)

def gerar_tabuleiro():
    tabuleiro = []
    for i in range(9):
        tabuleiro.append([0] * 9)
    return tabuleiro

def gerar_bombas(tabuleiro, num_bombas):
    seed(9001)
    bombas = []
    for i in range(num_bombas):
        linha = randint(0, 8)
        coluna = randint(0, 8)
        while [linha, coluna] in bombas:
            linha = randint(0, 8)
            coluna = randint(0, 8)
        tabuleiro[linha][coluna] = '*'
        bombas.append([linha, coluna])
        tabuleiro_soma_1(tabuleiro, linha, coluna)
    return bombas

def printar_tabuleiro_normal():
    for i in range(9):
        linha = ''
        for j in range(9):
            linha += '. '
        print(linha)

def main():
    tabuleiro = gerar_tabuleiro()
    bombas = gerar_bombas(tabuleiro, 5)
    printar_tabuleiro(tabuleiro)

if __name__ == '__main__':
    main()
