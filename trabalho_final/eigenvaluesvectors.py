# Dupla: Victor Martins e Luiz Gustavo
import scipy.linalg as sci
import numpy as np
from copy import deepcopy


class Potencia:

    @classmethod
    def potencia_com_deslocamento(cls, matriz, deslocamento, tol=10e-6):
        matriz_aux = deepcopy(matriz)
        matriz_aux = matriz_aux-(deslocamento * np.eye(matriz.shape[0])) # Desloco a matriz
        autovalor, autovetor = cls.potencia_inversa(matriz_aux, tol) # Calculo a potência inversa dessa nova matriz
        autovalor = autovalor + deslocamento # "Desloco" o autovalor dela
        return autovalor, autovetor

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
                autovalor_atual = np.squeeze(autovalor_atual) # Retiro os 2 brackets do autovalor, pois estava dentro de lista dentro de lista
                x = np.squeeze(x) # Retiro 1 bracket do autovetor, pois previamente estava em uma lista 2D
                return autovalor_atual, x

    @classmethod
    def potencia_inversa(cls, matriz, tol=10e-6):
        tam = matriz.shape[0]
        vetor_atual = np.ones((tam, 1))
        lu, pivo = sci.lu_factor(matriz) # A diferença pra regular é que aqui preciso fatorar em LU e guardar o pivô

        autovalor_atual = 0
        converge = True
        while converge:
            autovalor_anterior = autovalor_atual
            vetor_anterior = vetor_atual
            x = vetor_anterior / (np.linalg.norm(vetor_anterior))

            vetor_atual = sci.lu_solve((lu, pivo), x) # Uso os termos decompostos e soluciono o sistema linear
            autovalor_atual = np.matmul(np.transpose(x), vetor_atual)

            erro = abs((autovalor_atual-autovalor_anterior)/autovalor_atual)
            if erro < tol:
                autovalor_atual = 1/autovalor_atual # Inverto o autovalor, como mostrado no classroom.
                autovalor_atual = np.squeeze(autovalor_atual)
                x = np.squeeze(x)
                return autovalor_atual, x
            

def dividir_intervalos(a, b, tam_matriz):
    passo = (b - a) / (tam_matriz - 1)
    return [a + i * passo for i in range(tam_matriz)]


def main():
    matriz_1 = np.array([[5, 2, 1],
                         [2, 3, 1],
                         [1, 1, 2]])

    matriz_2 = np.array([[-14, 1, -2],
                        [1, -1, 1],
                        [-2, 1, -11]])

    matriz_3 = np.array([[40, 8, 4, 2, 1],
                         [8, 30, 12, 6, 2],
                         [4, 12, 20, 1, 2],
                         [2, 6, 1, 25, 4],
                         [1, 2, 2, 4, 5]])


    # Tupla contendo autovalores e autovetores dominantes. (autovalores, autovetores)
    dominante_matriz_1 = Potencia.potencia_regular(matriz_1)
    dominante_matriz_2 = Potencia.potencia_regular(matriz_2)
    dominante_matriz_3 = Potencia.potencia_regular(matriz_3)

    # Tuplas contendo autovalores e autovetores mínimos (de menor valor absoluto)
    minimo_matriz_1 = Potencia.potencia_inversa(matriz_1)
    minimo_matriz_2 = Potencia.potencia_inversa(matriz_2)
    minimo_matriz_3 = Potencia.potencia_inversa(matriz_3)

    # Crio vetores que contém números com espaços iguais entre o menor e maior autovalor das matrizes 1 a 3.
    vetor_de_deslocamentos_matriz_1 = dividir_intervalos(np.floor(minimo_matriz_1[0]), np.ceil(dominante_matriz_1[0]), tam_matriz=matriz_1.shape[0])
    vetor_de_deslocamentos_matriz_2 = dividir_intervalos(np.floor(minimo_matriz_2[0]), np.ceil(dominante_matriz_2[0]), tam_matriz=matriz_2.shape[0])
    vetor_de_deslocamentos_matriz_3 = dividir_intervalos(np.floor(minimo_matriz_3[0]), np.ceil(dominante_matriz_3[0]), tam_matriz=matriz_3.shape[0])
    print(vetor_de_deslocamentos_matriz_1)
    print()
    # Matriz 1:
    print("============MATRIZ 1=============")
    for deslocamento in vetor_de_deslocamentos_matriz_1:
        autovalor, autovetor = Potencia.potencia_com_deslocamento(matriz_1, deslocamento)
        print(f"Deslocamento feito: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")
    # Matriz 2:
    print("============MATRIZ 2=============")
    for deslocamento in vetor_de_deslocamentos_matriz_2:
        autovalor, autovetor = Potencia.potencia_com_deslocamento(matriz_2, deslocamento)
        print(f"Deslocamento feito: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")
    # Matriz 3:
    print("============MATRIZ 3=============")
    for deslocamento in vetor_de_deslocamentos_matriz_3:
        autovalor, autovetor = Potencia.potencia_com_deslocamento(matriz_3, deslocamento)
        print(f"Deslocamento feito: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")

if __name__ == '__main__':
    main()
