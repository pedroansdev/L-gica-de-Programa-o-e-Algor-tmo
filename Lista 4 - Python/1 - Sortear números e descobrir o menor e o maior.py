import random

print('Programa de comparação!\nSorteando numeros aleatorios e vendo o maior e menor!\n')

sorteados = []
maior = 1
menor = 100

for aleatorio in range(10):
    aleatorio = random.randint(1,100)
    
    if aleatorio > maior:
        maior = aleatorio
        
    if aleatorio < menor:
        menor = aleatorio
        
    sorteados.append(aleatorio)
    
print(f'Dos números sorteados temos as seguintes informações: \nMenor Número: {menor}\nMaior Número: {maior}')
