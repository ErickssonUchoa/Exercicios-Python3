print('\033[0;32;40m-='*15)
print('\033[0;31;40mFibonacci')
print('\033[0;32;40m-='*15)

n = int(input('Digite Quantos termos você deseja: '))
t1 = 0
t2 = 1
i = 3
print(f'{t1} -> {t2}', end=' -> ')
while i <= n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    i += 1
print('ACABOU')
