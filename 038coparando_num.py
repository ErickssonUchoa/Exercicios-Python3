print('\033[0;32;40m-='*15)
print('\033[0;31;40mComparando Números')
print('\033[0;32;40m-='*15)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Os dois valos são iguais!')
