# Q2

Para mostrar que a função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$ é primitiva recursiva, precisamos demonstrar que ela pode ser obtida a partir das funções iniciais e das operações de composição e recursão primitiva.

As funções iniciais são:

- A função zero: $z(x) = 0$ para todo $x$.
- A função sucessor: $s(x) = x + 1$ para todo $x$.
- As funções projeção: $p_i^n(x_1, \ldots, x_n) = x_i$ para todo $i \leq n$ e para todo $(x_1, \ldots, x_n)$.

As operações de composição e recursão primitiva são:

- Composição: Se $h(x_1, \ldots, x_n)$ e $g_1(x_1, \ldots, x_n), \ldots, g_m(x_1, \ldots, x_n)$ são funções primitivas recursivas, então $h(g_1(x_1, \ldots, x_n), \ldots, g_m(x_1, \ldots, x_n))$ também é primitiva recursiva.
- Recursão primitiva: Se $h(x_1, \ldots, x_n)$ e $g(x_1, \ldots, x_n, y)$ são funções primitivas recursivas, então a função $f(x_1, \ldots, x_n, y)$ definida por
    - $f(x_1, \ldots, x_n, 0) = h(x_1, \ldots, x_n)$
    - $f(x_1, \ldots, x_n, s(y)) = g(x_1, \ldots, x_n, y, f(x_1, \ldots, x_n, y))$
também é primitiva recursiva.

Dado que $f(x)$ é primitiva recursiva, podemos construir a função $g(x)$ usando as operações de composição e recursão primitiva.

- Primeiro, definimos a função auxiliar $h(x, y) = x - y^2$. Como a subtração e a multiplicação são primitivas recursivas, a função $h$ também é primitiva recursiva.

- Agora, definimos a função $r(x, y) = sgn(h(f(x), y))$, onde $sgn(x)$ é a função sinal que retorna 0 se $x = 0$, 1 se $x > 0$ e -1 se $x < 0$. A função sinal e a composição são primitivas recursivas, então a função $r$ também é primitiva recursiva.

- Vamos utilizar a recursão primitiva para construir a função $g'(x, y)$, onde $g'(x, 0) = 0$ e $g'(x, s(y)) = g'(x, y) + r(x, s(y))$. Como a adição e a recursão primitiva são primitivas recursivas, a função $g'$ também é primitiva recursiva.

- A função $g(x) = g'(x, f(x))$ é obtida por composição das funções primitivas recursivas $g'$ e $f$. Para mostrar que $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$, analisaremos o comportamento da função $g'(x, y)$.

Lembre-se de que $g'(x, y)$ retorna o valor acumulado da função $r(x, y)$ para $y = 0, 1, 2, \ldots, f(x)$. A função $r(x, y)$ é 1 sempre que $y^2 < f(x)$ e 0 caso contrário. Isso significa que $g'(x, y)$ conta quantos valores de $y$ satisfazem $y^2 < f(x)$.

Quando $y = \left\lfloor \sqrt{f(x)} \right\rfloor + 1$, temos que $y^2 > f(x)$, e $r(x, y) = 0$. Portanto, a partir desse ponto, a função $g'(x, y)$ não acumula mais valores. Então, $g'(x, f(x))$ conta todos os valores de $y$ que satisfazem $y^2 < f(x)$ até o valor máximo de $y$, que é $f(x)$. Isso é exatamente o valor $\left\lfloor \sqrt{f(x)} \right\rfloor$.

Como $g(x) = g'(x, f(x))$ é obtida por composição de funções primitivas recursivas e é igual a $\left\lfloor \sqrt{f(x)} \right\rfloor$, concluímos que a função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$ é primitiva recursiva.


### Concisa

Para mostrar que a função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$ é primitiva recursiva, usaremos as operações de composição e recursão primitiva:

- Defina a função $h(x, y) = x - y^2$, que é primitiva recursiva.
- Defina a função $r(x, y) = sgn(h(f(x), y))$, que é primitiva recursiva.
- Use a recursão primitiva para definir $g'(x, y)$, onde $g'(x, 0) = 0$ e $g'(x, s(y)) = g'(x, y) + r(x, s(y))$. A função $g'$ é primitiva recursiva.
- Finalmente, defina $g(x) = g'(x, f(x))$, que é primitiva recursiva e igual a $\left\lfloor \sqrt{f(x)} \right\rfloor$.

Assim, a função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$ é primitiva recursiva.

### Função Sinal

Claro! A função sgn() é conhecida como função sinal. Ela recebe um número real como entrada e retorna um valor que indica o "sinal" desse número. Em outras palavras, a função sinal classifica o número em três categorias: positivo, negativo ou zero. A definição da função sinal é a seguinte:

