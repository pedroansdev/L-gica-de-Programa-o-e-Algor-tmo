import random

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''


print('Programa de análise de texto!\nQuais palavras têm letras iguais a "python"\n')

print(f'Texto a ser analisado: \n{texto}')

texto = texto.replace('.','')
texto = texto.replace(',','')
texto = texto.replace(':','')

texto = texto.lower()
texto = texto.split()

def pythonica(p):
    for letras in p:
        if letras in 'python' and len(p) > 4:
            return p
    return False

confirmacao = str(input('Deseja começar a rodar o programa? [S/N]')).upper()

if (confirmacao == 'S'):
    for p in texto:
            print(pythonica(p))
else:
   exit()

input()

#while (confirmacao != 'S' and not 'N'):
#    confirmacao = str(input('Deseja começar a rodar o programa? [S/N]')).upper()
