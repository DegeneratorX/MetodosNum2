# Autovalores e Autovetores

Toda matriz $A$ quadrada tem autovalores $\lambda$ e seus correspondentes autovetores $x$, desde que ela seja diagonalizável. Uma matriz diagonal é quando os números de cima-direito e embaixo-esquerdo são zeros. Exemplo:

$$
\begin{bmatrix}
2 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -1
\end{bmatrix}
$$

é uma matriz diagonal.

Uma matriz qualquer $A$ pode ser diagonalizada se existe alguma matriz P invertível (ou seja, que tem inversa) tal que se multiplicar $P^{-1}$ pela matriz a ser diagonalizada, e depois multiplicar por $P$, resulta em $A$ diagonalizada. 

Ou seja, uma matriz $A$ é diagonalizável se:

$$\boxed{P^{-1}\cdot A\cdot P = D}$$

, onde $D$ é a versão diagonalizada da matriz $A$, e $P$ são os autovetores da matriz $A$ concatenados.

Ou seja, isso é equivalente a dizer que

$$\boxed{A = P\cdot D\cdot P^{-1}}$$

Essa fórmula acima também pode ser definida como a **decomposição espectral** da matriz $A$.

### Exemplo:

Diagonalizar essa matriz: 
$
\begin{bmatrix}
1 & 0 \\
1 & 4
\end{bmatrix}
$

![](2023-06-11-14-44-41.png)

# Método da Potência Regular

O método da potência regular busca encontrar numericamente o autovalor dominante de uma matriz e o autovetor associado a esse autovalor.

![](2023-06-21-17-17-30.png)

# Método da Potência Inversa

O método da potência inversa busca encontrar numericamente o autovalor mínimo de uma matriz e o autovetor associado a esse autovalor.

![](2023-06-22-17-19-34.png)

# Método da Potência com Deslocamento

O método da potência com deslocamento trabalha com chutes iniciais $\lambda _{chute}$ para procurar autovalores intermediários e seus respectivos autovetores. Os chutes normalmente são os valores dentro do intervalo $[\lambda _{min}, \lambda _{max}]$.

Se eu sei o autovalor mínimo e dominante, eu posso deslocar o $\lambda$ a partir do $\lambda _{min}$ e ir iterando chutes até o autovalor máximo, para encontrar um possível autovalor intermediário nesse intervalo.

> Nota: se a matriz for 2x2, os dois autovalores automaticamente são o dominante e o mínimo (podendo inclusive ser iguais), não havendo valores intermediários. Ou existe a possibilidade dela não possuir autovalores caso não seja diagonalizável. Ou seja, não existe autovalor quando não há solução para $Ax = \lambda x$. Se a matriz for 3x3 ou maior, pode (mas não obrigatoriamente) existir autovalores intermediários.

![](2023-06-22-17-20-41.png)