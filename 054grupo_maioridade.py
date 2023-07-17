from datetime import date
print('\033[0;32;40m-='*15)
print('\033[0;31;40m10 Grupo de Maioridade')
print('\033[0;32;40m-='*15)
c = 0
m = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'Digite o {i}° ano de nascimento: '))
    idade = atual - ano
    if idade < 18:
        c += 1
    else:
        m += 1
print(f'O numero de pessoas menor de idade é {c}')
print(f'O numero de pessoas maior de idade é {m}')
