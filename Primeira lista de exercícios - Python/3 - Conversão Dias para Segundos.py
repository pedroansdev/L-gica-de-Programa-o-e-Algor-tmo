print('Programa de conversão!\nDias, Horas, Minutos -> Segundos\n')

dias = int(input('Estipule uma quantidade de dias: '))
horas = int(input('Agora estipule a quantidade de horas: '))
minutos = int(input('Estipule a quantidade de minutos: '))
segundos = int(input('E por fim, estipule os segundos: '))

conversao = (minutos * 60) + (horas * 3600) + (dias * 86400) + segundos

print('Todos estes valores somados, dão: ', conversao, 's!')
