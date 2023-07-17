# from math import factorial
# n = int(input('Digite um numero: '))
# fat = factorial(n)
# print(fat)

n = int(input('Digite um numero: '))
i = n
f = 1
print(f'Calculando {n}!: ', end='')
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print(f'{f}')
