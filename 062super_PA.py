from time import sleep
print('\033[0;32;40m-='*15)
print('\033[0;31;40mSuper Termos de uma PA')
print('\033[0;32;40m-='*15)

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão: '))
i = 1
s = 0
while i <= 10:
    print(t, end=' -> ')
    t += r
    i += 1
    s += 1
print('PAUSA')
while True:
    print('\033[0;32;40m-='*15)
    c = 1
    nt = int(input('Quantos termos você quer mostrar a mais? '))
    if nt != 0:
        while c <= nt:
            print(t, end=' -> ')
            t += r
            c += 1
            s += 1
        print('PAUSA')
        sleep(2)
    else:
        print(f'Programa Finalizado com {s} termos mostrados.')
        break
