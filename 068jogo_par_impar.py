from random import randint
from time import sleep
print('\033[0;32;40m-=' * 41)
print('-='*15, 'JOGO DA PAR OU ÍMPAR', '-='*15)
print('\033[0;32;40m-=' * 41)
v = 0
while True:
    print("""
    [1] PAR
    [2] ÍMPAR
    """)
    op = int(input('ESCOLHA UMA OPÇÃO: '))

    jogador = int(input('jogue um numero: '))
    print('\033[0;32;40m-=' * 41)
    maquina = randint(0, 10)
    num = jogador + maquina

    if jogador > 10 or jogador < 0:
        print('Número Inválido! Jogue um número entre 0 e 10')
        continue

    if op == 1:

        if num % 2 == 0:
            print(f'Você jogou {jogador}')
            print(f'A Computador jogou {maquina}')
            print(f'O número {num} é par, VOCÊ VENCEU!')
            v += 1

        if num % 2 == 1:
            print(f'Você jogou {jogador}')
            print(f'A Computador jogou {maquina}')
            print(f'O número {num} é ímpar, VOCÊ PERDEU!')
            break

    if op == 2:

        if num % 2 == 1:
            print(f'Você jogou {jogador}')
            print(f'A Computador jogou {maquina}')
            print(f'O número {num} é ímpar, VOCÊ VENCEU!')
            v += 1

        if num % 2 == 0:
            print(f'Você jogou {jogador}')
            print(f'A Computador jogou {maquina}')
            print(f'O número {num} é par, VOCÊ PERDEU!')
            break
    print('\033[0;32;40m-=' * 41)
    sleep(2.5)
print(f'GAME OVER você venceu {v} vezes.')