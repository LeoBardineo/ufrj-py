import random

def dados_iguais():
    """ Gera dois números aleatórios de 1 a 6 até que ambos sejam iguais,
    enquanto esses números são gerados, um contador soma +1 a cada iteração,
    e quando ambos os núemros são equivalentes, retorna o contador.
    Não recebe dados de entrada. """
    count = 0
    roll1, roll2 = 0, 1
    while(roll1 != roll2):
        count += 1
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
    return count

def criarContato(nome, telefone = '', email = '', instagram = ''):
    """Dado um nome, telefone, email e um instagram,
    retorna um contato, que é uma lista com os argumentos dados,
    e se não foram passados, é colocado como uma string vazia
    str, list, str, str -> list
    """
    if(type(telefone) == list and len(telefone) > 1):
        return 'Apenas um número de telefone deve ser fornecido.'
    if(type(telefone) == str):
        contato = [nome, [telefone], email, instagram]
        return contato
    contato = [nome, telefone, email, instagram]
    return contato

def atualizarContato(lista, indice, informacao):
    """Atualiza o contato criado,
    dado uma lista com o contato, o indice do que quer alterar e a informação nova
    list, int, str -> list
    """
    if(indice == 1):
        if(informacao in lista[1]):
            lista[1].remove(informacao)
        else:
            lista[1].append(informacao)
    elif(indice > 3 or indice < 0):
        return lista
    else:
        lista[indice] = informacao
    return lista

def buscaDados(contatos, nome):
    """Dada uma lista de contatos e um nome,
    procura pelo nome na lista de contatos,
    iterando pela lista de contatos e
    verificando se o nome passado existe na string do nome do contato,
    caso exista, é adicionado o contato a uma lista, e ao final da iteração,
    retorna a lista.
    list, str -> list
    """
    i = 0
    contatosAchados = []
    tamanhoContatos = len(contatos)
    while i < tamanhoContatos:
        if nome in contatos[i][0] or nome.upper() in contatos[i][0]:
            contatosAchados.append(contatos[i])
        i += 1
    return contatosAchados

contatos = []

contatos.append(criarContato('julia Campos', ['2199112233'], 'brunoc91@emailquente.com.br', '@brunocampos91'))
contatos.append(criarContato('Julia Fields', ['2198145233'], '', '@juju.fields'))
print(contatos)

# [ ['Bruno Campos',['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields',['2198145233'], '', '@juju.fields'] ]

print(buscaDados(contatos, 'Julia'))
