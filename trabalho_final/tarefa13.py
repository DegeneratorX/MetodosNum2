# Dupla: Victor Martins e Luiz Gustavo
# Turma 2023.1
import numpy as np
G = 9.8

class ProblemaValorInicial:
    # Euler explícito: calcula a solução do próximo passo de tempo através 
    # do passo de tempo atual
    @classmethod
    def euler_explicito(cls, delta_t, velocidade_inicial, altura_inicial, k, massa):
        alturas = [altura_inicial] # lista de posições do objeto
        velocidade_atual = velocidade_inicial # Vou precisar também da velocidade anterior
        tempos = [0] # lista que guarda valores de tempos pontuais

        altura_maxima = 0 # Maior altura atingida
        tempo_altura_maxima = 0 # Tempo exato que essa altura foi atingida
        i = 0 # Contador

        while alturas[i] > 0: # Enquanto nenhuma altura listada atingiu o solo
            i += 1
            alturas.append(alturas[i-1] + velocidade_atual * delta_t) # Fórmula y0 + v0t. Pego a altura anterior para formar a nova
            tempos.append(delta_t * i) # Cálculo do novo tempo

            velocidade_anterior = velocidade_atual # Velocidade atual vira a anterior
            velocidade_atual = velocidade_atual + delta_t * (-G - (k/massa) * velocidade_atual) # Cálculo do método de Euler Explícito F(S_0, t_0), como mostrado no doc

             # Se o produto da velocidade anterior e atual for negativo, significa
             # que o objeto atingiu a altura máxima.
            if velocidade_anterior * velocidade_atual < 0:
                altura_maxima = alturas[i-1] + velocidade_atual * (delta_t/2)
                tempo_altura_maxima = tempos[i-1] + delta_t/2

        # Cálculo da posição e tempo final
        alturas.append(alturas[i-1] + (delta_t/2) * velocidade_atual)
        tempos.append(tempos[i-1] + delta_t/2)

        return altura_maxima, velocidade_atual, tempos[i+1], tempo_altura_maxima, i


    @classmethod
    def euler_implicito(cls, delta_t, velocidade_inicial, altura_inicial, k, massa):
        alturas = [altura_inicial] # lista de posições do objeto
        velocidade_atual = velocidade_inicial # Vou precisar também da velocidade anterior
        tempos = [0] # lista que guarda valores de tempos pontuais

        altura_maxima = 0 # Maior altura atingida
        tempo_altura_maxima = 0 # Tempo exato que essa altura foi atingida
        i = 0 # Contador

        while alturas[i] > 0: # Enquanto nenhuma altura listada atingiu o solo
            i += 1
            alturas.append(alturas[i-1]+((massa*delta_t)/(massa+k*delta_t))*(velocidade_atual-10*delta_t)) # Fórmula y0 + v0t. Pego a altura anterior para formar a nova
            tempos.append(delta_t * i) # Cálculo do novo tempo

            velocidade_anterior = velocidade_atual # Velocidade atual vira a anterior
            velocidade_atual = (massa/(massa+k*delta_t))*(velocidade_atual-10*delta_t) # Cálculo do método de Euler Explícito F(S_0, t_0), como mostrado no doc

             # Se o produto da velocidade anterior e atual for negativo, significa
             # que o objeto atingiu a altura máxima.
            if velocidade_anterior * velocidade_atual < 0:
                altura_maxima = alturas[i-1] + ((massa*(delta_t/2))/(massa+k*(delta_t/2)))*(velocidade_atual-10*delta_t)
                tempo_altura_maxima = tempos[i-1] + delta_t/2

        # Cálculo da posição e tempo final
        alturas.append(alturas[i-1] + ((massa*(delta_t/2))/(massa+k*(delta_t/2)))*(velocidade_atual-10*delta_t))
        tempos.append(tempos[i-1] + delta_t/2)

        return altura_maxima, velocidade_atual, tempos[i+1], tempo_altura_maxima, i


    # Método de passo simples: Runge Kutta
    @classmethod
    def runge_kutta(cls, f, delta_t, velocidade_inicial, altura_inicial, k, massa):
        estados = [[altura_inicial, velocidade_inicial]] # lista de posições e velocidades instantâneas do objeto
        tempos = [0] # lista que guarda valores de tempos pontuais

        altura_maxima = 0 # Maior altura atingida
        tempo_altura_maxima = 0 # Tempo exato que essa altura foi atingida
        i = 0 # Contador (de iterações e de índices de Estado)

        # Loop que verifica se a altura não é zero, pois se for, atingiu o solo
        while estados[i][0] > 0:
            i += 1
            tempos.append(delta_t * i)

            # Fórmulas de Runge-Kutta para estimar o próximo estado
            rk1 = estados[i-1] + (delta_t/2) * f(estados[i-1], k, massa)
            rk2 = estados[i-1] + delta_t*(-f(estados[i-1], k, massa) + 2*f(rk1, k, massa))

            # O próximo estado é definitivamente calculado usando a fórmula de Runge-Kutta
            estados.append(estados[i-1] + (delta_t/6) * (f(estados[i-1], k, massa) + 4*f(rk1, k, massa) + f(rk2, k, massa)))

            # Se o objeto atingiu a altura máxima na trajetória, ou seja, sua velocidade muda de sinal
            if (estados[i-1][1] * estados[i][1]) < 0:
                tempo_altura_maxima = tempos[i-1] + delta_t/2 # O tempo e o estado são guardados
                rk1 = estados[i-1] + (delta_t/4) * f(estados[i-1], k, massa)
                rk2 = estados[i-1] + (delta_t/2) * (-f(estados[i-1], k, massa) + 2*f(rk1, k, massa))
                altura_maxima = (estados[i-1] + (delta_t/12) * (f(estados[i-1], k, massa) + 4*f(rk1, k, massa) + f(rk2, k, massa)))[0]

        # Após atingir o solo, faz um último cálculo para saber o último estado e a velocidade do impacto com o mar
        tempos.append(tempos[i-1] + delta_t/2)
        rk1 = estados[i-1] + (delta_t/4) * f(estados[i-1], k, massa)
        rk2 = estados[i-1] + (delta_t/2) * (-f(estados[i-1], k, massa) + 2*f(rk1, k, massa))
        estados.append((estados[i-1] + (delta_t/12) * (f(estados[i-1], k, massa) + 4*f(rk1, k, massa) + f(rk2, k, massa))))

        return altura_maxima, estados[i+1][1], tempos[i+1], tempo_altura_maxima, i


    @classmethod
    def runge_kutta_prova(cls, f, delta_t, velocidade_inicial, distancia_inicial, k, massa, tempo_final, qsi):
        tempos = np.arange(0, tempo_final+delta_t, delta_t) # Vetor de tempos que contem, no intervalo [0,tempo_final+delta_t], N delta_t's.
        x = np.zeros(len(tempos)) # Crio vetores de espaço e velocidade do tamanho do número de passos de tempo
        v = np.zeros(len(tempos))

        x[0] = distancia_inicial
        v[0] = velocidade_inicial
        omega = np.sqrt(k/massa) # Cálculo direto do omega.
        
        for i in range(len(tempos)-1):
            # Define as derivadas
            dx1 = delta_t * v[i]
            dv1 = delta_t * (f(tempos[i])/massa - 2*qsi*omega*v[i] - omega**2*x[i])
            
            dx2 = delta_t * (v[i] + 0.5*dv1)
            dv2 = delta_t * (f(tempos[i]+0.5*delta_t)/massa - 2*qsi*omega*(v[i]+0.5*dv1) - omega**2*(x[i]+0.5*dx1))
            
            dx3 = delta_t * (v[i] + 0.5*dv2)
            dv3 = delta_t * (f(tempos[i]+0.5*delta_t)/massa - 2*qsi*omega*(v[i]+0.5*dv2) - omega**2*(x[i]+0.5*dx2))
            
            dx4 = delta_t * (v[i] + dv3)
            dv4 = delta_t * (f(tempos[i+1])/massa - 2*qsi*omega*(v[i]+dv3) - omega**2*(x[i]+dx3))
            
            # Atualiza os valores de x e v com Runge-Kutta
            x[i+1] = x[i] + (dx1 + 2*dx2 + 2*dx3 + dx4)/6
            v[i+1] = v[i] + (dv1 + 2*dv2 + 2*dv3 + dv4)/6

        return x[-1], v[-1] # Retorno o último no t = 1.2
    

