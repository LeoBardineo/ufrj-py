def main():
    comprimento = int(input('Qual o comprimento da pista em metros? '))
    voltas = int(input('Qual o número de voltas a serem percorridas? '))
    reabastecimentos = int(
        input('Qual o número de reabastecimentos desejados? '))
    consumo = int(input('Qual o consumo de combustível do carro em km/l? '))

    resultado = (comprimento * voltas/reabastecimentos) / consumo

    print('A quantidade total de combustível até o primeiro reabastecimento é', resultado)


if __name__ == '__main__':
    main()
