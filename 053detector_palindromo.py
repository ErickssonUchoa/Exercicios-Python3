print('\033[0;32;40m-='*15)
print('\033[0;31;40mPalíndromo')
print('\033[0;32;40m-='*15)
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um pálindromo')
