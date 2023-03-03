print('Programa para analisar um login!\nNome/Senha\n')

nome = str(input('Digite um nome: '))
senha = str(input('Digite uma senha: '))

while nome == senha:
    print('\nNome e senha inválidos! Tente novamente...')
    print('Aviso! Nome e senha devem ser diferentes!')
    nome = str(input('Digite um nome: '))
    senha = str(input('Digite uma senha: '))

    if nome != senha:
        print('\nNome e senha válidos!')
        break
