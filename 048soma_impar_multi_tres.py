print('\033[0;32;40m-='*15)
print('\033[0;31;40mSoma múltiplus de 3')
print('\033[0;32;40m-='*15)

soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        soma += i
print()
print(f'O valor da soma desses números é: {soma}')