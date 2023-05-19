print('Programa que verifica o maior e menor número!\n')

a = float(input('Insira um número a ser comparado: '))
b = float(input('Insira o outro número para a comparação: '))
c = float(input('Insira o último número para a comparação: '))

numeros = (a, b, c)
maior = max(numeros)
menor = min(numeros)

print(f'O maior número entre os 3 é {maior}, já o menor é {menor}!')
