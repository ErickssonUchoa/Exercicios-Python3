from datetime import date
print('\033[0;32;40m-='*15)
print('\033[0;31;40mConfederação Nacional de Natação')
print('\033[0;32;40m-='*15)

ano = date.today().year
nasc = int(input('Qual o ano de nascimento do atleta? '))
idade = ano - nasc

if nasc <= 9:
    print('Atleta Mirim.')
elif nasc <= 14:
    print('Atleta Infantil.')
elif nasc <= 19:
    print('Atleta Júnior.')
elif nasc <= 25:
    print('Atleta Sênior.')
else:
    print('Atleta Master.')
