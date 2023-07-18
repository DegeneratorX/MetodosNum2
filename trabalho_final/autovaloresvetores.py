# Dupla: Victor Martins e Luiz Gustavo
# Turma 2023.1

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
            
        return None, None

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
            
        return None, None
    
    @classmethod
    def householder(cls, matriz):
        tam = matriz.shape[0] # (linha 1)
        matriz_householder = np.eye(tam) # (linha 1)
        matriz_anterior = matriz # (linha 2)

        for i in range(tam-2): # (linha 3)
            householder_i = cls._matriz_householder_com_coluna_i_da_matriz_anterior(matriz_anterior, i) # (linha 4)
            matriz = np.matmul(np.matmul(np.transpose(householder_i), matriz_anterior), householder_i) # (linha 5)
            matriz_anterior = matriz # (linha 6)
            matriz_householder = np.matmul(matriz_householder, householder_i) # (linha 7)

        return matriz, matriz_householder # (linha 8, linha 9)

    @staticmethod
    def _matriz_householder_com_coluna_i_da_matriz_anterior(matriz_anterior, i):
        tam = matriz_anterior.shape[0]
        w = np.zeros(tam) # (linha 1)
        w_linha = np.zeros(tam) # (linha 2)

        w[i+1:tam] = matriz_anterior[i+1:tam,i] # (linha 4)

        w_linha[i+1] = np.linalg.norm(w) # (linha 5, linha 6)

        n = w - w_linha # (linha 7)
        n = n/np.linalg.norm(n) # (linha 8)

        n = [[i] for i in n] # Recoloco os valores em formato [[a], [b], [c]]...
        # ...assim n fica [[a], [b], [c]] (coluna) e n transposto fica [[a, b, c]] (linha).

        householder_i = np.eye(tam) - 2*np.matmul(n, np.transpose(n)) # (linha 9)
        return householder_i # (linha 10)

    @classmethod
    def qr(cls, matriz, tridiagonalizada=False, tol=10e-6):
        val = 100 # (linha 1)
        tam = matriz.shape[0]
        p = np.eye(tam) # (linha 2)

        matriz_anterior = deepcopy(matriz) # (linha 3)
        k = 0 # Registro de iterações

        while val > tol: # (linha 4)
            if not tridiagonalizada:
                q, r = cls._decomposicao_qr_regular(matriz_anterior, tam, tol) # (linha 5)
            else: 
                q, r = cls._decomposicao_qr_tridiagonal(matriz_anterior, tam) # (linha 5)

            matriz = np.matmul(r, q) # (linha 6)
            matriz_anterior = deepcopy(matriz) # (linha 7)
            p = np.matmul(p, q) # (linha 8)
            val = cls._soma_dos_quadrados_dos_termos_abaixo_da_diagonal(matriz, tam) # (linha 9)

            #print(f"ITERAÇÃO {k}: (1.iii e 2.i) Matriz_3 após a iteração:") # Requisito da questão 1.iii
            #for i in matriz:
            #    print(i)
            k += 1

        print(f"\n(1.i) Matriz 3 barra (equivale ao A barra, mas contém os autovalores diagonalizados):")
        for i in matriz:
            print(i)

        autovalores = np.zeros(5) # (linha 10)
        for i in range(matriz.shape[0]): # (linha 10)
            autovalores[i] = matriz[i][i] # (linha 10)

        return p, autovalores # (linha 11)

    @classmethod
    def _decomposicao_qr_regular(cls, matriz_anterior, tam, tol):
        qt = np.eye(tam) # (linha 1)
        r_anterior = matriz_anterior # (linha 2)

        for j in range(tam-1): # (linha 3)
            for i in range(j+1, tam): # (linha 4)

                jota = cls.matriz_jacobi_baseada_no_elemento_ij_de_R_velha(r_anterior, i, j, tam, tol) # (linha 5)
                r = np.matmul(jota, r_anterior) # (linha 6)
                r_anterior = deepcopy(r) # (linha 7)
                qt = np.matmul(jota, qt) # (linha 8)

        return np.transpose(qt), r # (linha 10, 11 e 12)
    
    @staticmethod # Processo de Gram-Schmidt (invés de Jacobi)
    def _decomposicao_qr_tridiagonal(matriz_anterior, tam):
        qt = np.zeros((tam, tam))
        r = np.zeros((tam, tam))
        
        for j in range(tam):
            v = matriz_anterior[:, j]
            for i in range(j):
                r[i, j] = np.dot(qt[:, i], matriz_anterior[:, j])
                v -= r[i, j] * qt[:, i]
            
            r[j, j] = np.linalg.norm(v)
            qt[:, j] = v / r[j, j]
        
        return qt, r

    @staticmethod
    def matriz_jacobi_baseada_no_elemento_ij_de_R_velha(matriz_anterior, i, j, tam, tol):
        jota = np.eye(tam) # (linha 1)

        if abs(matriz_anterior[i][j]) <= tol: # (linha 2)
            return jota
        
        if abs(matriz_anterior[j][j]) <= tol: # (linha 3)
            if matriz_anterior[i][j] < 0: # (linha 4)
                angulo = np.pi/2 # (linha 5)
            else:                # (linha 6)
                angulo = -np.pi/2 # (linha 7)

        else: # (linha 9)
            angulo = np.arctan(-matriz_anterior[i][j]/matriz_anterior[j][j]) # (linha 10)
            
        jota[i][i] = np.cos(angulo) # (linha 12)
        jota[j][j] = np.cos(angulo) # (linha 13)
        jota[i][j] = np.sin(angulo) # (linha 14)
        jota[j][i] = -np.sin(angulo) # (linha 15)
        
        return jota # (linha 16)
 
    @staticmethod
    def _soma_dos_quadrados_dos_termos_abaixo_da_diagonal(matriz, tam):
        soma = 0
        for i in range(tam):
            for j in range(i):
                soma = soma + (matriz[i,j])**2
        return soma


