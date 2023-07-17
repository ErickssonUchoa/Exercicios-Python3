#Calculo hypotenusa 

from math import hypot
a = float(input('Informe o cateto oposto: '))
b = float(input('Informe o cateto adjacente: '))
h = hypot(a, b)
print(f'A hypotenusa é {h:.2f} ')

