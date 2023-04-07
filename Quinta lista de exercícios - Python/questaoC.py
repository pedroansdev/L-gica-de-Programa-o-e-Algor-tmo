print('Questão C!\nQuantos números divisíveis por 2 e 7 existem no range de 1067 - 3627?\n')

#para i = 1 até 9
#   se i != 3, então
#       para j = 1 até 6
#           imprime 'oi'

divisivel = []

for n in range(1067,3628):
    if n % 2 == 0 and n % 7 == 0:
        divisivel.append(n)
    qtd = len(divisivel)

print(f'A quantidade de números divisíveis por 2 e 7 neste range é {qtd}')
