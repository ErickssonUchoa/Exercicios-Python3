from time import sleep
print('\033[0;32;40m-='*15)
print('\033[0;31;40mPalíndromo')
print('\033[0;32;40m-='*15)
total = 0
mais = 0
menor = ''
m = 0
i = 1
while True:

    nome = input('Qual o nome do produto: ')
    pre = float(input('Qual o preço do produto: '))
    total += pre

    if i == 1:
        m = pre
        menor = nome

    if pre < m:
        m = pre
        menor = nome

    if pre > 1000:
        mais += 1

    op = input('Deseja continuar comprando? [S]/[N]: ').upper()
    print('\033[0;32;40m-=' * 15)
    if op == 'N':
        print('Programa finalizado!')
        break
    i += 1
    sleep(0.5)

print(f'Foram comprados {mais} produtos com valor de 1000.00 R$')
print(f'O produto com o menor valor comprado foi {menor}')
print(f'O total das compras foi {total:.2f} R$')
