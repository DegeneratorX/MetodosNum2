import numpy as np
import cv2

def aplicar_filtro_gaussiano(image, kernel_tam):
    """
        Essa função recebe uma imagem e um tamanho de kernel como parâmetros. 
        Ela cria um kernel Gaussiano predefinido,normaliza-o e, em seguida, 
        aplica a convolução entre o kernel e a imagem usando um laço for.
        A variável imagem_entrada representa a imagem de entrada com uma borda de pixels adicionada em torno dela. 
        Essa borda é criada para permitir a aplicação de filtros em pixels de borda sem que ocorram erros de indexação.
        O resultado é uma imagem suavizada.
    """
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    kernel = kernel / np.sum(kernel)
    imagem_filtrada = np.zeros_like(image, dtype=np.float64)
    imagem_entrada = np.pad(image, ((1, 1), (1, 1)), mode='constant')

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            regiao = imagem_entrada[i:i+3, j:j+3]
            imagem_filtrada[i, j] = np.sum(regiao * kernel)

    return imagem_filtrada

def aplicar_filtro_sobel(imagem, dx, dy):
    """
    Essa função recebe uma imagem, bem como as direções dx e dy (derivadas parciais), como parâmetros. 
    Com base nas direções especificadas, ela seleciona o kernel de Sobel correspondente (sobel_x ou sobel_y) 
    e realiza a convolução com a imagem. 
    A variável imagem_entrada representa a imagem de entrada com uma borda de pixels adicionada em torno dela. 
    Essa borda é criada para permitir a aplicação de filtros em pixels de borda sem que ocorram erros de indexação.
    O resultado é uma imagem com as derivadas parciais nas direções especificadas.
    """
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    imagem_filtrada = np.zeros_like(imagem, dtype=np.float64)
    imagem_entrada = np.pad(imagem, ((1, 1), (1, 1)), mode='constant')

    if dx == 1 and dy == 0:
        kernel = sobel_x
    elif dx == 0 and dy == 1:
        kernel = sobel_y
    else:
        raise ValueError("dx e dy inválidos. Precisam ser 1 ou 0.")

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            region = imagem_entrada[i:i+3, j:j+3]
            imagem_filtrada[i, j] = np.sum(region * kernel)

    return imagem_filtrada

def aplicar_filtro_gradiente_convolucional(imagem, kernel):
    """
    Função para aplicar filtro de gradiente. 
    Ela recebe uma imagem e um kernel como parâmetros e realiza a convolução entre o kernel e a imagem.
    """
    imagem_filtrada = np.zeros_like(imagem, dtype=np.float64)
    imagem_entrada = np.pad(imagem, ((1, 1), (1, 1)), mode='constant')

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            regiao = imagem_entrada[i:i+3, j:j+3]
            imagem_filtrada[i, j] = np.sum(regiao * kernel)

    return imagem_filtrada



def calcular_gradiente_magnitude(image, threshold):
    """
    Essa função recebe uma imagem e um valor de limite (threshold) como parâmetros. 
    Ela aplica os filtros de Sobel para calcular as derivadas parciais dx e dy. Em seguida, eleva ao quadrado essas derivadas parciais, 
    soma os resultados e tira a raiz quadrada dos elementos. A magnitude do gradiente é obtida. 
    A função retorna uma matriz com valores binários, onde os valores abaixo do limite são 0 e os valores acima do limite são 255.
    """
    dx = aplicar_filtro_sobel(image, 1, 0)
    dy = aplicar_filtro_sobel(image, 0, 1)
    gradiente_quadrado = dx**2 + dy**2
    gradiente_magnitude = np.sqrt(gradiente_quadrado)
    return np.where(gradiente_magnitude < threshold, 0, 1).astype(np.uint8) * 255

# Carregar a imagem de exemplo
imagem = cv2.imread('C:/Users/Samsung/tarefa_1.2/imagem4.jpg', cv2.IMREAD_GRAYSCALE)

# Suavizar a imagem aplicando um filtro Gaussiano
imagem_suavizada = aplicar_filtro_gaussiano(imagem, kernel_tam = 5)

# Aplicar filtro 
imagem_filtro_convol_gradiente = aplicar_filtro_gradiente_convolucional(imagem,kernel = 5)

# Calcular as derivadas parciais nas direções x e y gerando as matrizes A = dx e B = dy
dx = aplicar_filtro_sobel(imagem_suavizada, 1, 0)
dy = aplicar_filtro_sobel(imagem_suavizada, 0, 1)

# Elevar ao quadrado os valores das derivadas
dx_quadrada = dx**2
dy_quadrada = dy**2

# Somar as matrizes A e B modificadas
soma_matrizes_quadradas = dx_quadrada + dy_quadrada

# Tirar a raiz quadrada de cada elemento da matriz
matriz_c = np.sqrt(soma_matrizes_quadradas)

# Escolher um valor de threshold
threshold = 150.0 # quanto menor o thershold mais pixels brancos

# Gerar a matriz final (D)
final_imagem = calcular_gradiente_magnitude(matriz_c, threshold)

# Exibir a imagem final
cv2.imshow('Final Image', final_imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


































