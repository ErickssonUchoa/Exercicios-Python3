from random import randint
print('\033[0;32;40m-='*20)
print('\033[0;31;40mPedra Papel Tessoura')
print('\033[0;32;40m-='*20)

itens = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0, 0)
jogador = int(input("""
[0] Pedra
[1] Papel
[2] Tesoura
Escolha sua opção:
"""))
print('\033[0;34;40m-='*20)
print(f'Você jogou {itens[jogador]}')
print(f'A maquina jogou {itens[maquina]}')
print('\033[0;34;40m-='*20)

if jogador == 0:
    if maquina == 0:
        print('EMPATE')
    elif maquina == 1:
        print('Você PERDEU!')
    else:
        print('Você GANHOU')

if jogador == 1:
    if maquina == 0:
        print('você GANHOU!')
    elif maquina == 1:
        print('EMPATE!')
    else:
        print('Você PERDEU')

if jogador == 2:
    if maquina == 0:
        print('Você PERDEU')
    elif maquina == 1:
        print('Você GANHOU!')
    else:
        print('EMPATE')
