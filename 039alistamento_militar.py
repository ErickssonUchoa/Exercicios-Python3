from datetime import date
print('\033[0;32;40m-='*15)
print('\033[0;31;40mAlistamento Militar')
print('\033[0;32;40m-='*15)

ano = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = ano - nasc

if idade == 18:
    print('Está na hora de você se alistar ao Serviço Militar.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos(s) para você se alistar')
else:
    saldo = idade - 18
    print(f'Você ultrapassou o prazo de alistamento em {saldo} ano(s)')
