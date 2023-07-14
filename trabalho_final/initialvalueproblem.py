# Dupla: Victor Martins e Luiz Gustavo
# Turma 2023.1

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

        return altura_maxima, velocidade_atual, tempos[i + 1], tempo_altura_maxima, i

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

        return altura_maxima, velocidade_atual, tempos[i + 1], tempo_altura_maxima, i

    # Método de passo simples: Runge Kutta
    @classmethod
    def runge_kutta(cls, delta_t, velocidade_inicial, altura_inicial, k, massa):
        estados = [[altura_inicial, velocidade_inicial]] # lista de posições do objeto
        velocidade_atual = velocidade_inicial # Vou precisar também da velocidade anterior
        tempos = [0] # lista que guarda valores de tempos pontuais

        altura_maxima = 0 # Maior altura atingida
        tempo_altura_maxima = 0 # Tempo exato que essa altura foi atingida
        i = 0 # Contador

        while estados[i][0] > 0:
            i = i+1
            tempos.append(delta_t * i)


def main():

    velocidade_inicial = 5
    altura_inicial = 200

    k = 0.25
    massa = 2

    for i in range(1,6):
        delta_t = 10**(-i)
        print(f"DELTA T: {delta_t}")
        altura_maxima, velocidade_no_impacto, tempo_total, tempo_altura_maxima, iteracoes = ProblemaValorInicial.euler_implicito(delta_t, velocidade_inicial, altura_inicial, k, massa)

        print(f"numero de iterações: {iteracoes}")
        print("===========================================")

        print(f"Altura máxima alcançada: {altura_maxima}m.")
        print(f"Tempo exato quando essa altura máxima é atingida: {tempo_altura_maxima}s")
        print(f"Tempo total da trajetória até atingir o mar = {tempo_total}s")
        print(f"Velocidade exata do objeto quando atinge o mar: {velocidade_no_impacto}m/s")
        print(f"Massa do objeto: {massa}kg.")
        print(f"Constante k utilizada: {k}kg/s.")
        print()

if __name__ == "__main__":
    main()
