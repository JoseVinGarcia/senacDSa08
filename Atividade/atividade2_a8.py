import os

def limpa_tela():
    os.system("cls")

limpa_tela()

# ATIVIDADE 2

def calcula_multa(pp):
    m = (pp - LIMITE) * MULTA
    return m

MULTA = 4
LIMITE = 100.00

print("-"*30)

peso_peixe = float(input("Digite o peso do peixe pescado: "))

if peso_peixe > LIMITE:
    valor_multa = calcula_multa(peso_peixe)
    print(f"Sua multa será de R$ {valor_multa}.")
else:
    print("Sem multa!")
