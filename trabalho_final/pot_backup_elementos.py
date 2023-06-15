def dividir_intervalos(a, b, tam_matriz):
    passo = (b - a) / (tam_matriz - 1)
    return [a + i * passo for i in range(tam_matriz)]

vetor_de_deslocamentos_matriz_1 = dividir_intervalos(np.floor(minimo_matriz_1[0]), np.ceil(dominante_matriz_1[0]), tam_matriz=matriz_1.shape[0])
vetor_de_deslocamentos_matriz_2 = dividir_intervalos(np.floor(minimo_matriz_2[0]), np.ceil(dominante_matriz_2[0]), tam_matriz=matriz_2.shape[0])
vetor_de_deslocamentos_matriz_3 = dividir_intervalos(np.floor(minimo_matriz_3[0]), np.ceil(dominante_matriz_3[0]), tam_matriz=matriz_3.shape[0])