# Dupla: Victor Martins e Luiz Gustavo
import scipy.linalg as sci
import numpy as np
from copy import deepcopy


class AutoValoresVetores:

    @classmethod
    def potencia_com_deslocamento(cls, matriz, deslocamento, tol=10e-6):
        matriz_aux = deepcopy(matriz)
        matriz_aux = matriz_aux-(deslocamento * np.eye(matriz.shape[0])) # Desloco a matriz (passo 1)
        autovalor, autovetor = cls.potencia_inversa(matriz_aux, tol) # Calculo a potência inversa dessa nova matriz (passo 2)
        autovalor = autovalor + deslocamento # "Desloco" o autovalor dela (passo 3)
        return autovalor, autovetor # passo 5

    @classmethod
    def potencia_regular(cls, matriz, tol=10e-6):
        tam = matriz.shape[0]  # Tamanho da matriz (passo 1)
        vetor_atual = np.ones((tam, 1))         # Crio um vetor arbitrário de valor 1, com apenas 1 coluna (passo 3)
        autovalor_atual = 0 # Inicializo o autovalor atual como zero (passo 2)

        converge = True
        while converge: # inicio da iteração
            autovalor_anterior = autovalor_atual # Guardo o autovalor anterior para efeito de comparação (passo 4)
            vetor_anterior = vetor_atual # Faço o mesmo para o vetor (passo 5)
            x = vetor_anterior / (np.linalg.norm(vetor_anterior)) # defino x como sendo a normalização do vetor velho (passo 6)

            vetor_atual = np.matmul(matriz, x) # Faço o produto da matriz recebida com x e o resultado é um novo vetor (passo 7)
            autovalor_atual = np.matmul(np.transpose(x), vetor_atual) # e um novo autovalor é o produto desse vetor atual com a transposta de x. (passo 8)

            erro = abs((autovalor_atual-autovalor_anterior)/autovalor_atual) # Erro (passo 9)
            if erro < tol: # Se atingiu a tolerância, para o algoritmo. Caso não, converge mais. (passo 10)
                autovalor_atual = np.squeeze(autovalor_atual) # Retiro os 2 brackets do autovalor, pois estava dentro de lista dentro de lista
                x = np.squeeze(x) # Retiro 1 bracket do autovetor, pois previamente estava em uma lista 2D
                return autovalor_atual, x

    @classmethod
    def potencia_inversa(cls, matriz, tol=10e-6):
        tam = matriz.shape[0] # (passo 1)
        vetor_atual = np.ones((tam, 1)) # (passo 4)
        lu, pivo = sci.lu_factor(matriz) # A diferença pra regular é que aqui preciso fatorar em LU e guardar o pivô (passo 2)

        autovalor_atual = 0 # (passo 3)
        converge = True
        while converge: # inicio da iteração
            autovalor_anterior = autovalor_atual # (passo 5)
            vetor_anterior = vetor_atual # (passo 6)
            x = vetor_anterior / (np.linalg.norm(vetor_anterior)) # (passo 7)

            vetor_atual = sci.lu_solve((lu, pivo), x) # Uso os termos decompostos e soluciono o sistema linear (passo 8)
            autovalor_atual = np.matmul(np.transpose(x), vetor_atual) # (passo 9)

            erro = abs((autovalor_atual-autovalor_anterior)/autovalor_atual) # (passo 10)
            if erro < tol: # (passo 11) 
                autovalor_atual = 1/autovalor_atual # Inverto o autovalor, como mostrado no classroom. (passo 11)
                autovalor_atual = np.squeeze(autovalor_atual)
                x = np.squeeze(x)
                return autovalor_atual, x # (passo 13)
            
    @classmethod
    def householder(cls, matriz):
        tam = matriz.shape[0] # (passo 1)
        matriz_householder = np.eye(tam) # (passo 1)
        matriz_anterior = matriz # (passo 2)
        for i in range(tam-2):
            householder_i = cls._matriz_householder_com_coluna_i_da_matriz_anterior(matriz_anterior, i)
            matriz = np.matmul(np.matmul(np.transpose(householder_i), matriz_anterior), householder_i)
            matriz_anterior = matriz
            matriz_householder = np.matmul(matriz_householder, householder_i)
        return matriz, matriz_householder



    @staticmethod
    def _matriz_householder_com_coluna_i_da_matriz_anterior(matriz_anterior, i):
        tam = matriz_anterior.shape[0]
        w = np.zeros(tam)
        w_linha = np.zeros(tam)

        w[i+1:tam] = matriz_anterior[i+1:tam,i]
        w_linha[i+1] = np.linalg.norm(w)
        n = w - w_linha
        n = n/np.linalg.norm(n)
        householder_i = np.eye(tam) - (2*(np.matmul(n, np.transpose(n))))
        return householder_i