# Função para Runge-Kutta
def f(estados, k, massa):
    return np.array([estados[1], -10-(k/massa) * estados[1]])


# Função para Runge-Kutta da prova
def forca(tempo):
    if tempo < 0.5:
        return 4 * tempo
    elif tempo < 1.0:
        return 4 * (1 - tempo)
    else:
        return 0


def main_euler():
    velocidade_inicial = 5
    altura_inicial = 200

    k = 0.25
    massa = 2

    for i in range(1,6):
        delta_t = 10**(-i)

        print()
        print(f"DELTA T: {delta_t}")
        altura_maxima, velocidade_no_impacto, tempo_total, tempo_altura_maxima, iteracoes = ProblemaValorInicial.euler_implicito(delta_t, velocidade_inicial, altura_inicial, k, massa)

        print(f"numero de iterações: {iteracoes}")
        print("===========================================")

        print(f"Altura máxima alcançada: {altura_maxima:8f}m.")
        print(f"Tempo exato quando essa altura máxima é atingida: {tempo_altura_maxima:8f}s")
        print(f"Tempo total da trajetória até atingir o mar = {tempo_total:8f}s")
        print(f"Velocidade exata do objeto quando atinge o mar: {velocidade_no_impacto:8f}m/s")
        print(f"Massa do objeto: {massa}kg.")
        print(f"Constante k utilizada: {k}kg/s.")
        print()

