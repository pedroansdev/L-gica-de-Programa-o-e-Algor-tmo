import random

print('Vetores de números aleatórios!')

vet1 = random.sample(range(1, 101),10)
vet2 = random.sample(range(1, 101),10)

vet3 =  []

for n in range(10):
    vet3.append(vet1[n])
    vet3.append(vet2[n])

print(f'Vetor 1: {vet1}\nVetor 2: {vet2}\nVetor 3: {vet3}')
