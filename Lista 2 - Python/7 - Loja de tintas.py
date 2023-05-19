print('Programa de cálculo de quantidade de latas de tinta!\n')

metragem = float(input('Indique a metragem do local a ser pintado(em m²): '))

latas = metragem / 54

if metragem % 54 > 0:
    latas = int(latas) + 1
    preço = latas * 80
    print(f'Será necessárias {latas} lata(s) de 18l de tinta para concluir a pintura e a conta ficará por R${preço:.2f}!')
