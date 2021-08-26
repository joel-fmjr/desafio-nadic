# Função que irá calcular o número de passos até que
# N volte para 1
def num_de_passos(n, dicionario_passos):
    num_passos = 0
    n_temp = n

    # Uso do while True ara que o loop seja executado pelo menos 1 vez
    while True:
        passos_temp = dicionario_passos.get(n_temp)

        if passos_temp is not None:
            num_passos += passos_temp
            break

        if n % 2 == 0:
            num_passos += 1
            n = n / 2

        else:
            # Aumenta a contagem de passos em 2, porque estão sendo feitos
            # 2 passos na mesma fórmula
            num_passos += 2
            # Todo número n, ímpar, quando aplicado à fórmula 3n + 1
            # torna-se um número par, então podemos fazer 2 passos em 1
            n = (3*n + 1)//2

        # Parar o loop em n = 1, depois de todas as contagens de passos,
        # para que não entre em loop infinito
        if n == 1:
            break

    dicionario_passos[n] = num_passos
    return num_passos


def main():
    # Armazena o maior número de passos para voltar a 1
    maior_num_passos = 0
    # Armazena o valor que gera tal número de passos
    maior_n = 0

    # dicionário para armazenar o número de passos gerados por cada número
    # para evitar repetição de verificações por números já consultados
    dicionario_passos = {}

    for i in range(1, 1000000):
        num_passos = num_de_passos(i, dicionario_passos)

        # atualiza as variáveis que armazenam o maior número de passos
        # e o valor que gera tal número de passos
        if(num_passos > maior_num_passos):
            maior_num_passos = num_passos
            maior_n = i

    print(maior_n, maior_num_passos)


if __name__ == '__main__':
    main()
