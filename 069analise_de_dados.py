from time import sleep
print('\033[0;32;40m-='*15)
print('\033[0;31;40mAnálise de Dados')
print('\033[0;32;40m-='*15)
maior = 0
homem = 0
menor = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Qual o sexo da pessoa? [M]/[F]: ').strip().upper()

    if sexo != 'M' and sexo != 'F':
        print('Sexo Inválido! Tente novamente')
        continue

    if idade > 18:
        maior += 1

    if idade < 20 and sexo == 'F':
        menor += 1

    if sexo == 'M':
        homem += 1

    op = input('Deseja continuar? [S]/[N]: ').strip().upper()
    print('\033[0;32;40m-=' * 15)

    if op == 'N':
        print('Programa finalizado!')
        break

    sleep(1)

print(f'foram cadastradas {maior} pessoas maior de 18 anos')
print(f'Foram cadastrados {menor} mulheres menores de 20 anos')
print(f'Foram cadastrados {homem} homens')
