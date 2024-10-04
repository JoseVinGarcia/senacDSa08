import os

def limpa_tela():
    os.system("cls")

limpa_tela()

# ATIVIDADE 2

def calcula_multa(pp):
    m = (pp - 100) * 4
    return m


peso_padrao = 100.00

print("-"*30)

peso_peixe = float(input("Digite o peso do peixe pescado: "))

if peso_peixe > peso_padrao:
    valor_multa = calcula_multa(peso_peixe)
    print(f"Sua multa será de R$ {valor_multa}.")
else:
    print("Sem multa!")
