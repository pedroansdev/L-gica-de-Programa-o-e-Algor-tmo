print('Programa sobre sequência de Fibonacci!\n')

num = int(input('Escreva o número para a sequência de Fibonacci: '))

a = 1
b = 1
count = 0

while count <= num - 2:
    
    print(f'F{count} = {b}')

    a, b = b, a+b

    count += 1

