print('\033[0;32;40m-='*15)
print('\033[0;31;40m10 Numeros primos')
print('\033[0;32;40m-='*15)
num = int(input('Digite um número: '))
t = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[0;32;40m{i}', end=' ')
        t += 1
    else:
        print(f'\033[0;31;40m{i}', end=' ')
print()
if t == 2:
    print('O número é primo')
else:
    print(f'O número {10} não é Primo')
