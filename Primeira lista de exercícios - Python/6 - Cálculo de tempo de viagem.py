print('Programa de cálculo de duração de uma viagem!\n')

distancia = float(input('Insira a distância percorrida na viagem(em km): '))
velocidade = float(input('Insira a velocidade média do carro durante a viagem(em km/h): '))

tempo = distancia / velocidade

print('O tempo gasto na viagem será de ', tempo, 'h!')
