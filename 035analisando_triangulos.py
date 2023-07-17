print('-='*15)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*15)
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar triângulo')
