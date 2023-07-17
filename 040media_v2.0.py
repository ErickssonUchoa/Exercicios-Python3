print('\033[0;32;40m-='*15)
print('\033[0;31;40mMédia do Aluno')
print('\033[0;32;40m-='*15)

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'A média é {media}. Aluno Reprovado!')
elif 5.0 <= media <= 6.9:
    print(f'A média é {media}. Aluno em Recuperação!')
else:
    print(f'A média é {media}. Aluno Aprovado!')