def main_rk():
    velocidade_inicial = 5
    altura_inicial = 200

    k = 0.25
    massa = 2
    
    for i in range(1,6):
        delta_t = 10**(-i)

        print()
        print(f"DELTA T: {delta_t}")
        altura_maxima, velocidade_no_impacto, tempo_total, tempo_altura_maxima, iteracoes = ProblemaValorInicial.runge_kutta(f, delta_t, velocidade_inicial, altura_inicial, k, massa)
        
        print(f"numero de iterações: {iteracoes}")
        print("===========================================")

        print(f"Altura máxima alcançada: {altura_maxima:8f}m.")
        print(f"Tempo exato quando essa altura máxima é atingida: {tempo_altura_maxima:8f}s")
        print(f"Tempo total da trajetória até atingir o mar = {tempo_total:8f}s")
        print(f"Velocidade exata do objeto quando atinge o mar: {velocidade_no_impacto:8f}m/s")
        print(f"Massa do objeto: {massa}kg.")
        print(f"Constante k utilizada: {k}kg/s.")

def main_rkprova():
    velocidade_inicial = 0
    distancia_inicial = 1

    k = 4
    massa = 2
    qsi = 0.05

    tempo_final = 1.2
    delta_t = 0.1 # Começo com passo 0.1

    # Tolerância
    tol = 1e-6

    distancia_velha, velocidade_velha = ProblemaValorInicial.runge_kutta_prova(forca, delta_t, velocidade_inicial, distancia_inicial, k, massa, tempo_final, qsi)

    while True:
        delta_t /= 10
        distancia_nova, velocidade_nova = ProblemaValorInicial.runge_kutta_prova(forca, delta_t, velocidade_inicial, distancia_inicial, k, massa, tempo_final, qsi)
        if abs((distancia_nova - distancia_velha) / distancia_nova) < tol:
            break
        distancia_velha, velocidade_velha = distancia_nova, velocidade_nova

    print(f"x(1.2) = {distancia_nova}, v(1.2) = {velocidade_nova}")


if __name__ == "__main__":
    main_rk()
