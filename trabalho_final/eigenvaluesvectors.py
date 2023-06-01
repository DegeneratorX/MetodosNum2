import numpy as np

class Potencia:
    @staticmethod
    def potencia_regular(matriz, tol=10e-6):
        tam = matriz.shape[0]
        vetor_atual = np.ones((tam, 1))
        erro = None
        autovalor_atual = 0

        converge = True
        while converge:
            autovalor_anterior = autovalor_atual
            vetor_anterior = vetor_atual
            x = vetor_anterior / (np.linalg.norm(vetor_anterior))

            vetor_atual = np.matmul(matriz, x)
            autovalor_atual = np.matmul(np.transpose(x), vetor_atual)

            erro = abs((autovalor_atual-autovalor_anterior)/autovalor_atual)
            if erro < tol:
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
    print(f"Autovetor associado ao autovalor citado:\n {resultado_matriz_1[1]}")

    resultado_matriz_2 = Potencia.potencia_regular(matriz_2)
    print(f"Maior autovalor da matriz 2: {resultado_matriz_2[0]}")
    print(f"Autovetor associado ao autovalor citado:\n {resultado_matriz_2[1]}")

if __name__ == '__main__':
    main()