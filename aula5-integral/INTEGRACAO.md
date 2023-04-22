# Integração Numérica

A integração Numérica consiste em achar integrais (áreas ou volumes) que normalmente não é possível determinar por meio de uma integração analítica. Ou seja, usamos aproximações computacionais com uma tolerância para ter um resultado aproximado da área de uma função de comportamento fora do padrão e que não é possível integrar, usando técnicas de interpolações estudadas em métodos 1, como a de Newton e Lagrange. 

- **Teorema:** se $f$ for integrável em $[a,b]$, então:

$$\boxed{\Large \lim_{x \to \infty} \sum_{i = 1}^{n}f(x_i)\Delta x = \int_{a}^{b}f(x)dx}$$

Com $\Delta x = \frac{b-a}{n}$, e $x_i = a + i\Delta x$. 

Esse teorema nos diz que em um dado intervalo na abscissa $\Delta x$, eu fatio em infinitos pontos $n$ (extremamente pequenos, tendendo a zero de largura) dentro de $\Delta x$ de tal forma que obtenho infinitas alturas $f(x)$ como resultado correspondente, e ao multiplicar base vezes altura daquele intervalo infinitesimal de $x$ com relação ao seu resultado $f(x)$ produzido, obtenho uma área extremamente fina, e somando essas áreas n vezes, sendo $n$ tendendo ao infinito, obtenho a área total do gráfico naquele intervalo em relação a $x$. Isso é integrar. 

- **Teorema:** seja uma função f(x) integrável no intervalo $[a,b]$, então:

$$\boxed{\Large\int_{a}^{b}f(x)dx = F(b) - F(a) \iff F'(x) = f(x)}$$

Esse é o Teorema Fundamental do Cálculo.

O problema é que nem sempre, analiticamente, esse cálculo pode ser feito com $F(x)$, ou é de difícil obtenção. Se esse for o caso e conhecemos somente valores discretos de $f(x)$, então precisamos utilizar métodos numéricos para avaliar a integral de $f(x)$.