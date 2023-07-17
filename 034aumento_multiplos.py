import string


salario = float(input('Qual o seu salário: '))

if salario > 1250.0:
    aumento = salario * 0.1
    novo = aumento + salario
    print(f'Você recebeu um aumento de {aumento:.2f} R$, e seu novo salário é {novo:.2f} R$')
else:
    aumento = salario * 0.15
    novo = aumento + salario
    print(f'Você recebeu um aumento de {aumento:.2f} R$, e seu novo salário é {novo:.2f} R$')
