# Dado o ano de nascimento de uma pessoa, retorna o signo chinês dela
# de acordo com a tabela
# int -> string
def signo_chines(ano):
    tabela = (
        "Macaco",
        "Galo",
        "Cão",
        "Porco",
        "Rato",
        "Boi",
        "Tigre",
        "Coelho",
        "Dragão",
        "Serpente",
        "Cavalo",
        "Carneiro"
    )
    return tabela[ano%12]
