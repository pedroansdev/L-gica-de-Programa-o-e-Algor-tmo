print('Programa para analisar crescimento de países!\n')

popA = 80000
popB = 200000

cresA = 0.03
cresB = 0.015

anos = 0

while popA < popB:
    popA = popA + popA * cresA
    popB = popB + popB * cresB
    anos = anos + 1
    
    if popA > popB:
        print('\nPopulação do pais A ficou maior que o país B!')
        print(f'Após {anos} anos o pais A ficou com {popA:.0f} habitantes, enquanto o país B com{popB:.0f} habitantes!')
        break
