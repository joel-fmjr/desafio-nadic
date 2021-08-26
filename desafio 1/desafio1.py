# função que irá calcular o número de passos até que
# n volte para 1
def num_de_passos(n, dicionario_passos):
    num_passos = 0
    n_temp = n

    # uso do while true para que o loop seja executado pelo menos 1 vez
    while True:
        # verifica se já existe um número de passos registrado para o
        # valor de n atual
        passos_temp = dicionario_passos.get(n_temp)

        # caso exista, armazena na varíavel que será retornada
        if passos_temp is not None:
            num_passos += passos_temp
            break

        if n_temp % 2 == 0:
            num_passos += 1
            n_temp = n_temp / 2

        else:
            # aumenta a contagem de passos em 2, porque estão sendo feitos
            # 2 passos na mesma fórmula
            num_passos += 2
            # todo número n, ímpar, quando aplicado à fórmula 3n + 1
            # torna-se um número par, então podemos fazer 2 passos em 1
            n_temp = (3*n_temp + 1)/2

        # parar o loop em n = 1, depois de todas as contagens de passos,
        # para que não entre em loop infinito
        if n_temp == 1:
            break

    # registra o número de passos para n no dicionário
    dicionario_passos[n] = num_passos
    return num_passos


def main(n):
    maior_num_passos = 0    # maior número de passos para voltar a 1
    maior_n = 0             # valor que gera tal número de passos

    # dicionário para armazenar o número de passos gerados por cada número
    # para evitar repetição de verificações por números já consultados
    dicionario_passos = {}

    for i in range(1, n):
        num_passos = num_de_passos(i, dicionario_passos)

        # atualiza as variáveis que armazenam o maior número de passos
        # e o valor que gera tal número de passos
        if(num_passos > maior_num_passos):
            maior_num_passos = num_passos
            maior_n = i

    print(maior_n, maior_num_passos)


if __name__ == '__main__':
    main(1000000)
