print('Programa de cálculo de salário líquido!\n')

ganhoHora = float(input('Insira quantos reais você ganha por hora trabalhada: '))
horasTrabalhadas = float(input('Insira quantas horas você trabalhou no mês: '))

salarioBruto = ganhoHora * horasTrabalhadas

ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

descontos = ir + inss + sindicato

salarioLiquido = salarioBruto - descontos

print(f'Seu salário bruto é de R${salarioBruto:.2f}!')
print(f'Foram pagos R${ir:.2f} ao Imposto de Renda!')
print(f'Foram pagos R${inss:.2f} ao INSS!')
print(f'Foram pagos R${sindicato:.2f} ao Sindicato!')
print(f'Seu salário líquido é de R${salarioLiquido:.2f}')
