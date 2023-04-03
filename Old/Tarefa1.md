**Pela série de Taylor**

Por conta da filosofia ser central, existem dois pontos $(x + \Delta x)$ e $(x - \Delta x)$.

Sendo assim, a gente precisa de dois pontos vizinhos em relação a $x$ pra ter uma estimativa de como a função se comporta nesses pontos. E a série de taylor pode ajudar nesse processo.

$f(x+\Delta x) = f(x) + f'(x)\Delta x + \frac{1}{2!}f''(x)(\Delta x)^2+ \frac{1}{3!}f'''(x)(\Delta x)^3 + \frac{1}{4!}f^(iv)(x)(\Delta x)^4 + ...$

E também posso expandir o outro vizinho

$f(x-\Delta x) = f(x) - f'(x)\Delta x + \frac{1}{2!}f''(x)(\Delta x)^2 - \frac{1}{3!}f'''(x)(\Delta x)^3 + \frac{1}{4!}f^(iv)(x)(\Delta x)^4 + ...$

Termos após a quarta derivada é o erro de truncamento da série de taylor, justamente pq a tarefa pede que o erro seja de ordem $(\Delta x)^4$. Se o erro pedido fosse de $(\Delta x)^3$, por exemplo, ai o erro seria após o termo com a terceira derivada.

Combinando as duas séries e isolando a derivada segunda:

$f(x + \Delta x) + f(x - \Delta x) = 2f(x) + f''(x)(\Delta x)^2 + (1/12)f^{iv}(x)(\Delta x)^4 + ...$

$\implies f''(x) = \left(\frac{1}{(\Delta x)^2}\right)[f(x+\Delta x))-2f(x)+f(x-\Delta x)] - \frac{1}{12}f^{iv}(x)(\Delta x)^2 - ...$

Pronto, obtemos a fórmula da segunda derivada usando as expansões de taylor, com erro de ordem $(\Delta x)^4$

**Interpolação**



