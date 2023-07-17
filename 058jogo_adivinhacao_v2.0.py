from random import randint
print('\033[0;32;40m-=' * 41)
print('-='*15, 'JOGO DA ADIVINHAÇÃO', '-='*15)
print('\033[0;32;40m-=' * 41)
p = 0
while True:
    num = randint(0, 10)
    t = int(input('Tente adivinhar um numero entr 0 e 10: '))
    if t != num:
        print(f'A maquina escolheu {num}')
        print('Você errou! tente novamente')
        print('\033[0;32;40m-=' * 15)
        p += 1
    if t == num:
        print(f'A maquina escolheu {num}')
        print('Você Acertou!')
        p += 1
        break
print(f'Foram necessárias {p} tentativas Para vencer')
