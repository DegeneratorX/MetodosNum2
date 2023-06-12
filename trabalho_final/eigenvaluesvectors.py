# Dupla: Victor Martins e Luiz Gustavo

import numpy as np


class Potencia:
    @classmethod
    def potencia_regular(cls, matriz, tol=10e-6):
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

    @classmethod
    def potencia_inversa(cls, matriz, tol=10e-6):
        tam = matriz.shape[0]  # Tamanho da matriz
        vetor_atual = np.ones((tam, 1)) # Crio um vetor arbitrário de valor 1, com apenas 1 coluna
        


    @staticmethod
    def fatoracao_lu(matriz):
        tam = matriz.shape[0]
        L = np.eye(tam)  # Inicializa L como identidade
        U = matriz.copy()  # Inicializa U como uma cópia da matriz original
        P = np.eye(tam)  # Inicializa P como identidade para pivoteamento

        for k in range(tam):
            # Pivoteamento parcial
            max_linha = np.argmax(np.abs(U[k:, k])) + k
            if max_linha != k:
                U[[k, max_linha], :] = U[[max_linha, k], :]  # Troca as linhas em U
                P[[k, max_linha], :] = P[[max_linha, k], :]  # Troca as linhas em P
                if k >= 1:
                    L[[k, max_linha], :k] = L[[max_linha, k], :k]  # Troca as linhas em L pelas colunas < k

            # Calcula L e U para a iteração atual
            L[k+1:, k] = U[k+1:, k] / U[k, k]
            U[k+1:, k:] -= L[k+1:, k:k+1] @ U[k:k+1, k:] # @ = produto de matriz

        return P, L, U

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
        f"Autovetor associado ao autovalor citado:\tam {resultado_matriz_1[1]}")

    resultado_matriz_2 = Potencia.potencia_regular(matriz_2)
    print(f"Maior autovalor da matriz 2: {resultado_matriz_2[0]}")
    print(
        f"Autovetor associado ao autovalor citado:\tam {resultado_matriz_2[1]}")


if __name__ == '__main__':
    main()
