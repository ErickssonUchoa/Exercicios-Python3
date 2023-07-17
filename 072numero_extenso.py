print('\033[0;32;40m-='*15)
print('\033[0;31;40mNúmeros por extenso')
print('\033[0;32;40m-='*15)

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Número Inválido! Tente Novamente.')
        continue
    print(f'Você digitou {num[n]}')
