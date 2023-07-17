from random import randint
num = randint(0, 5)
print('*'*10, 'JOGO DA ADIVINHAÇÃO', '*'*10)
jogador = int(input('Adivinhe o numero de 0 até 5: '))
msg = f'Você acertou! o numero era {num}' if jogador == num else f'Você errou! o numero era {num}'
print(msg)
