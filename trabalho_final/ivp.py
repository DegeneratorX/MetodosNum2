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


def main():
    y0 = 200
    v0 = 5
    k = 0.25
    m = 2
    
    for i in range(1,5):
        dt = 10 ** (-i)
        print('--'*8+f' delta t = {dt} '+'--'*8+'\n')
        altura_maxima, v, tempo_total, tempo_altura_maxima, iteracoes = ProblemaValorInicial.euler_explicito(dt, v0, y0, k, m)
        print("Altura máxima da trajetória = ", altura_maxima ,"metros")
        print("Tempo decorrido até a altura máxima = ", tempo_altura_maxima, "segundos")
        print("Tempo total até a queda no mar = ", tempo_total, "segundos")
        print("velocidade no momento do impacto com o mar = ", v, "m/s")
        print(f"numero de iterações: {iteracoes}")


if __name__ == "__main__":
    main()
