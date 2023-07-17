print('\033[0;32;40m-='*15)
print('\033[0;31;40m10Média idade, Homem mais velho, Mulheres com menos de 20')
print('\033[0;32;40m-='*15)
soma = 0
velho = 0
total = 0
nome1 = ''
for i in range(1, 5):
    nome = input(f'Qual o nome da {i}° pessoa: ')
    idade = int(input(f'Qual a idade da {i}° pessoa: '))
    sexo = input(f'Qual o sexo da {i}° pessoa: ').strip().lower()
    print('\033[0;32;40m-=' * 15)
    soma += idade
    if i == 1 and sexo == 'masculino':
        velho = idade
        nome1 = nome
    else:
        if idade > velho:
            velho = idade
            nome1 = nome
    if sexo == 'feminino' and idade < 20:
        total += 1

media = soma / 4
print(f'A média de idade é {media} anos.')
print(f'O homem mais velho do grupo é {nome1}, ele tem {velho} anos.')
print(f'A quantidade de mulheres com menos de 20 anos é {total}.')
