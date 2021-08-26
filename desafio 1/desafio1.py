# Função que irá calcular o número de passos até que
# N volte para 1
def num_de_passos(n):
    num_passos = 0

    # Para que o loop seja executado pelo menos 1 vez
    while True:
        if n % 2 == 0:
            num_passos += 1
            n = n / 2

        else:
            num_passos += 1
            n = 3*n + 1

        # Para o loop em n = 1, depois de todas as contagens de passos,
        # para que não entre em loop infinito
        if n == 1:
            break

    return num_passos
