print('Programa de análise de triângulos!\n')

a = float(input('Insira o tamanho do primeiro lado do triângulo: '))
b = float(input('Insira o tamanho do segundo lado do triângulo: '))
c = float(input('Insira o tamanho do terceiro lado do triângulo: '))

if a > abs(b - c) or b > abs(a - c) or c > abs(a - b):

    print('É possível formar um triângulo :)')

    if a == b == c:
        print(f'O triângulo tem todos os lados iguais, se tornando um triângulo equilátero!')
    elif a == b or b == c or a == c:
        print(f'O triângulo tem 2 lados iguais, e 1 diferente, se tornando um triângulo isósceles!')
    else:
        print(f'O triângulo tem 3 lados diferentes, se tornando um triângulo escaleno!')

else:
    print('Não é possível formar um triângulo :(')
