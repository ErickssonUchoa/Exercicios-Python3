print('\033[0;32;40m-='*15)
print('\033[0;31;40m10 Termos de uma PA')
print('\033[0;32;40m-='*15)
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão: '))

for i in range(10, 0, -1):
    print(t, end=' -> ')
    t += r
print('ACABOU!')
