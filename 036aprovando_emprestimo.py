print('\033[0;32;40m-='*15)
print('\033[0;31;40mAprovando Empréstimo')
print('\033[0;32;40m-='*15)
print('\033[0;35;40m')

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
mensal = casa / (anos * 12)
print(f'\033[0;37;40mPara pagar a casa no valor de {casa:.2f} R$ em {anos} anos, as pretações seram de {mensal:.2f} R$')
if mensal > salario * 0.30:
    print('\033[0;31;40mEmpréstimo negado!')
else:
    print('\033[0;32;40mEmpréstimo concedido!')
