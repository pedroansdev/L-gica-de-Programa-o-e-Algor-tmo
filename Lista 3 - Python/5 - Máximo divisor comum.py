print('Programa para calcular o MDC!\n')

a = int(input('Primeiro número para o MDC: '))
b = int(input('Segundo número para o MDC: ')) 

while a%b != 0:
    a, b = b, a%b
    
    if a%b == 0:
        print(f'O MDC é {b}!')

