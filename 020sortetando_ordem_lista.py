# sorteio sequencia aleatoria trabalho

import random
al1 = str (input('Primeiro aluno: '))
al2 = str (input('Segundo aluno: '))
al3 = str (input('Terceiro aluno: '))
al4 = str (input('Quarto aluno: '))
nomes = [al1, al2, al3, al4]
ordem = random.shuffle(nomes)
print('A ordem de apresentação será')
print(nomes)