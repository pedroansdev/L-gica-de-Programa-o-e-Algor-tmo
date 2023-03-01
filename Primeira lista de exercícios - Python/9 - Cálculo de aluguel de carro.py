print('Programa de cálculo de aluguel de carro!\n')

dias = int(input('Escreva por quantos dias você alugou o carro: '))
km = float(input('Escreva quantos km foram rodados com o carro: '))

aluguel = (dias * 60) + (km * 0.15) 

print('\nValores:\n60 reais o dia alugado\nR$0,15 por km rodado\n')

print('O valor total do aluguel do carro ficou em R$', aluguel)

