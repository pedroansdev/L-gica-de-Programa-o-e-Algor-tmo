print('Programa de cálculo de descontos!\n')

valor = float(input('Insira o valor atual do produto: '))
porcentagem = float(input('Insira a porcentagem de desconto: '))

desconto = valor * (porcentagem / 100)

valorAtual = valor - desconto

print('\nAqui estão os detalhes do preço de sua compra!')
print('Desconto: R$', desconto)
print('Valor a pagar: R$', valorAtual)
