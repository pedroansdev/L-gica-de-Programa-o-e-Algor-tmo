# importando uma biblioteca de contas matemáticas do python
import math

print('Programa de cálculo de redução de vida!\n')

qtdDiaria = int(input('Escreva quantos cigarros você fuma por dia: '))
qtdAnos = int(input('Escreva por quantos anos você é usuário: '))

qtdCigarros = qtdDiaria * (qtdAnos * 365) # qtdAnos * 365 pois aí calcularemos cada dia do ano

minutosReduzidos = qtdCigarros * 10

diasReduzidos = minutosReduzidos/1440

# Arredondando a quantidade de dias para até 1 casa após a vírgula, caso queira 2 casas, multiplica e divide por 100, e assim em diante
diasArredondados = (math.ceil(diasReduzidos*10)/10)

print('Durante sua vida de fumante, você já teve o total de ', diasArredondados,' dias reduzidos na sua vida!')