$$sgn(x) = \left\{ \begin{array}{cl}
1 & se \ x > 0 \\
0 & se \ x = 0 \\
-1 & se \ x < 0
\end{array} \right.$$

No contexto daquela resposta, a função sinal era usada para determinar se um valor de $y^2$ era menor que $f(x)$. A função $r(x, y) = sgn(h(f(x), y))$ retornaria 1 se $y^2 < f(x)$ e 0 caso contrário. Isso era útil para contar quantos valores de $y$ satisfazem $y^2 < f(x)$, o que, por sua vez, nos permitiu calcular $\left\lfloor \sqrt{f(x)} \right\rfloor$.

### Responsta Concisa sem sgn()

Sim, é possível mostrar que a função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$ é primitiva recursiva sem usar a função sinal ($sgn()$) e de forma concisa. Vamos usar a propriedade de minimização, que é garantida para funções primitivas recursivas.

- Defina a função $h(x, y) = (y + 1)^2 - f(x)$, que é primitiva recursiva, pois a adição, a multiplicação e a subtração são primitivas recursivas.
- Defina a função $m(x, y) = \min{y' \mid h(x, y') = 0}$, que retorna o menor valor de $y'$ para o qual $h(x, y') = 0$. Como $h$ é primitiva recursiva, a função $m$ também é primitiva recursiva.
- Finalmente, defina $g(x) = m(x, f(x)) - 1$. Como a função $m$ é primitiva recursiva e a subtração é primitiva recursiva, a função $g$ também é primitiva recursiva.

A função $g(x) = \left\lfloor \sqrt{f(x)} \right\rfloor$, pois ela retorna o menor valor $y$ tal que $(y + 1)^2 > f(x)$, e então subtrai 1 para obter $\left\lfloor \sqrt{f(x)} \right\rfloor$.

# Q3

Considere uma função unária $f$ computável que seja estritamente crescente, ou seja, para todo $i \in \mathbb{N}$, $f(i) < f(i+1)$. Mostre que o predicado

