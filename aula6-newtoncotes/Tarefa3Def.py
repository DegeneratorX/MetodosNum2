import math
import numpy as np

def f(x):
    return 2*(math.sqrt(x)+np.cos(x/2))


class NewtonCotes:
    def __init__(self) -> None:
        raise TypeError("A classe não pode ser instanciada.")
    
    
    @staticmethod
    def newton_cotes(a, b, grau, tol=1e-6):
        # Indexação
        print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(
            "iteracoes", "particoes", "h", "integral", "erro"))
        

        converge = True
        # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
        particoes = 1
        # Primeira iteração
        k = 1
        while converge:
            soma = 0
            h = (b-a)/particoes

            for particao in range(particoes):
                x_inicial = a+particao*h
                x_final = x_inicial+h

