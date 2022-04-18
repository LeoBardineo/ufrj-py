def areaRetangulo():
    print('1 - Área do retângulo')
    largura = int(input('Digite a largura do retângulo: '))
    altura = int(input('Digite a altura do retângulo: '))
    area = largura * altura
    print('A área do retângulo é ' + str(area) + '.')

def areaCubo():
    print('2 - Área de superfície do cubo')
    c = int(input('Digite a aresta do cubo: '))
    area = c ** 2 * 6
    print('A área da superfície do cubo é ' + str(area) + '.')

def areaCoroa():
    print('3 - Área da coroa circular')
    r1 = int(input('Digite o raio da circuferência externa: '))
    r2 = int(input('Digite o raio da circuferência interna: '))
    if (r2 > r1): return print('O raio da circuferencia interna é maior que o raio da circuferência externa. Por favor, digite-os novamente.')
    area = 3.14 * (r1 ** 2 - r2 ** 2)
    print('A área da coroa circular é ' + str(area))

def mediaSimples(n1, n2):
    return n1 + n2 / 2

def ordenada(a, b, c, x):
    return a * x ** 2 + b * x + c

def mediaPonderada(n1, p1, n2, p2):
    return (n1 * p1 + n2 * p2) / (p1 + p2)

def erroAproximacao(q, n):
    somaTermos = 1 / (1 - q)
    somaPrimeirosTermos = (q ** n - 1) / (q - 1)
    return somaTermos - somaPrimeirosTermos

def gorjeta(conta):
    return conta * 0.1

def gorjetaLegislacao(conta, porcentagem):
    return conta * porcentagem / 100

def saldoFinal(saldoInicial, numeroMeses, jurosMensal):
    return saldoInicial * (1 + jurosMensal * numeroMeses)

def distancia(velocidadeCorrenteza, larguraRio, velocidadeBarco):
    tempo = larguraRio / velocidadeBarco
    return velocidadeCorrenteza * tempo

def main () :
    exerciciosDisponiveis = [
        areaRetangulo,
        areaCubo,
        areaCoroa,
        mediaSimples,
        ordenada,
        mediaPonderada,
        erroAproximacao,
        gorjeta,
        gorjetaLegislacao,
        saldoFinal,
        distancia
    ]

    print('Bem-vindo ao Laboratório de Programação 1.')

    exercicio = int(input('Qual exercício, de 1 à 11, você deseja executar? '))

    if (exercicio < 1 or exercicio > 11):
        print('Exercício não encontado. Por favor, digite um número entre ou igual à 1 e 11, correspondente ao exercício.')
        main()

    print('')
    exerciciosDisponiveis[exercicio - 1]()
    print('')

    execOutro()

def execOutro () :
    executar = input('Deseja executar outro exercício? (s/n) ').lower().strip()
    if (executar == 's' or executar == 'sim'):
        main()
    elif (executar == 'n' or executar == 'nao' or executar == 'não'):
        print('Encerrando programa. Obrigado por conferir os exercícios que fiz.')
        print('Você pode ver mais projetos meus em https://www.github.com/leobardineo.')
    else:
        print('Por favor, digite s para sim, e n para não.')
        execOutro()

main()
