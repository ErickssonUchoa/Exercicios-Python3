from time import sleep
print('\033[0;32;40m-='*15)
print('\033[0;31;40mTabuada V3.0')
print('\033[0;32;40m-='*15)

while True:
    num = int(input('Digite um numero: '))
    print('\033[0;32;40m-=' * 15)
    if num < 0:
        print('Tabuada encerrada!')
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*1}')
    print('\033[0;32;40m-=' * 15)
    sleep(1)
