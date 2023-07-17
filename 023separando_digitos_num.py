# receber numero de 0 a 9999 e mostrar suas unidades

num = int (input('Digite um numero de 0  a 9999:'))
u = num // 1 % 10  # pegando a unidade de um numero
d = num // 10 % 10  # pegando a dezena de um numero
c = num // 100 % 10  # pegando a centena de um numero
m = num // 1000 % 10  # pegando a milhar de um numero
print(f'A sua unidade é: {u}')
print(f'A sua dezena é: {d}')
print(f'A sua centena é: {c}')
print(f'A sua milhar é: {m}')

# numero = str(input("Digite um numero de 1 a 9999: "))
# print("A casa do milhar vale:, ", numero[0])
# print("A casa da centena vale: ", numero[1])
# print("A casa da dezena vale: ", numero[2])
# print("A casa da unidade vale: ", numero[3])

# num = str(input('Digite um número de 0 a 9999: '))
# if len(num) != 4:
#   print('Valor incorreto')
# else:
#    print(f'Unidade: {num[3]}')
#    print(f'Dezena: {num[2]}')
#    print(f'Centena: {num[1]}')
#    print(f'Milhar: {num[0]}')




