print('\033[0;32;40m-='*15)
print('\033[0;31;40mPeso maior e Peso menor')
print('\033[0;32;40m-='*15)
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Informe o preso da pessoa {p}: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso digitado foi {maior}')
print(f'O menor peso digitado foi {menor}')
