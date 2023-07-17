print('\033[0;32;40m-='*15)
print('\033[0;31;40mTratando Valores')
print('\033[0;32;40m-='*15)

i = 0
s = 0

while True:

    n = int(input('Digite um numero: '))
    i += 1
    s += n

    if n == 999:
        s -= n
        i -= 1
        break

print(f'Foram digitados {i} numeros e a soma entre eles é {s}')
