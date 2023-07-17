# Dupla: Victor Martins e Luiz Gustavo
# Turma 2023.1
import numpy as np
from scipy.linalg import lu_factor, lu_solve
G = 9.8

class ProblemaValorContorno:
    @classmethod
    def diferenca_finita_pvc1(cls, n, y_inicial, y_final, esquerda, central, direita):
        # Delta x será utilizado para a diferença finita (tamanho da partição)
        delta_x = (y_final - y_inicial)/n

        # Inicialização da matriz e do vetor b que irão fazer parte 
        # do sistema de equações do método
        matriz = np.zeros((n-1, n-1))
        b = np.zeros(n-1)
        
        # Primeira linha da condição de contorno do sistema
        matriz[0, 0:2] = np.array([central(delta_x), direita(delta_x)])

        b[0] = -1 * (y_inicial * esquerda(delta_x))
        
        b[n-2] = -1* (y_final * direita(delta_x))

        # Linhas do meio da matriz, tridiagonalizar
        for i in range(1, n-2):
            matriz[i,  i-1:i+2] = np.array([esquerda(delta_x), central(delta_x), direita(delta_x)])

        # Última linha da matriz, levando em consideração a condição de contorno
        matriz[n-2, n-3:n-1] = np.array([esquerda(delta_x), central(delta_x)])

        # Resolve o sistema com essa matriz produzida
        lu, piv = lu_factor(matriz)
        solucao = lu_solve((lu, piv), b)
        
        return solucao, matriz
    

# Construção do sistema de mascaras
def esquerda(delta_x):
    return 1/delta_x**2

def direita(delta_x):
    return 1/delta_x**2

def central(delta_x):
    return -(2 / (delta_x ** 2) + 1)

def funcao_solucao_exata(x):
    return (np.e**(-x) - np.e**(x)) / (np.e**(-1)-np.e)

def main():
    n = 8
    y_inicial = 0
    y_final = 1
    intervalos = np.linspace(y_inicial, y_final, n+1)

    solucao_exata = []
    for x in intervalos:
        solucao_exata.append(funcao_solucao_exata(x))

    solucao, matriz = ProblemaValorContorno.diferenca_finita_pvc1(n, y_inicial, y_final, esquerda, central, direita)
    print(f"Intervalos: {intervalos}")
    print(f"Vetor solucão exata do PVC1:")
    for i in solucao_exata:
        print(i)

    print(f"Vetor solucão aproximada do PVC1")
    for i in solucao:
        print(i)

    print(f"\nMatriz tridiagonal do PVC1 aproximado:")
    for i in matriz:
        print(i)


if __name__ == "__main__":
    main()