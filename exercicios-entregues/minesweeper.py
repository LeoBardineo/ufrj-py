from random import randint, seed

# Funções de validação

def validar_nao_vazio(entrada):
    """ Valida se entrada não é vazia, e se for, retorna um texto de erro.
    str -> str
    """
    if not entrada:
        return 'Entrada vazia. Digite algo.\n'

def validar_numero(txt):
    """ Valida se o texto é um número, e se não for, retorna um texto de erro.
    str -> str
    """
    if not txt.isnumeric():
        return 'O texto digitado não é numérico.\n'

def validar_in_range(min, max, num):
    """ Valida se o número está entre o mínimo e o máxmio, e se não estiver, retorna um texto de erro.
    int, int, int -> str
    """
    if num < min or num > max:
        return 'Número digitado fora do alcance. Mínimo: ' + str(min) + ', máximo: ' + str(max) + '.\n'

def validar_resposta(resposta):
    """ Valida se a resposta é sim, sim, n, nao ou não, e se não for, recursivamente pede novamente a entrada.
    str -> str
    """
    if not resposta.lower() in ['s', 'sim', 'n', 'nao', 'não']:
        resposta = input('Resposta inválida. Digite "S" / "Sim", ou "N" / "Nao" / "Não". ')
        return validar_resposta(resposta)
    else:
        return resposta

def validar_jogada(jogadas, linha, coluna):
    """ Valida se a jogada já foi feita, e se já foi feita, imprime uma mensagem dizendo que já foi realizada.
    list, int, int -> None
    """
    if [linha, coluna] in jogadas:
        print('Você já realizou essa jogada.')
    else:
        jogadas.append([linha, coluna])

# Geração do tabuleiro e das bombas

def gerar_tabuleiro():
    """ Gera um tabuleiro novo, uma matriz com 9 linhas e 9 colunas, totalizando 81 posições.
    None -> list
    """
    tabuleiro = []
    for i in range(9):
        tabuleiro.append([0] * 9)
    return tabuleiro

def gerar_bombas(tabuleiro, num_bombas):
    """ Adiciona num_bombas bombas em posições aleatórias no tabuleiro, e retorna as posições das bombas.
    list, int -> list
    """
    # Se quiser testar, só tirar o comentário da próxima linha:
    # seed(9001)
    # a aleatoriedade perde sua propriedade e gera o seguinte tabuleiro:
    #   1 2 3 4 5 6 7 8 9
    # 1 0 0 0 1 * 1 0 1 1
    # 2 0 0 0 1 1 1 0 1 *
    # 3 0 0 1 1 1 0 0 1 1
    # 4 1 1 3 * 2 0 0 1 1
    # 5 1 * 3 * 2 0 0 1 *
    # 6 1 1 2 1 1 0 0 1 1
    # 7 0 1 2 2 1 1 1 1 0
    # 8 0 1 * * 2 2 * 1 0
    # 9 0 1 2 2 2 * 2 1 0
    bombas = []
    for i in range(num_bombas):
        linha = randint(0, 8)
        coluna = randint(0, 8)
        while [linha, coluna] in bombas:
            linha = randint(0, 8)
            coluna = randint(0, 8)
        tabuleiro[linha][coluna] = 'm'
        bombas.append([linha, coluna])
        tabuleiro_soma_1(tabuleiro, linha, coluna)
    return bombas

def tabuleiro_soma_1(tabuleiro, linha, coluna):
    """ Adiciona +1 aos arredores da posição de linha "linha" e coluna "coluna",
    sempre verificando se a posição a ser adicionada não passa do tabuleiro e se
    a posição a ser adicionada não é uma bomba.
    list, int, int -> None
    """

    if linha < 8:
        if tabuleiro[linha + 1][coluna] != 'm': tabuleiro[linha + 1][coluna] += 1 # baixo centro

    if linha > 0:
        if tabuleiro[linha - 1][coluna] != 'm': tabuleiro[linha - 1][coluna] += 1 # topo centro

    if coluna < 8:
        if tabuleiro[linha][coluna + 1] != 'm': tabuleiro[linha][coluna + 1] += 1 # direita centro

    if coluna > 0:
        if tabuleiro[linha][coluna - 1] != 'm': tabuleiro[linha][coluna - 1] += 1 # esquerda centro

    if linha < 8 and coluna < 8:
        if tabuleiro[linha + 1][coluna + 1] != 'm': tabuleiro[linha + 1][coluna + 1] += 1 # baixo direita

    if linha < 8 and coluna > 0:
        if tabuleiro[linha + 1][coluna - 1] != 'm': tabuleiro[linha + 1][coluna - 1] += 1 # baixo esquerda

    if linha > 0 and coluna < 8:
        if tabuleiro[linha - 1][coluna + 1] != 'm': tabuleiro[linha - 1][coluna + 1] += 1 # topo direita

    if linha > 0 and coluna > 0:
        if tabuleiro[linha - 1][coluna - 1] != 'm': tabuleiro[linha - 1][coluna - 1] += 1 # topo esquerda

