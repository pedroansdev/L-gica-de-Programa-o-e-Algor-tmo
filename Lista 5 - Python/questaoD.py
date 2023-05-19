print('Questão D!\nNúmeros sortudos entre 18644 e 33087\n')

sortudo = []

for n in range(18644,33087):
    n = str(n)
    if '2' in n and '7' not in n:
        sortudo.append(n)

qtd = len(sortudo)

print(f'A quantidade de números sortudos entre 18644 e 33087 é {qtd}')
