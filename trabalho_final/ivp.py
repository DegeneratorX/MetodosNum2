# Dupla: Victor Martins e Luiz Gustavo
# Turma 2023.1

import numpy as np
from copy import deepcopy
from collections import deque
import matplotlib.pyplot as plt

class ProblemaValorInicial:
    @classmethod
    def euler_explicito(cls, y0, v0, k, massa, delta_t):
        alturas = [y0]
        tempos = [0]
        altura_maxima = 0
        tempo_altura_maxima = 0
        i = 0
        while alturas[i] > 0:
            i += 1
            alturas.append(alturas[i-1] + delta_t * v0)
            tempos.append(delta_t * i)
            velocidade_anterior = v0
            v0 = v0 + delta_t * (-10 - (k/massa) * v0)
            if velocidade_anterior*v0 < 0:
                altura_maxima = alturas[i-1] + (delta_t/2) * v0
                tempo_altura_maxima = tempos[i-1] + delta_t/2

        alturas.append(tempos[i-1]+(delta_t/2)*v0)
        tempos.append(tempos[i-1]+delta_t/2)

        return alturas[i+1], altura_maxima, v0, tempos[i+1], tempo_altura_maxima


def main():
    y0 = 200
    v0 = 5
    k = 0.25
    m = 2
    
    for i in range(1,5):
        dt = 10 ** (-i)
        print('--'*8+f' delta t = {dt} '+'--'*8+'\n')
        altura_valor, altura_maxima, v, tempo_total, tempo_altura_maxima = ProblemaValorInicial.euler_explicito(y0, v0, k, m, dt)
        print("Altura máxima da trajetória = ", altura_maxima ,"metros")
        print("Tempo decorrido até a altura máxima = ", tempo_altura_maxima, "segundos")
        print("Tempo total até a queda no mar = ", tempo_total, "segundos")
        print("velocidade no momento do impacto com o mar = ", v, "m/s")


if __name__ == "__main__":
    main()