# Funções apenas para imprimir o tabuleiro

def printar_tabuleiro_inteiro(tabuleiro):
    """ Imprime o tabuleiro formatada corretamente,
    indicando as posições para auxiliar o usuário a escolher a posição corretamente.
    list -> None
    """
    print('\n    1 2 3 4 5 6 7 8 9')
    print('   ' + '―' * 18)
    count = 1
    for i in range(len(tabuleiro)):
        linha = str(count) + ' | '
        for j in tabuleiro[i]:
            j = str(j)
            linha += j + ' '
        count += 1
        print(linha)
    print('')

def printar_tabuleiro_apos_jogada(tabuleiro_final, jogadas):
    """ Após uma série de jogadas que foram feitas,
    imprime na tela um tabuleiro com pontinhos nas posições que não foram reveladas,
    e o número correspondente ao tabuleiro que já foi gerado nas posições que foram jogadas.
    list, list -> None
    """
    tabuleiro_printado = gerar_tabuleiro()
    for i in range(9):
        for j in range(9):
            tabuleiro_printado[i][j] = '.'

    for i in jogadas:
        linha = i[0]
        coluna = i[1]
        tabuleiro_printado[linha][coluna] = tabuleiro_final[linha][coluna]
    printar_tabuleiro_inteiro(tabuleiro_printado)

# Main

def main():
    """ Função principal, que realiza a interação com o usuário e une com as funções de apoio, anteriormente definidas.
    None -> None
    """
    tabuleiro_final = gerar_tabuleiro()
    bombas = gerar_bombas(tabuleiro_final, 10)
    jogadas = []
    print ('Bem-vindo ao campo minado.')
    print(r"""
                ,--.!,
    Cuidado    __/   -*-
    com as   ,d08b.  '|`
    minas    0088MM
    !!!!!    `9MMP'
        """)
    printar_tabuleiro_apos_jogada(tabuleiro_final, jogadas)
    resposta = input('Digite "S" ou "Sim" para jogar, ou "N" ou "Não" para não jogar. ')
    resposta = validar_resposta(resposta)
    while resposta.lower() in ['s', 'sim']:
        linha = input('Digite a linha que deseja jogar: ')

        erro = validar_nao_vazio(linha)
        if erro:
            return print('Ocorreu um erro.', erro)

        erro = validar_numero(linha)
        if erro:
            return print('Ocorreu um erro.', erro)

        linha = int(linha) - 1

        erro = validar_in_range(1, 9, linha + 1)
        if erro:
            return print('Ocorreu um erro.', erro)

        coluna = input('Digite a coluna que deseja jogar: ')

        erro = validar_nao_vazio(coluna)
        if erro:
            return print('Ocorreu um erro.', erro)

        erro = validar_numero(coluna)
        if erro:
            return print('Ocorreu um erro.', erro)

        coluna = int(coluna) - 1

        erro = validar_in_range(1, 9, coluna + 1)
        if erro:
            return print('Ocorreu um erro.', erro)

        validar_jogada(jogadas, linha, coluna)
        printar_tabuleiro_apos_jogada(tabuleiro_final, jogadas)

        if [linha, coluna] in bombas:
            print(r"""Você pisou em uma mina e explodiu.

    \         .  ./
  \      .:";'.:.."   /
      (M^^.^~~:.'").
-   (/  .    . . \ \)  -
   ((| :. ~ ^  :. .|))
-   (\- |  \ /  |  /)  -
     -\  \     /  /-
       \  \   /  /

Você perdeu.""")
            tabuleiro_final[linha][coluna] = 'M'
            print('\nO tabuleiro inteiro:')
            return printar_tabuleiro_inteiro(tabuleiro_final)
        elif len(jogadas) == 71:
            return print('Você venceu o campo minado. Parabéns.')
        else:
            resposta = input('Digite "S" ou "Sim" para continuar jogando, ou "N" ou "Não" para desistir. ')
            resposta = validar_resposta(resposta)
    print('Obrigado por conferir meu campo minado. Volte sempre.')

if __name__ == '__main__':
    main()
