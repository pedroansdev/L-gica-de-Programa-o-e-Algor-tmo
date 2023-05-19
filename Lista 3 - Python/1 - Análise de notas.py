print('Programa para analisar uma nota!\nVálida/Inválida\n')

nota = float(input('Digite uma nota: '))

while nota < 0 or nota > 10:
    print('\nNota inválida! Tente novamente...')
    nota = float(input('Digite uma nota: '))

    if nota >= 0 and nota <= 10:
        print('\nNota válida!')
        break
