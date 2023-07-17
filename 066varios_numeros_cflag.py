i = 0
s = 0

while True:
    num = int(input(f'Digite um numero: '))
    if num == 999:
        break
    s += num
    i += 1
print(f'Foram digitados {i} números e a soma entre eles é {s}')
