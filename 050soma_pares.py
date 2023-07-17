print('\033[0;32;40m-='*15)
print('\033[0;31;40mSoma dos Pares')
print('\033[0;32;40m-='*15)

soma = 0
c = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} número inteiro: '))
    if num % 2 == 0:
        soma += num
        c += 1
print(f'Você digitou {c} Números Pares.\nA soma dos numero pares digitados é {soma}')
