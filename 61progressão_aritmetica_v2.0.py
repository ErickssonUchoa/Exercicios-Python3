print('\033[0;32;40m-='*15)
print('\033[0;31;40mDez Termos de uma PA')
print('\033[0;32;40m-='*15)

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão: '))
i = 1
while i <= 11:
    print(t, end=' -> ')
    t += r
    i += 1
print('FIM!')
