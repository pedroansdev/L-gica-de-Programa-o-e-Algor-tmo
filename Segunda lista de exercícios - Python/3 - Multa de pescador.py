print('Programa de cálculo de rendimento!\n')

peso = float(input('Insira quanto você pegou de peixe(em kg): '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('\nOs valores abaixo são, respectivamente, o excesso de peso que você pegou de acordo com o regulamento, e a multa que você deverá pagar!')
    print(f'Excesso: {excesso:.2f}kg\nMulta: R${multa:.2f}\n')
else:
    excesso = 0
    multa = 0
    print('\nVocê não excedeu nada, portnato...')
    print(f'Excesso: {excesso:.2f}kg\nMulta: R${multa:.2f}\n')
