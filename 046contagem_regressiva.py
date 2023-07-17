from time import sleep
print('\033[0;32;40m-='*15)
print('\033[0;31;40mContagem Regressiva')
print('\033[0;32;40m-='*15)
print('Contagem regressiva para a queima de fogos!')

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('\033[0;31;40mFogooooooooooooooooooooooooooo!')
