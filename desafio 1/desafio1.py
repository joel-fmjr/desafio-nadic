# Função que irá calcular o número de passos até que
# N volte para 1
def num_de_passos(n):
    num_passos = 0

    # Uso do while True ara que o loop seja executado pelo menos 1 vez
    while True:
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

    return num_passos


def main():
    # Armazena o maior número de passos para voltar a 1
    maior_num_passos = 0
    # Armazena o valor que gera tal número de passos
    maior_n = 0

    for i in range(1, 1000000):
        num_passos = num_de_passos(i)

        # atualiza as variáveis que armazenam o maior número de passos
        # e o valor que gera tal número de passos
        if(num_passos > maior_num_passos):
            maior_num_passos = num_passos
            maior_n = i

    print(maior_n, maior_num_passos)


if __name__ == '__main__':
    main()
