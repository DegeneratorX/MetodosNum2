import math
import numpy as np


def gauss_legendre_2_pontos(a, b, tol=1e-6):
    # Raízes dos dois pontos
    x1 = -1/math.sqrt(3)
    x2 = 1/math.sqrt(3)

    # Pesos
    w1 = w2 = 1

    # Iterações
    k = 0

    soma_anterior = 0
    soma = (b-a)/2 * (w1*f((b-a)/2*x1 + (b+a)/2) + w2*f((b-a)/2*x2 + (b+a)/2))

    erro = abs((soma-soma_anterior))

    print("{:^15}{:^15}{:^15}".format("iteracoes", "soma", "erro"))
    print("{:^15.8f}{:^15.8f}{:^15.8f}".format(k, soma, erro))

    converge = True

    while converge:
        soma_anterior = soma
        k += 1
        h = (b-a)/(2*k)
        soma_particao = 0
        for i in range(k):
            x1_i = a + (2*i + 1)*h
            x2_i = b - (2*i + 1)*h
            soma_particao += w1*f(x1_i) + w2*f(x2_i)
        soma = (b-a)/(2*k) * soma_particao

        erro = abs(soma - soma_anterior)
        print("{:^15.8f}{:^15.8f}{:^15.8f}".format(k, soma, erro))
        if erro < tol:
            return soma, k


def f(x):
    return (np.sin(2*x)+4*(x**2)+3*x)**2


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
result, k = gauss_legendre_2_pontos(a, b)
print("Resultado: ", result)
print("Número de iterações: ", k)
