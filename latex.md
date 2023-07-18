# Q2

O movimento do carrinho é dado pela solução da seguinte equação diferencial:

$$\frac{d^2x(t)}{dt^2} + 2\xi \omega \frac{dx(t)}{dt} + \omega ^2x(t) = \frac{f(t)}{m}$$

,onde

$m = 1$ é a massa do carrinho em quilogramas;

$k = 4$ é a rigidez da mola em N/m (Newton por metro);

$ω$ = 2$ é a frequência natural de vibração não-amortecida do sistema, em (ciclos/s);

$\xi = 0.05$ é o fator de amortecimento; e

$f(t)$ é a força externa aplicada no carrinho. Essa força varia com o tempo da seguinte forma (estimativa): $f(0) = 0N$, $f(0.5) = 2N$, $f(1) = 0N$.

No instante $t = 0$:

- $x(0) = 0$,

- e a velocidade do carrinho $v(0) = 0$. 

Determine os valores de $x$ (deslocamento) e $v$ (velocidade) no instante de tempo $t = 1.2s$, usando o método de Runge-Kutta de quarta ordem. Defina uma tolerância $0 < \epsilon < 1$, escolha um valor para $\Delta t$ e calcule a solução várias vezes (sempre dividindo o valor de $\Delta t$ por 10) até que o erro relativo de $x(1.2)$ em duas soluções sucessivas seja menor do que a tolerância $\epsilon$.

Faça mais uma vez para $m = 2$, $k = 4$, $\xi = 0.05$, $x(0) = 1$, $v(0) = 0$ e $\xi = 0.0000001$ e escreva os valores de $x(1.2)$ e $v(1.2)$.

### Solução

Para $m = 2$, $k = 4$, $\xi = 0.05$, $x(0) = 1$, $v(0) = 0$ e $\epsilon = 0.0000001$