$$P(x) = \left\{ \begin{array}{cl}
1 &  \ se \ existe \ j \ tal \ que \ f(j) = x \\
0 & : \ caso \ contário
\end{array} \right.$$

é também computável.

Outra pergunta. E se a função $f$ não fosse estritamente crescente, a sua estratégia para mostrar que o predicado $P(x)$ é computável continuaria funcionando? Justifique intuitivamente (sem muita preocupação com formalismos, mas de maneira clara) a sua resposta.

Responda as duas

### RESPOSTA

**Mostrando que $P(x)$ é computável quando $f$ é estritamente crescente:**

Se $f$ é uma função computável e estritamente crescente, então para cada valor $i \in \mathbb{N}$, temos $f(i) < f(i+1)$. Podemos usar essa propriedade para decidir o predicado $P(x)$.

Construa um algoritmo para computar $P(x)$:

- Inicialize $i$ com 0.
- Calcule $f(i)$.
- Se $f(i) = x$, retorne 1, pois encontramos um $j$ tal que $f(j) = x$.
- Se $f(i) > x$, retorne 0, pois como $f$ é estritamente crescente, não existirá um $j > i$ tal que $f(j) = x$.
- Incremente $i$ e vá para o passo 2.
Como o algoritmo acima sempre termina e retorna o valor correto para o predicado $P(x)$, temos que $P(x)$ é computável quando $f$ é estritamente crescente.

**Se a função $f$ não fosse estritamente crescente:**

Se $f$ não fosse estritamente crescente, a estratégia descrita acima não funcionaria diretamente, pois não poderíamos garantir que não haveria um valor $j > i$ tal que $f(j) = x$ se $f(i) > x$. Nesse caso, teríamos que modificar nossa abordagem.

Uma possível estratégia seria encontrar limites superior e inferior para o valor de $j$ (se existir) tal que $f(j) = x$. Se pudéssemos fazer isso e os limites fossem finitos, poderíamos verificar todos os valores de $j$ nesse intervalo e decidir se $f(j) = x$ para algum $j$. Entretanto, essa estratégia dependeria das propriedades específicas de $f$ e, em geral, não podemos garantir que $P(x)$ seja computável para qualquer função computável $f$ que não seja estritamente crescente.

# Q4

Sejam $P_1(x)$, $P_2(x)$ e $P_3(x)$ três predicatos tais que para todo $x \in \mathbb{N}$, $P_1(x) \wedge P_2(x) = P_1(x) \wedge P_3(x) = P_2(x) \wedge P_3(x) = 0$. Isso é a mesma coisa que dizer que nunca dois desses predicados vão retornar 1 (verdadeiro) ao mesmo tempo, embora os três podem retornar 0 (falso) ao mesmo tempo. Além disso, assuma que há três funções parcialmente computáveis $f_1$, $f_2$ e $f_3$ com as seguintes propriedades:

$$f_1(x) = \left\{ \begin{array}{cl}
1 &  \ se \ P_1(x) \vee P_2(x) \\
2 &  \ se \ P_3(x) \\
\uparrow  & caso \ contrário
\end{array} \right.$$

$$f_2(x) = \left\{ \begin{array}{cl}
\uparrow &  \ se \ P_1(x) \vee P_3(x) \\
0 &  \ caso \ contrário
\end{array} \right.$$

$$f_3(x) = \left\{ \begin{array}{cl}
\uparrow &  \ se \ P_2(x) \vee P_3(x) \\
0 &  \ caso \ contrário
\end{array} \right.$$

Prove que

$$f_2(x) = \left\{ \begin{array}{cl}
1 &  \ se \ P_2(x) \\
\uparrow &  \ se \ \neg P_2(x)
\end{array} \right.$$

é parcialmente computável.

Dica: nessa pergunta, você deverá construir um programa em nossa linguagem $\mathscr{L}$ que compute a função $f(x)$. Você poderá usar as macros para $f_1$, $f_2$ e $f_3$ nessa empreitada, já que elas são parcialmente computáveis. No entanto, não podemos usar macros para $P_1(x)$, $P_2(x)$ e $P_3(x)$, pois não sabemos se elas são computáveis.

### Resposta concisa

Vamos construir um programa em $\mathscr{L}$ que compute $f_2(x)$:

1. Calcule $y_1 = f_1(x)$.
2. Se $y_1 = 1$, vá para o passo 3; caso contrário, vá para o passo 4.
3. Retorne $\uparrow$.
4. Calcule $y_2 = f_3(x)$.
5. Se $y_2 = 0$, retorne 1; caso contrário, retorne $\uparrow$.

O programa acima utiliza as funções parcialmente computáveis $f_1$ e $f_3$. Se $P_2(x)$ é verdadeiro, então $f_1(x) \neq 1$ e $f_3(x) = 0$, então o programa retorna 1. Se $P_2(x)$ é falso, então $f_1(x) = 1$ e o programa retorna $\uparrow$. Portanto, $f_2(x)$ é parcialmente computável.

### Pseudocodigo

Aqui está o pseudocódigo para calcular a função $f_2(x)$:

```
function f2(x):
    y1 = f1(x)
    
    if y1 == 1:
        return undefined
    else:
        y2 = f3(x)
        
        if y2 == 0:
            return 1
        else:
            return undefined
```

Este programa utiliza as funções parcialmente computáveis $f_1$ e $f_3$. Se $P_2(x)$ é verdadeiro, então $f_1(x) \neq 1$ e $f_3(x) = 0$, então o programa retorna 1. Se $P_2(x)$ é falso, então $f_1(x) = 1$ e o programa retorna indefinido. Portanto, $f_2(x)$ é parcialmente computável.

# Q5

Seja a função

$$f(x) = \left\{ \begin{array}{cl}
0 &  \ se \ x = 0 \\
f(x-1) + 2x - 1 &  \ caso \ contrário
\end{array} \right.$$

Demonstre que $f(x)$ é primitiva recursiva.

### Resposta

Para mostrar que a função $f(x)$ é primitiva recursiva, precisamos expressá-la usando as funções iniciais e as operações de composição e recursão primitiva. A definição de $f(x)$ já está na forma de uma recursão primitiva. Vamos analisar seus componentes:

- Caso base: $f(x) = 0$ se $x = 0$. A função zero é uma função inicial primitiva recursiva.

- Caso recursivo: $f(x) = f(x-1) + 2x - 1$ para $x > 0$. Podemos expressar esse caso usando funções e operações primitivas recursivas:

    a. A função predecessora $p(x) = x - 1$ é primitiva recursiva.

    b. A função $g(x) = 2x - 1$ é primitiva recursiva, pois a multiplicação por uma constante e a subtração são primitivas recursivas.

    c. A função $h(x) = f(p(x)) + g(x)$ é primitiva recursiva, pois a composição de funções primitivas recursivas também é primitiva recursiva.

- Usando a recursão primitiva, podemos definir a função $f(x)$ da seguinte maneira:

    - $f(0) = 0$ (caso base)
    
    - $f(s(x)) = h(x)$, onde $s(x)$ é a função sucessor (caso recursivo)

Como a função $f(x)$ é construída usando as funções iniciais e as operações de composição e recursão primitiva, ela é primitiva recursiva.