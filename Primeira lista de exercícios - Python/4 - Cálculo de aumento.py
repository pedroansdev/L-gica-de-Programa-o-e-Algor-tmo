print('Programa de cálculo de aumentos!\n')

salario = float(input('Insira o valor atual de seu salário: '))
porcentagem = float(input('Insira a porcentagem do aumento: '))

aumento = salario * (porcentagem / 100)

salarioAtual = salario + aumento

print('\nAqui estão os detalhes de seu salário!')
print('Aumento: R$', aumento)
print('Salário Atual: R$', salarioAtual)
