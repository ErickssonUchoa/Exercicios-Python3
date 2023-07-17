print('\033[0;32;40m-='*15)
print('\033[0;31;40mConversão de números nas bases')
print('\033[0;32;40m-='*15)
print('\033[0;35;40m')
# print(f'{bin(num)}, {oct(num)}, {hex(num)}')
num = int(input('Digite o número que deseja converter: '))
print(''' Escolha a base em que vc quer a conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
''')
conver = input('Sua opção: ')

if conver == '1':
    print(f'O numero {num} convertido em Binário é {bin(num)}')
elif conver == '2':
    print(f'O numero {num} convertido em Octal é {oct(num)}')
elif conver == '3':
    print(f'O numero {num} convertido em Hexadecial é {hex(num)}')
