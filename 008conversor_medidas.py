#   Converter metros em Cm e Mm

m = float(input('Informe a metragem:'))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000

print(f'conversão de {m} metros:')
print(f'Em decímetros são {dm}Dm\nEm centímetros são{cm}Cm\n', end='')
print(f'Em milímetros são {mm}Mm')
print(f'Em decâmetro é {dam}Dam\nEm hectômetro é {hm}Hm\n', end='')
print(f'Em quilômetro é {km}Km')
