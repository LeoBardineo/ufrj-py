# Dado um nome, telefone, email e um instagram,
# retorna um contato, que é uma lista com os argumentos dados,
# e se não foram passados, é colocado como uma string vazia
# str, list, str, str -> list
def criarContato(nome, telefone = '', email = '', instagram = ''):
    if(type(telefone) == list and len(telefone) > 1):
        return 'Apenas um número de telefone deve ser fornecido.'
    if(type(telefone) == str):
        return [nome, [telefone], email, instagram]
    return [nome, telefone, email, instagram]

# Atualizada o contato criado,
# dado uma lista com o contato, o indice do que quer alterar e a informação nova
# list, int, str -> list
def atualizarContato(lista, indice, informacao):
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
