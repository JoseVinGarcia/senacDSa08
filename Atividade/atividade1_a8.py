import os
import random

def decoracao():
    print(12 * "-")


def limpa_tela():
    os.system("cls")


# ATIVIDADE 1 - Funções soma, subtração, multiplicação e divisão

def gerar_numeros():
    a = random.randint(0,99)
    b = random.randint(0,99)
    return a,b


def soma(a,b):
    return a + b


def subtracao(a,b):
    return a - b


def multiplicacao(a,b):
    return a * b


def divisao(a,b):
    return a / b


limpa_tela()
decoracao()
print("CALCULADORA")

numero1, numero2 = gerar_numeros()

print(f"\nO primeiro número é {numero1}, o segundo número é {numero2}")

print(f"\nA soma é: {soma(numero1,numero2)}")

print(f"A subtração é: {subtracao(numero1,numero2)}")

print(f"A multiplicação é: {multiplicacao(numero1,numero2)}")

print(f"A divisão é: {divisao(numero1,numero2)}")
