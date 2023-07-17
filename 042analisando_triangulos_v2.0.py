print('\033[0;32;40m-='*15)
print('\033[0;31;40mAnalisando Triângulo v2.0')
print('\033[0;32;40m-='*15)

lado1 = float(input('Digite o primeiro lado do Triângulo: '))
lado2 = float(input('Digite o segundo lado do Triângulo: '))
lado3 = float(input('Digite o terceiro lado do Triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos podem formar um triângulo')
    if lado1 != lado2 != lado3:
        print('Triângulo Escaleno!')
    elif lado1 == lado2 == lado3:
        print('Triângulo Equilátero!')
    else:
        print('Triângulo Isósceles')
else:
    print('Os segmentots não podem formar um triângulo')
