print('\033[0;32;40m-='*15)
print('\033[0;31;40mTabuada V2.0')
print('\033[0;32;40m-='*15)

num = int(input('Digite um numero: '))

for i in range(1, 11):
    print(f'{num} x {i}: ', num * i)