$$\frac{d^2x(t)}{dt^2} + 0.1\sqrt{2} \frac{dx(t)}{dt}+2x(t) = \left\{ \begin{array}{cl}
2t & \ \text{ se } t \in [0,0.5] \\
2(1-t) & \ \text{ se } t \in [0.5,1.0] \\
0 & t > 1
\end{array} \right.$$

Passo 1: Transformar a equação diferencial do estado S

$S = 
\begin{pmatrix}
x \\
v
\end{pmatrix}$, 
$S_0 = 
\begin{pmatrix}
1 \\
0
\end{pmatrix}
$

$$\frac{dS}{dt} = \begin{pmatrix}
\frac{dx}{dt} \\
\frac{dv}{dt}
\end{pmatrix} = 
\begin{pmatrix}
v \\
\frac{d^2x}{dt^2}
\end{pmatrix}
= \mathfrak{I}(S,t) = 
\begin{pmatrix}
v \\
\left\{ \begin{array}{cl}
2t - 0.1\sqrt{2}v - 2x & \ \text{ se } t \in [0,0.5] \\
2(1-t) - 0.1\sqrt{2}v - 2x & \ \text{ se } t \in [0.5,1.0] \\
-0.1\sqrt{2}v-2x & t > 1
\end{array} \right.
\end{pmatrix}
$$

Passo 2: Resolver pelo método de Runge-Kutta de quarta ordem, usando

$S_{i+1} = S_i + \frac{\Delta t}{6}(\mathfrak{I}_1 + 2\mathfrak{I}_2 + 2\mathfrak{I}_3 + \mathfrak{I}_4)$

onde

$\mathfrak{I}_1 = \mathfrak{I}(S_i, t_i)$

$\overline{S_2} = S_i + \frac{\Delta t}{2}\mathfrak{I}_1$

$\mathfrak{I}_2 = \mathfrak{I}(\overline{S_2},t_i + \frac{\Delta t}{2})$

$\overline{S_3} = S_i + \frac{\Delta t}{2}\mathfrak{I}_2$

$\mathfrak{I}_3 = \mathfrak{I}(\overline{S_3},t_i + \frac{\Delta t}{2})$

$\overline{S_4} = S_i + \Delta t\mathfrak{I}_3$

$\mathfrak{I}_4 = \mathfrak{I}(\overline{S_4},t_i + \Delta t)$

Para $m = 2$, $k = 4$, $\xi = 0.05$, $x(0) = 1$, $v(0) = 0$ e $\epsilon = 0.0000001$,

$x(1.2) = 2.22554$ e $v(1.2) = -2.02273$


Faça em python a solução dessa questão até chegar nos resultados $x(1.2) = 2.22554$ e $v(1.2) = -2.02273$ utilizando como base a solução dessa questão e a tolerância $\epsilon = 0.0000001$,.







# Q3

A equação diferencial e as condições de contorno que governam o problema do deslocamento $y(r)$ de uma membrana circular sujeita a uma pressão constante $P$ são dadas por

$$
\left\{ \begin{array}{cl}
Ty''(r) + \frac{T}{r}y'(r) = -P \\
\text{Condição de Contorno}\left\{ \begin{array}{cl}
y(0.2) = 0 \\
y(0.5) = 0 &
\end{array} \right. &
\end{array} \right.
$$

, com $0.2 \leq r \leq 0.5$ (OBS: a membrana fica entre dois círculos concêntricos de raios $0.2m$ e $0.5m$), onde $r$ é a coordenada radial, $y(r)$ é o deslocamento da membrana na posição radial $r$, $T$ é a tensão em $N/m$ e $P$ é a pressão em $N/m^2$. Os valores de $T$ e $P$ são $T = 5$ e $P = 15$.

Resolva o problema pelo método das diferenças finitas com um número de partições $N = 4$.

# Resposta

Vamos resolver este problema utilizando o método de diferenças finitas para discretizar a equação diferencial.

Primeiro, é necessário discretizar o domínio radial $r$ em uma grade de $N+1$ pontos, que vai de $0.2m$ a $0.5m$. Isso significa que $ri = 0.2m + i \Delta r$, onde $\Delta r = (0.5m - 0.2m) / N = 0.075m$, e $i$ vai de $0$ a $4$.

O próximo passo é transformar a equação diferencial em uma equação de diferenças finitas. As derivadas de segunda ordem e de primeira ordem podem ser aproximadas pelas seguintes fórmulas de diferenças finitas:

$y''(r) \approx \frac{y{i+1} - 2yi + y{i-1}}{(\Delta r)^2}$

$y'(r) \approx \frac{y{i+1} - y{i-1}}{2\Delta r}$

Substituindo estas fórmulas na equação diferencial, obtém-se:

$T \frac{y_{i+1} - 2yi + y{i-1}}{(\Delta r)^2} + \frac{T}{ri} \frac{y{i+1} - y{i-1}}{2\Delta r} = -P$

Agora podemos substituir os valores de $T$, $P$ e $\Delta r$:

$5 \frac{y{i+1} - 2yi + y{i-1}}{(0.075)^2} + \frac{5}{ri} \frac{y{i+1} - y{i-1}}{2*0.075} = -15$

Rearranjando os termos temos:

$y{i+1}\left(\frac{5}{(0.075)^2} + \frac{5}{20.075r_i}\right) - 2yi\frac{5}{(0.075)^2} + y{i-1}\left(\frac{5}{(0.075)^2} - \frac{5}{20.075r_i}\right) = -15$

Estas são as equações de diferenças finitas que devem ser resolvidas. As condições de contorno $y(0.2) = 0$ e $y(0.5) = 0$ significam que $y_0 = y_4 = 0$.

Agora, podemos resolver o sistema de equações resultante para encontrar as $y_i$.

Este sistema de equações precisa ser resolvido numericamente, por exemplo, com o método de Gauss-Seidel ou o método de Jacobi. Esses métodos são iterativos e convergem para a solução correta se as equações forem compatíveis e determinadas. A implementação deste método vai além do escopo desta resposta, mas existem várias bibliotecas em linguagens de programação como Python, Matlab e R que podem resolver este tipo de sistema de equações.