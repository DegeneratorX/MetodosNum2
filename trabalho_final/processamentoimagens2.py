import numpy as np
import cv2

def aplicar_filtro_Gaussiano(imagem, kernel_tam):
    """
    Aplica o filtro Gaussiano em uma imagem.
    Essa função recebe a imagem de entrada e o tamanho do kernel do filtro.
    A variável imagem_entrada representa a imagem de entrada com uma borda de pixels adicionada em torno dela. 
    Essa borda é criada para permitir a aplicação de filtros em pixels de borda sem que ocorram erros de indexação.
    É retornada a imagem filtrada após a aplicação do filtro Gaussiano.
    """
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    kernel = kernel / np.sum(kernel)
    imagem_filtrada = np.zeros_like(imagem, dtype=np.float64)
    imagem_entrada = np.pad(imagem, ((1, 1), (1, 1)), mode='constant')

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            regiao = imagem_entrada[i:i+3, j:j+3]
            imagem_filtrada[i, j] = np.sum(regiao * kernel)

    return imagem_filtrada


def aplicar_filtro_laplace(imagem):
    """
    Aplica o filtro convolucional de Laplace em uma imagem.
    Essa função recebe imagem de entrada.
    A variável imagem_entrada representa a imagem de entrada com uma borda de pixels adicionada em torno dela. 
    Essa borda é criada para permitir a aplicação de filtros em pixels de borda sem que ocorram erros de indexação.
    Retorna a imagem filtrada após a aplicação do filtro convolucional de Laplace.
    """
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    imagem_filtrada = np.zeros_like(imagem, dtype=np.float64)
    imagem_entrada = np.pad(imagem, ((1, 1), (1, 1)), mode='constant')

    for i in range(1, imagem.shape[0] + 1):
        for j in range(1, imagem.shape[1] + 1):
            regiao = imagem_entrada[i-1:i+2, j-1:j+2]
            imagem_filtrada[i-1, j-1] = np.sum(regiao * kernel)

    return imagem_filtrada.astype(np.uint8)



# Carregar a imagem de exemplo
imagem = cv2.imread('C:/Users/Samsung/tarefa_1.2/imagem4.jpg', cv2.IMREAD_GRAYSCALE)

# Suavizar a imagem aplicando um filtro Gaussiano
imagem_suavizada = aplicar_filtro_Gaussiano(imagem, kernel_tam=5)

# Aplicar o filtro convolucional de Laplace
imagem_laplace = aplicar_filtro_laplace(imagem_suavizada)

# Gerar a matriz B
tolerance = 50.6 # quanto maior a tolerancia, menos pixels brancos.
final_imagem = np.where(np.abs(imagem_laplace) > tolerance, 255, 0).astype(np.uint8)

# Exibir a imagem final
cv2.imshow('Final Image', final_imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
