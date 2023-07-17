a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a < b and a < c:
    menor = a
elif b < c and b < a:
    menor = b
else:
    menor = c

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
