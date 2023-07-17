from time import sleep

i = 0
soma = 0

while True:

    num = int(input(f'Digite um numero: '))
    soma += num
    i += 1
    media = soma / i
    if i == 1:
        maior = menor = num

    else:

        if num > maior:
            maior = num

        if num < menor:
            menor = num

    p = input('Quer continuar [S]/[N]: ').strip().upper()
    if p == 'N':
        break

    sleep(0.2)

print(f'A média de todos os números digitados foi {media:.1f}')
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
