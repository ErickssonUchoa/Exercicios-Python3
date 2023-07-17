#   LARGURA E ALTURA, CALCULAR ÁREA E QUANTIDADE DE TINTA GASTA

larg = float(input('Informe a largura:'))
altura = float(input('informe a altura:'))
area = larg * altura
tinta = area / 2
print(f'A área da parede é {area:.1f}m² e serão necessários', end=' ') 
print(f'{tinta:.1f} litros de tinta para pintar toda a área ')
