# =============== Funções de validação ===============

def validar_nao_vazio(entrada):
    if not entrada:
        raise TypeError('Entrada vazia. Digite algo.\n')

def validar_numero(txt):
    if not txt.isnumeric():
        raise TypeError('O número digitado não é numérico.\n')

def validar_positivo(num):
    if num <= 0:
        raise ValueError('O numero digitado não é positivo e/ou diferente de zero.\n')

def validar_a_menor_que_b(a, b):
    if a > b:
        raise ValueError('A é maior que B, e é preciso que seja menor.\n')

def validar_info(info):
    if info.len() != 4:
        raise ValueError('Quantidade de informações inválida. Apenas 4 informações devem ser passadas.\n')

def validar_in_range(min, max, num):
    if num < min or num > max:
        raise IndexError('Número digitado fora do alcance. Mínimo: ' + str(min) + ', máximo: ' + str(max) + '.\n')

# =============== Questão 1 ===============

from random import randint

def gerar_rolagens(num_rolagens):
    """ Simula as rolagens de um dado, gerando números aleatórios de 1 até 6, pela quantidade de vezes que o usuário quiser, e retorna uma lista com todos os números aleatórios.
    int -> list
    """
    rolagens = []
    while len(rolagens) != num_rolagens:
        rolagens.append(randint(1, 6))
    return rolagens

def contar_sequencia(rolagens):
    """ Conta e retorna quantas sequências numéricas ocorreram em uma lista.
    list -> int
    """
    count = 0
    sequencia_rolando = False
    for i in range(1, len(rolagens)):
        if(rolagens[i] == rolagens[i - 1] and not sequencia_rolando):
            count += 1
            sequencia_rolando = True
        else:
            sequencia_rolando = False
    return count

def main_questao_1():
    """ Une a lógica das funções gerar_rolagem, e contar_sequencia, com a interação do usuário por meio do print e input, para contar a sequência de números em uma rolagem de dados, sendo o número de rolagens definido pelo usuário.
    None -> None
    """
    print('\n===== Contador de sequências na rolagem de dados =====')
    print(r"""
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/
    """)
    num_rolagens = input('Quantas rolagens você deseja realizar? ')

    validar_nao_vazio(num_rolagens)
    validar_numero(num_rolagens)

    num_rolagens = int(num_rolagens)

    validar_positivo(num_rolagens)

    rolagens = gerar_rolagens(num_rolagens)
    count_sequencia = contar_sequencia(rolagens)

    print('Números:', str(rolagens).replace('[', '').replace(']', ''))
    print('Sequências:', count_sequencia, '\n')

# =============== Questão 2 ===============

def caso_1(a, b, c):
    """ Caso 1 da segunda questão, retorna a área do trapézio.
    int, int, int -> float
    """
    return (a + b) * c / 2

def caso_2(a, b, c):
    """ Caso 2 da segunda questão, retorna os valores ao quadrado.
    int, int, int -> int
    """
    return a * b, b * b, c * c

def caso_3(a, b, c):
    """ Caso 3 da segunda questão, retorna a média aritmética dos valores.
    int, int, int -> float
    """
    return (a + b + c) / 3

def caso_4(a, b, c):
    """ Caso 4 da segunda questão, retorna a soma dos inteiros de a até b, com uma variação entre os inteiros de c.
    int, int, int -> int
    """
    resultado = 0
    for i in range(a, b + 1, c):
        resultado += i
    return resultado

# Array com funções >>> switch case
def main_questao_2():
    """ Dado um código i e os valores a, b e c pelo usuário por meio do input, executa um dos quatro cálculos e retorna seu resultado junto aos valores digitados.
    None -> None
    """
    print('\n===== Cálculos diversos =====\n')

    print('1 - Irá ser calculado a área do trapézio, sendo a e b as bases e c altura.')
    print('2 - Irá ser calculado a * a, b * b e c * c')
    print('3 - Irá ser calculado a média aritmética entre a, b e c.')
    print('4 - Irá ser calculado a soma dos inteiros de a até b, com uma varação de c entre os inteiros.\n')

    casos = [caso_1, caso_2, caso_3, caso_4]
    i = input('Indique o código i que desejar, de 1 até 4: ')

    validar_nao_vazio(i)
    validar_numero(i)
    validar_in_range(1, 4, i)

    a = input('Quanto vale a? ')

    validar_nao_vazio(a)
    validar_numero(a)
    validar_positivo(a)

    b = input('Quanto vale b? ')

    validar_nao_vazio(b)
    validar_numero(b)
    validar_positivo(b)
    validar_a_menor_que_b(a, b)

    c = input('Quanto vale c? ')

    validar_nao_vazio(b)
    validar_numero(c)
    validar_positivo(c)

    i = int(i)
    a = int(a)
    b = int(b)
    c = int(c)

    print('Valores lidos: {}, {}, {}'.format(a, b, c))
    print('Resultado:', casos[i - 1](a, b, c), '\n')

# =============== Questão 3 ===============

