print('\033[0;32;40m-='*15)
print('\033[0;31;40mBRASILEIRÃO')
print('\033[0;32;40m-='*15)

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza',
         'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print(f'O primeiros 5 colocados são: {times[0:5]}')
print('\033[0;32;40m-='*15)
print(f'Os times que estão do Z4 são: {times[16:]} ')
print('\033[0;32;40m-='*15)
print(f'Em ordem Alfabética {sorted(times)}')
print('\033[0;32;40m-='*15)
print(f'A posição do Flamengo é {times.index("Flamengo") + 1}° posição')
