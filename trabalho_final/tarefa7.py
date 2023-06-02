import numpy as np
from abc import ABC, abstractstaticmethod
import math
"""
Gauss Exponenciação

Autores:
Victor Martins
Luiz Gustavo
"""

class Integracao(ABC):
    @abstractstaticmethod
    def integrar(f, a, b, tol=1e-6):
        pass


class GaussExponenciacao(Integracao):

    @classmethod
    def integrar(cls, f, limite_inferior_a, limite_superior_b, c, grau, exponencial_simples=True, tol=1e-6):
        print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format("iteracoes",
              "particoes", "tamanho particao", "integral", "erro", "c"))
        a = -c
        b = c
        converge = True
        # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
        particoes = 1
        # Iterações
        k = 0
        primeira_iteracao = True

        while converge:
            k += 1
            soma = 0
            tamanho_particao = (b-a)/particoes
            for particao in range(particoes):
                x_inicial = a+particao*tamanho_particao
                x_final = x_inicial+tamanho_particao
                if grau == 1:
                    soma = soma + \
                        cls.__grau_1(f, x_inicial, x_final, limite_inferior_a,
                                     limite_superior_b, exponencial_simples)
                elif grau == 2:
                    soma = soma + \
                        cls.__grau_2(f, x_inicial, x_final, limite_inferior_a,
                                     limite_superior_b, exponencial_simples)
                elif grau == 3:
                    soma = soma + \
                        cls.__grau_3(f, x_inicial, x_final, limite_inferior_a,
                                     limite_superior_b, exponencial_simples)
                elif grau == 4:
                    soma = soma + \
                        cls.__grau_4(f, x_inicial, x_final, limite_inferior_a,
                                     limite_superior_b, exponencial_simples)
                else:
                    print("Grau inválido.")
                    return

            if primeira_iteracao:
                soma_anterior = 0
                primeira_iteracao = False
            else:
                soma_anterior = soma_atual

            soma_atual = soma
            erro = abs(soma_atual-soma_anterior)
            print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
                k, particoes, tamanho_particao, soma_atual, erro, c))

            if erro < tol:
                return soma_atual
            particoes *= 2

    # Função x(a_k) de gauss-legendre. Mudei para "s", faz mais sentido nesse caso.

    @staticmethod
    def __s(x_inicial, x_final, raiz_a_k):
        return ((x_inicial+x_final)/2) + ((x_final-x_inicial)/2) * raiz_a_k

    # Função x(s)
    @staticmethod
    def __x_de_s_simples(s, limite_inferior_a, limite_superior_b):
        return ((limite_inferior_a+limite_superior_b)/2) + ((limite_superior_b-limite_inferior_a)/2) * np.tanh(s)

    @staticmethod
    def __x_de_s_dupla(s, limite_inferior_a, limite_superior_b):
        return ((limite_inferior_a+limite_superior_b)/2)+((limite_superior_b-limite_inferior_a)/2)*np.tanh((np.pi/2)*np.sinh(s))

    # Função f_barra = f(x(s)) * (d x(s)/ds), onde d x(s)/ds é a derivada da função x(s).
    @classmethod
    def __f_barra_de_s(cls, s, f, limite_inferior_a, limite_superior_b, exponencial_simples):
        if exponencial_simples:
            return f(cls.__x_de_s_simples(s, limite_inferior_a, limite_superior_b))*(((limite_superior_b - limite_inferior_a)/2)*(1/np.cosh(s)**2))
        else:
            return f(cls.__x_de_s_dupla(s, limite_inferior_a, limite_superior_b))*(((limite_superior_b - limite_inferior_a)/2)*((np.pi/2)*(np.cosh(s)/((np.cosh((np.pi/2)*np.sinh(s)))**2))))

    # Gauss-Legendre grau 1
    @classmethod
    def __grau_1(cls, f, x_inicial, x_final, limite_inferior_a, limite_superior_b, exponencial_simples):
        x_1 = 0
        w_1 = 1
        return \
            2*(((x_final-x_inicial)/2 *
                ((cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_1), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_1)))

    # Gauss-Legendre grau 2
    @classmethod
    def __grau_2(cls, f, x_inicial, x_final, limite_inferior_a, limite_superior_b, exponencial_simples):
        x_1 = -np.sqrt(1/3)
        x_2 = +np.sqrt(1/3)
        w_1 = w_2 = 1
        return \
            ((x_final-x_inicial)/2 *
             ((cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_1), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_1 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_2), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_2))

    # Gauss-Legendre grau 3
    @classmethod
    def __grau_3(cls, f, x_inicial, x_final, limite_inferior_a, limite_superior_b, exponencial_simples):
        x_1 = -np.sqrt(3/5)
        x_2 = 0
        x_3 = +np.sqrt(3/5)
        w_1 = w_3 = 5/9
        w_2 = 8/9
        return \
            ((x_final-x_inicial)/2 *
             ((cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_1), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_1 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_2), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_2 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_3), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_3))

    # Gauss-Legendre grau 4
    @classmethod
    def __grau_4(cls, f, x_inicial, x_final, limite_inferior_a, limite_superior_b, exponencial_simples):
        x_1 = -np.sqrt((3+2*np.sqrt(6/5))/7)
        x_2 = -np.sqrt((3-2*np.sqrt(6/5))/7)
        x_3 = np.sqrt((3-2*np.sqrt(6/5))/7)
        x_4 = np.sqrt((3+2*np.sqrt(6/5))/7)
        w_1 = w_4 = (1/2)-((np.sqrt(5/6)/6))
        w_2 = w_3 = (1/36)*(18+np.sqrt(30))

        return \
            ((x_final-x_inicial)/2 *
             ((cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_1), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_1 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_2), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_2 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_3), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_3 +
             (cls.__f_barra_de_s(cls.__s(x_inicial, x_final, x_4), f, limite_inferior_a, limite_superior_b, exponencial_simples))*w_4))


def f(x):
    return 1/(x**2)**(1/3)


def g(x):
    return 1/math.sqrt((4-x**2))


if __name__ == '__main__':
    GaussExponenciacao.integrar(f, limite_inferior_a=-1, limite_superior_b=1,c=3, grau=4, exponencial_simples=True, tol=10e-3)
    GaussExponenciacao.integrar(f, limite_inferior_a=-1, limite_superior_b=1,c=3, grau=4, exponencial_simples=False, tol=10e-3)

    GaussExponenciacao.integrar(g, limite_inferior_a=-2, limite_superior_b=0,
                                c=15, grau=4, exponencial_simples=True, tol=10e-10)
    GaussExponenciacao.integrar(g, limite_inferior_a=-2, limite_superior_b=0,
                                c=3, grau=4, exponencial_simples=False, tol=10e-10)
