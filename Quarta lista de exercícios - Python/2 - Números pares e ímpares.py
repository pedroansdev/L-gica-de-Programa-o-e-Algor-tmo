import random

print('Programa de comparação!\nNúmeros pares e ímpares!')

num = random.sample(range(100),20)

listaPar = []
listaImpar = []

for n in num:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print(f'Numeros pares: {listaPar}\nNumeros ímpares: {listaImpar}')

