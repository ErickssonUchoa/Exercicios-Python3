from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número número: '))

while True:
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS VALORES
    [5] SAIR
    """)
    op = input('ESCOLHA UMA OPÇÃO: ')
    if op == '1':
        soma = n1 + n2
        print(f'Soma {n1} + {n2} = {soma}')
    elif op == '2':
        mul = n1 * n2
        print(f'Multiplicação: {n1} * {n2} = {mul}')
    elif op == '3':
        if n1 > n2:
            print(f'Maior: {n1}')
        if n2 > n1:
            print(f'Maior: {n2}')
        else:
            print('Numeros Iguais!')
    elif op == '4':
        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))
    elif op == '5':
        print('Programa Finalizado!')
        break
    else:
        print('Opção Inválida, tente novamente')
    sleep(2)