np.set_printoptions(precision=6, suppress=True)

################################################
# ================= TAREFA 11 =================#
################################################
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
    vetor_de_deslocamentos_matriz_1 = np.linspace(np.floor(minimo_matriz_1[0]), np.ceil(dominante_matriz_1[0]), matriz_1.shape[0]) # Espaçamento igual para melhorar a busca por autovalores intermediários. Divido em 3
    vetor_de_deslocamentos_matriz_2 = np.linspace(np.floor(minimo_matriz_2[0]), np.ceil(dominante_matriz_2[0]), matriz_2.shape[0])
    vetor_de_deslocamentos_matriz_3 = np.linspace(np.floor(minimo_matriz_3[0]), np.ceil(dominante_matriz_3[0]), matriz_3.shape[0]) # Espaçamento igual para melhorar a busca por autovalores intermediários. Divido em 5

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


################################################
# ================= TAREFA 12 =================#
################################################
def tarefa12_hh():
    print("=================================")
    print("=====TAREFA HOUSEHOLDER (12)=====")
    print("=================================")
    print()

    matriz_3 = np.array([[40, 8, 4, 2, 1],
                         [8, 30, 12, 6, 2],
                         [4, 12, 20, 1, 2],
                         [2, 6, 1, 25, 4],
                         [1, 2, 2, 4, 5]])
    
    matriz_3_barra, matriz_householder = AutoValoresVetores.householder(matriz_3)
    
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

    dominante_matriz_3 = AutoValoresVetores.potencia_regular(matriz_3_barra)
    minimo_matriz_3 = AutoValoresVetores.potencia_inversa(matriz_3_barra)
    vetor_de_deslocamentos_matriz_3 = np.linspace(np.floor(minimo_matriz_3[0]), np.ceil(dominante_matriz_3[0]), matriz_3.shape[0]) # Espaçamento igual para melhorar a busca por autovalores intermediários

    print("============AUTOVALORES E AUTOVETORES DE MATRIZ 3 E MATRIZ 3 BARRA=============")
    for deslocamento in vetor_de_deslocamentos_matriz_3:
        autovalor, autovetor = AutoValoresVetores.potencia_com_deslocamento(matriz_3_barra, deslocamento)
        print(f"Deslocamento: {deslocamento}")
        print(f"Autovalor Matriz 3 (e Matriz 3 barra): {autovalor}")
        print(f"Autovetor na Matriz 3 barra: \n{autovetor}")
        print(f"Autovetor na Matriz 3 encontrado pelo produto da matriz hh com autovetor da matriz barra: \n{np.matmul(matriz_householder, np.transpose(autovetor))}")
        print()
    print("\n")

def tarefa12_qr():
    print("==================================")
    print("==========TAREFA QR (12)==========")
    print("==================================")
    print()

    matriz_3 = np.array([[100, 30, -25, 15, 5],
                         [30, 150, 20, 10, -15],
                         [-25, 20, 200, -10, 13],
                         [15, 10, -10, 300, 50],
                         [5, -15, 13, 50, 250]])
    print("============AUTOVALORES E AUTOVETORES DA MATRIZ 3 SEM TRIDIAGONAL=============")
    autovetores_p, autovalores = AutoValoresVetores.qr(matriz_3, tridiagonalizada=False)

    print()
    print(f"(1.ii) Matriz acumulada P = Q1*Q2*Q3*... (é uma matriz composta por autovetores para cada autovalor):")
    for i in autovetores_p:
        print(i)
    print()
    autovetores_p = np.transpose(autovetores_p) # Transposta para capturar as colunas de autovetores
    print("(1.iv) Pares de autovalores e autovetores da Matriz 3:")
    for i in range(matriz_3.shape[0]):
        print(f"Autovalor Matriz 3: {autovalores[i]}")
        print(f"Autovetor associado: {autovetores_p[i]}\n")


    print("============AUTOVALORES E AUTOVETORES DA MATRIZ 3 COM TRIDIAGONAL=============")
    matriz_3_barra, matriz_householder = AutoValoresVetores.householder(matriz_3)
    autovetores_p, autovalores = AutoValoresVetores.qr(matriz_3_barra, tridiagonalizada=True)
    
    print()
    print(f"(2.ii) Matriz acumulada P = Q1*Q2*Q3*...:")
    for i in autovetores_p:
        print(i)
    print()
    print(f"(2.iii) Matriz H*P resultante:")
    resultante = np.matmul(matriz_householder, autovetores_p)
    for i in resultante:
        print(i)
    print()

if __name__ == '__main__':
    #tarefa11()
    #tarefa12_hh()
    tarefa12_qr()