def gerar_table(matriz):
    quantidade_char = 0
    maiores = [4, 8, 8]
    for i in range(len(matriz)):
        indice = 0
        for j in matriz[i]:
            quantidade_char += len(j)
            if (len(j)> maiores[indice]):
                maiores[indice] = len(j)
            indice += 1

    linha = ''

    for i in range(len(matriz)):
        nome = matriz[i][0]
        registro = matriz[i][1]
        telefone = matriz[i][2]

        if maiores[0] > len(nome):
            espacos_nome = (maiores[0] - len(nome)) + 1
        else:
            espacos_nome = 1

        if maiores[1] > len(registro):
            espacos_registro = (maiores[1] - len(registro)) + 1
        else:
            espacos_registro = 1

        if maiores[2] > len(telefone):
            espacos_telefone = (maiores[2]  - len(telefone)) + 1
        else:
            espacos_telefone = 1

        linha += '| {}'.format(nome) + ' ' * espacos_nome
        linha += '| {}'.format(registro) + ' ' * espacos_registro
        linha += '| {}'.format(telefone) + ' ' * espacos_telefone + '|\n'
        linha += '+' + '-' * (maiores[0] + 2)
        linha += '+' + '-' * (maiores[1] + 2)
        linha += '+' + '-' * (maiores[2] + 2) + '+\n'

    if maiores[0] > 4:
        espacos_nome = (maiores[0]) - 3
    else:
        espacos_nome = 1

    if maiores[1] > 8:
        espacos_registro = (maiores[1] - 8)
    else:
        espacos_registro = 1

    if maiores[2] > 8:
        espacos_telefone = (maiores[2] - 8) + 1
    else:
        espacos_telefone = 1

    primeira_linha = '+' + '-' * (maiores[0] + 2)
    primeira_linha += '+' + '-' * (maiores[1] + 2)
    primeira_linha += '+' + '-' * (maiores[2] + 2) + '+\n'
    primeira_linha +='| Nome' + ' ' * espacos_nome
    primeira_linha +='| Registro' + ' ' * espacos_registro
    primeira_linha +='| Telefone' + ' ' * espacos_telefone + '|\n'
    primeira_linha += '+' + '-' * (maiores[0] + 2)
    primeira_linha += '+' + '-' * (maiores[1] + 2)
    primeira_linha += '+' + '-' * (maiores[2] + 2) + '+'

    return primeira_linha + '\n' + linha


def busca(setor, matriz):
    """ Dado um setor e uma matriz de funcionários de uma empresa, retorna todos os funcionários que pertencem aquele setor.
    string, list -> list
    """
    resultado = []
    for i in range(len(matriz)):
        for j in matriz[i]:
            if(setor.lower().strip() == j.lower()):
                resultado.append([matriz[i][0], matriz[i][1], matriz[i][3]])
    return resultado

def main_questao_3():
    print('\n===== Busca por funcionários de certo setor  =====\n')
    len_funcionarios = input('Quantos funcionários você deseja por na matriz? ')

    validar_nao_vazio(len_funcionarios)
    validar_numero(len_funcionarios)
    validar_positivo(len_funcionarios)

    info_funcionarios = []
    for i in range(len_funcionarios):
        info_funcionarios.append([])

        info = input('Digite as informações do {}º funcionário separado por vígula: '.format(i+1))
        validar_nao_vazio(info)
        lista_info = info.split(',')
        validar_info(lista_info)

        for info_funcionario_especifico in lista_info:
            info_funcionarios[i].append(info_funcionario_especifico.strip())

    setor = input('Indique qual setor dos funcionários deseja realizar a pesquisa: ')
    resultado = busca(setor, info_funcionarios)
    print('\n{} funcionários encontrados: '.format(len(resultado)))
    print(gerar_table(resultado))

# =============== Main ===============

def main():
    """ Une todas as funções das questões, e pergunta para o usuário qual das questões ele deseja executar.
    None -> None
    """
    try:
        print('1 - Contador de sequências na rolagem de dados')
        print('2 - Cálculos diversos')
        print('3 - Busca por funcionários de certo setor\n')
        questoes = [main_questao_1, main_questao_2, main_questao_3]

        questao = input('Qual questão você deseja executar? ')

        validar_nao_vazio(questao)
        validar_numero(questao)

        questao = int(questao)

        validar_in_range(1, 3, questao)

        questoes[questao - 1]()
    except Exception as error:
        print('Ocorreu um erro.', error)
    finally:
        executar_outro()

def executar_outro():
    """ Pergunta ao usuário se ele deseja executar outro exercício para que o mesmo não tenha que executar novamente o arquivo para testar as outras questões.
    None -> None
    """
    executar = input('Deseja executar outro exercício? (S/N) ').lower().strip()
    if (executar == 's' or executar == 'sim'):
        return main()
    elif (executar == 'n' or executar == 'nao' or executar == 'não'):
        print('\nEncerrando programa. Obrigado por conferir os exercícios que fiz.\n')
    else:
        print('Por favor, digite S ou Sim para executar outro exercício, e N ou Não para não executar.\n')
        return executar_outro()

def bem_vindo():
    """ Imprime na tela a mensagem de bem-vindo. Não coloquei na main pois se não essa mensagem ficaria imprimindo várias vezes, já que utilizei da recursão durante o programa.
    None -> None
    """
    print('\n===== Seja bem-vindo ao Laboratório de Programação 10 =====\n')

bem_vindo()
main()
