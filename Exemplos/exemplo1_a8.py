import os
os.system("cls")

# EXEMPLO 2 - Biblioteca para números aleatórios
import random

num = random.randint(0, 5)

print(num)

# EXEMPLO 3 - Funcao que faz o usuario escolher range
def gera_numero(i,f,q):
    # Gera uma lista com numeros aleatorios até chegar na quantidade desejada
    return [random.randint(i, f) for _ in range(q)]


inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
quantidade = int(input("Quantos números você quer gerar? "))

lista = gera_numero(inicio, fim, quantidade)

print(lista)
