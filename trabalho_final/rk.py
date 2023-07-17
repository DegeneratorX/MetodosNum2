import numpy as np

def runge_kutta(h, t_final, m, k, xi, x0, v0, f):
    t = np.arange(0, t_final+h, h)
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0
    omega = np.sqrt(k/m)
    
    for i in range(len(t)-1):
        # Define as derivadas
        dx1 = h * v[i]
        dv1 = h * (f(t[i])/m - 2*xi*omega*v[i] - omega**2*x[i])
        
        dx2 = h * (v[i] + 0.5*dv1)
        dv2 = h * (f(t[i]+0.5*h)/m - 2*xi*omega*(v[i]+0.5*dv1) - omega**2*(x[i]+0.5*dx1))
        
        dx3 = h * (v[i] + 0.5*dv2)
        dv3 = h * (f(t[i]+0.5*h)/m - 2*xi*omega*(v[i]+0.5*dv2) - omega**2*(x[i]+0.5*dx2))
        
        dx4 = h * (v[i] + dv3)
        dv4 = h * (f(t[i+1])/m - 2*xi*omega*(v[i]+dv3) - omega**2*(x[i]+dx3))
        
        # Atualiza os valores de x e v
        x[i+1] = x[i] + (dx1 + 2*dx2 + 2*dx3 + dx4) / 6
        v[i+1] = v[i] + (dv1 + 2*dv2 + 2*dv3 + dv4) / 6
    print(f"Vetor x: {x}")
    print(f"Vetor v: {v}")
    print(f"Vetor t: {t}")
    return x[-1], v[-1]

# Força como função do tempo
def f(t):
    if t < 0.5:
        return 4 * t
    elif t < 1.0:
        return 4 * (1 - t)
    else:
        return 0

# Parametros iniciais
m = 2
k = 4
xi = 0.05
x0 = 1
v0 = 0
t_final = 1.2

# Tamanho do passo inicial
h = 0.1

# Tolerância
eps = 1e-6

x_old, v_old = runge_kutta(h, t_final, m, k, xi, x0, v0, f)

while True:
    h = h / 10
    x_new, v_new = runge_kutta(h, t_final, m, k, xi, x0, v0, f)
    if abs((x_new - x_old) / x_new) < eps:
        break
    x_old, v_old = x_new, v_new

print(f"x(1.2) = {x_new}, v(1.2) = {v_new}")