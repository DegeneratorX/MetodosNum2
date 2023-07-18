import numpy as np

import integracao
import autovaloresvetores
import pvi
import pvc

print("="*20)
print("Bem-vindo ao programa de Métodos Numéricos 2")
print("="*20)
while True:
    while True:
        print("Escolha a Unidade com que deseja trabalhar")

        print("1 - Derivação Numérica (Processamento de Imagens)")
        print("2 - Integração Numérica")
        print("3 - Autovalores e Autovetores")
        print("4 - Problema de Valor Inicial (PVI)")
        print("5 - Problema de Valor de Contorno (PVC)")
        print("9 - Sair")

        ans = int(input("Digite (1-5) ou 9 para sair: "))

        if 1 < ans < 6:
            break

        if ans == 9:
            exit()

        if ans == 1:
            print('\nFavor executar o arquivo "processamentoimagens.py".\n\n')
            break
        print("Digito inválido.\n")

    if ans == 2:
        while True:
            print("=============== INTEGRAÇÃO NUMÉRICA ================")
            print("Escolha o método de integração numérica:")
            print("1 - Quadratura de Newton-Cotes.")
            print("2 - Quadratura de Gauss-Legendre.")
            print("3 - Quadratura de Gauss-Hermite.")
            print("4 - Quadratura de Gauss-Laguerre.")
            print("5 - Quadratura de Gauss-Chebychev.")
            print("6 - Exponenciação Simples.")
            print("7 - Exponenciação Dupla.")

            ans_integral = int(input("Digite (1-7): "))

            if 0 < ans_integral < 8:
                break
            print("Digito inválido.\n")
        
        if ans_integral == 1:
            print("=============== NEWTON-COTES ================")
            print("A fórmula a ser integrada será: [sen(2x) + 4x^2 + 3x]^2")
            a = int(input('Digite o valor "a" do intervalo: '))
            b = int(input('Digite o valor "b" do intervalo: '))
            grau = int(input("Digite o grau 1-4 de integração: "))
            filosofia = int(input("Filosofia fechada = 0 ou aberta = 1?: "))
            tol = float(input("Digite a tolerância: "))

            f = lambda x : (np.sin(2*x)+4*x**2+3*x)**2
            integracao.NewtonCotes.integrar(f, a, b, grau, filosofia, tol)

        if ans_integral == 2:
            print("=============== GAUSS-LEGENDRE ================")
            print("A fórmula a ser integrada será: [sen(2x) + 4x^2 + 3x]^2")
            a = int(input('Digite o valor "a" do intervalo: '))
            b = int(input('Digite o valor "b" do intervalo: '))
            grau = int(input("Digite o grau 1-4 de integração: "))
            tol = float(input("Digite a tolerância: "))

            f = lambda x : (np.cos(x))**3 + (np.sen(x))**2
            integracao.GaussLegendre.integrar(f, a, b, grau, tol)

        if ans_integral == 3:
            print("=============== GAUSS-HERMITE ================")
            print("A fórmula a ser integrada será: [sen(2x) + 4x^2 + 3x]^2")
            grau = int(input("Digite o grau 1-4 de integração: "))

            f = lambda x : (np.sin(2*x)+4*x**2+3*x)**2
            integracao.GaussHermite.integrar(f, grau)

        if ans_integral == 4:
            print("=============== GAUSS-LAGUERRE ================")
            print("A fórmula a ser integrada será: [sen(2x) + 4x^2 + 3x]^2")
            grau = int(input("Digite o grau 1-4 de integração: "))

            f = lambda x : (np.sin(2*x)+4*x**2+3*x)**2
            integracao.GaussLaguerre.integrar(f, grau)
        
        if ans_integral == 5:
            print("=============== GAUSS-CHEBYCHEV ================")
            print("A fórmula a ser integrada será: [sen(2x) + 4x^2 + 3x]^2")
            grau = int(input("Digite o grau 1-4 de integração: "))

            f = lambda x : (np.sin(2*x)+4*x**2+3*x)**2
            integracao.GaussChebychev.integrar(f, grau)

        if ans_integral == 6:
            print("=============== EXPONENCIAÇÃO SIMPLES ================")
            print("A fórmula a ser integrada será: 1/(x^2)^(1/3)")
            limite_inferior_a = float(input("Digite o limite inferior a: "))
            limite_superior_b = float(input("Digite o limite superior b: "))
            c = float(input("Digite o c (comece com valores baixos): "))
            grau = int(input("Digite o grau 1-4 de integração: "))
            tol = float(input("Digite a tolerância: "))

            f = lambda x : 1/(x**2)**(1/3)
            integracao.GaussExponenciacao.integrar(f, limite_inferior_a, limite_superior_b, c, grau, True, tol)

        if ans_integral == 7:
            print("=============== EXPONENCIAÇÃO DUPLA ================")
            print("A fórmula a ser integrada será: 1/sqrt((4-x^2))")
            limite_inferior_a = float(input("Digite o limite inferior a: "))
            limite_superior_b = float(input("Digite o limite superior b: "))
            c = float(input("Digite o c (comece com valores baixos): "))
            grau = int(input("Digite o grau 1-4 de integração: "))
            tol = float(input("Digite a tolerância: "))

            f = lambda x : 1/np.sqrt((4-x**2))
            integracao.GaussExponenciacao.integrar(f, limite_inferior_a, limite_superior_b, c, grau, False, tol)

    if ans == 3:
        while True:
            print("=============== AUTOVALORES E AUTOVETORES ================")
            print("Escolha o método de autovalores e autovetores:")
            print("1 - Método da Potência.")
            print("2 - Método de HouseHolder.")
            print("3 - Método QR.")

            ans_auto = int(input("Digite (1-3): "))

            if 0 < ans_auto < 4:
                break
            print("Digito inválido.\n")

        if ans_auto == 1:
            autovaloresvetores.tarefa11()
        if ans_auto == 2:
            autovaloresvetores.tarefa12_hh()
        if ans_auto == 3:
            autovaloresvetores.tarefa12_qr()

    if ans == 4:
        while True:
            print("=============== PROBLEMA DE VALOR INICIAL ================")
            print("Escolha o método de problema de valor inicial:")
            print("1 - Método de Euler")
            print("2 - Método de Runge-Kutta.")
            print("3 - Método de Runge-Kutta AP3")

            ans_pvi = int(input("Digite (1-4): "))

            if 0 < ans_pvi < 5:
                break
            print("Digito inválido.\n")

        if ans_pvi == 1:
            pvi.main_euler()
        if ans_pvi == 2:
            pvi.main_rk()
        if ans_pvi == 3:
            pvi.main_rkprova()

    if ans == 5:
        print("=============== PROBLEMA DE VALOR DE CONTORNO ================")
        pvc.main()