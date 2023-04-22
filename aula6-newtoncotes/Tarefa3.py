import math
import numpy as np


def f(x):
    return 2*(math.sqrt(x)+np.cos(x/2))


def newton_cotes_grau4_fechada(a, b, tol=1e-3):
    # Indexação
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(
        "iteracoes", "particoes", "h", "integral", "erro"))

    # Grau da fórmula.
    grau = 4

    # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
    particoes = 1
    # Primeira iteração
    k = 1

    # Intervalo h de cada partição do conjunto de partições
    h = (b-a)/particoes

    # Integral
    #soma = ((2*(b-a)/grau) / 45) * (7*f(a)+32 *f(a+h)+12*f(a+2*h)+32*f(a+3*h)+7*f(b))
    soma = ((b-a)/2)*(f(a)+f(b))
    soma_anterior = 0  # Valor necessário pra verificar a tolerância
    soma_atual = soma  # E fazer a subtração desse com o anterior
    erro = abs((soma_atual-soma_anterior)/soma_atual)  # Erro

    # Formatação das iterações
    print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
        k, particoes, h, soma_atual, erro))

    if erro < tol:  # Se já atingiu a tolerância, o programa para
        return soma_atual

    # Aumento as partições
    particoes = 2
    converge = True

    # Aqui começa o método iterativo, refazendo todo o cálculo com novas divisões para partições
    while converge:
        soma = 0

        k = k + 1  # Segunda, terceira, quarta iteração...
        h = (b-a)/particoes

        for particao in range(particoes):
            x_inicial = a+particao*h  # Defino um novo "a" e "b" novo para cada partição. O "a" é baseado em quantos "h" foram andados.
            x_final = x_inicial+h

            # Fórmula do grau 4 fechada
            #soma = soma + ((2*(x_final-x_inicial)/grau) / 45) * (7*f(x_inicial) + 32*f(x_inicial+h)+12*f(x_inicial+2*h)+32*f(x_inicial+3*h)+7*f(x_final))
            soma = soma + ((x_final-x_inicial)/2)*(f(x_inicial)+f(x_final))
        # Feita a soma, guardo o valor anterior e capturo esse novo valor
        soma_anterior = soma_atual
        soma_atual = soma
        erro = abs((soma_atual-soma_anterior)/soma_atual)

        print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
            k, particoes, h, soma_atual, erro))

        if erro < tol:
            return soma_atual

        # Multiplico as partições por 2, pois assim corto pela metade cada vez mais o h, procurando manter a simetria dos intervalos
        particoes *= 2


def newton_cotes_grau4_aberta(a, b, tol=1e-6):
    # Indexação
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(
        "iteracoes", "particoes", "h", "integral", "erro"))

    # Grau da fórmula. Na aberta o denominador é grau+2.
    grau = 4 + 2

    # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
    particoes = 1
    # Primeira iteração
    k = 1

    # Intervalo h de cada partição do conjunto de partições
    h = (b-a)/particoes

    # Integral
    soma = ((6*(b-a)/grau) / 20) * (11*f(a+h)-14 *f(a+2*h)+26*f(a+3*h)-14*f(a+4*h)+11*f(a+5*h))

    soma_anterior = 0  # Valor necessário pra verificar a tolerância
    soma_atual = soma  # E fazer a subtração desse com o anterior
    erro = abs((soma_atual-soma_anterior)/soma_atual)  # Erro

    # Formatação das iterações
    print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
        k, particoes, h, soma_atual, erro))

    if erro < tol:  # Se já atingiu a tolerância, o programa para
        return soma_atual

    # Aumento as partições
    particoes = 2
    converge = True

    # Aqui começa o método iterativo, refazendo todo o cálculo com novas divisões para partições
    while converge:
        soma = 0

        k = k + 1  # Segunda, terceira, quarta iteração...
        h = (b-a)/particoes

        for particao in range(particoes):
            x_inicial = a+particao*h  # Defino um novo "a" e "b" novo para cada partição
            x_final = x_inicial+h

            # Fórmula do grau 4 aberta

            soma = soma + ((6*(x_final-x_inicial)/grau) / 20) * (11*f(x_inicial+h)-14*f(
                x_inicial+2*h)+26*f(x_inicial+3*h)-14*f(x_inicial+4*h)+11*f(x_inicial+5*h))
        # Feita a soma, guardo o valor anterior e capturo esse novo valor
        soma_anterior = soma_atual
        soma_atual = soma
        erro = abs((soma_atual-soma_anterior)/soma_atual)

        print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
            k, particoes, h, soma_atual, erro))

        if erro < tol:
            return soma_atual

        # Multiplico as partições por 2, pois assim corto pela metade cada vez mais o h, procurando manter a simetria dos intervalos
        particoes *= 2


print("==Tabela de integração de Newton-Cotes grau 4 fechada==")
soma_fechada = newton_cotes_grau4_fechada(2, 20)
print()
print("==Tabela de integração de Newton-Cotes grau 4 aberta==")
soma_aberta = newton_cotes_grau4_aberta(2, 20)
print()
print(
    f"Resultado da integral aproximada usando grau 4 fechada: {soma_fechada}")
print(f"Resultado da integral aproximada usando grau 4 aberta: {soma_aberta}")