def tarefa11():
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
    dominante_matriz_1 = AutoValoresVetores.potencia_regular(matriz_1)
    dominante_matriz_2 = AutoValoresVetores.potencia_regular(matriz_2)
    dominante_matriz_3 = AutoValoresVetores.potencia_regular(matriz_3)

    # Tuplas contendo autovalores e autovetores mínimos (de menor valor absoluto)
    minimo_matriz_1 = AutoValoresVetores.potencia_inversa(matriz_1)
    minimo_matriz_2 = AutoValoresVetores.potencia_inversa(matriz_2)
    minimo_matriz_3 = AutoValoresVetores.potencia_inversa(matriz_3)

    # Crio vetores que contém números entre o menor e maior autovalor das matrizes 1 a 3.
    vetor_de_deslocamentos_matriz_1 = [np.floor(minimo_matriz_1[0]), 4.0, np.ceil(dominante_matriz_1[0])]
    vetor_de_deslocamentos_matriz_2 = [np.floor(minimo_matriz_2[0]), -8.0, np.ceil(dominante_matriz_2[0])]
    vetor_de_deslocamentos_matriz_3 = [np.floor(minimo_matriz_3[0]), 15.0, 27.0, 38.0, np.ceil(dominante_matriz_3[0])]

    print()
    # Matriz 1:
    print("============MATRIZ 1=============")
    for i in matriz_1:
        print(i)
    print()
    for deslocamento in vetor_de_deslocamentos_matriz_1:
        autovalor, autovetor = AutoValoresVetores.potencia_com_deslocamento(matriz_1, deslocamento)
        print(f"Deslocamento: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")
    # Matriz 2:
    print("============MATRIZ 2=============")
    for i in matriz_2:
        print(i)
    print()
    for deslocamento in vetor_de_deslocamentos_matriz_2:
        autovalor, autovetor = AutoValoresVetores.potencia_com_deslocamento(matriz_2, deslocamento)
        print(f"Deslocamento: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")
    # Matriz 3:
    print("============MATRIZ 3=============")
    for i in matriz_3:
        print(i)
    print()
    for deslocamento in vetor_de_deslocamentos_matriz_3:
        autovalor, autovetor = AutoValoresVetores.potencia_com_deslocamento(matriz_3, deslocamento)
        print(f"Deslocamento: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")

def tarefa12():
    matriz_3 = np.array([[40, 8, 4, 2, 1],
                         [8, 30, 12, 6, 2],
                         [4, 12, 20, 1, 2],
                         [2, 6, 1, 25, 4],
                         [1, 2, 2, 4, 5]])
    
    matriz_3_barra, matriz_householder = AutoValoresVetores.householder(matriz_3)
    
    dominante_matriz_3 = AutoValoresVetores.potencia_regular(matriz_3_barra)
    minimo_matriz_3 = AutoValoresVetores.potencia_inversa(matriz_3_barra)
    vetor_de_deslocamentos_matriz_3 = [np.floor(minimo_matriz_3[0]), 15.0, 27.0, 38.0, np.ceil(dominante_matriz_3[0])]

    print("============MATRIZ 3=============")
    for i in matriz_3:
        print(i)
    print()
    print("============MATRIZ 3 BARRA=============")
    for i in matriz_3_barra:
        print(i)
    print()
    print("============MATRIZ HOUSEHOLDER ACUMULADA=============")
    for i in matriz_householder:
        print(i)
    print()
    for deslocamento in vetor_de_deslocamentos_matriz_3:
        autovalor, autovetor = AutoValoresVetores.potencia_com_deslocamento(matriz_3_barra, deslocamento)
        print(f"Deslocamento: {deslocamento}")
        print(f"Autovalor: {autovalor}")
        print(f"Autovetor associado: {autovetor}")
        print()
    print("\n")


if __name__ == '__main__':
    #tarefa11()
    tarefa12()
