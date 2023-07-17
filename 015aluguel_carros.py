# Aluguel de carro
d = int(input('Dias alugados? '))
km = float(input('Quilômetros rodados? '))
vp = (d * 60) + (0.15 * km)
print(f'O valor a pagar é R${vp:.2f}')
