# Dupla: Victor Martins e Luiz Gustavo

import numpy as np


class Potencia:
    @staticmethod
    def potencia_regular(matriz, tol=10e-6):
        tam = matriz.shape[0]  # Tamanho da matriz
        vetor_atual = np.ones((tam, 1))         # Crio um vetor arbitrário de valor 1, com apenas 1 coluna
        autovalor_atual = 0 # Inicializo o autovalor atual como zero

        converge = True
        while converge:
            autovalor_anterior = autovalor_atual # Guardo o autovalor anterior para efeito de comparação
            vetor_anterior = vetor_atual # Faço o mesmo para o vetor
            x = vetor_anterior / (np.linalg.norm(vetor_anterior)) # defino x como sendo a normalização do vetor velho

            vetor_atual = np.matmul(matriz, x) # Faço o produto da matriz recebida com x e o resultado é um novo vetor
            autovalor_atual = np.matmul(np.transpose(x), vetor_atual) # e um novo autovalor é o produto desse vetor atual com a transposta de x.

            erro = abs((autovalor_atual-autovalor_anterior)/autovalor_atual) # Erro
            if erro < tol: # Se atingiu a tolerância, para o algoritmo. Caso não, converge mais.
                return autovalor_atual, x


def main():
    matriz_1 = np.array([[40, 8, 4, 2, 1],
                         [8, 30, 12, 6, 2],
                         [4, 12, 20, 1, 2],
                         [2, 6, 1, 25, 4],
                         [1, 2, 2, 4, 5]])

    matriz_2 = np.array([[5, 2, 1],
                         [2, 3, 1],
                         [1, 1, 2]])

    resultado_matriz_1 = Potencia.potencia_regular(matriz_1)
    print(f"Maior autovalor da matriz 1: {resultado_matriz_1[0]}")
    print(
        f"Autovetor associado ao autovalor citado:\n {resultado_matriz_1[1]}")

    resultado_matriz_2 = Potencia.potencia_regular(matriz_2)
    print(f"Maior autovalor da matriz 2: {resultado_matriz_2[0]}")
    print(
        f"Autovetor associado ao autovalor citado:\n {resultado_matriz_2[1]}")


if __name__ == '__main__':
    main()
