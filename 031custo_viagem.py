# distancia = float(input('Qual a distância da viagem? '))
# if distancia <= 200:
#     valor = distancia * 0.50
#     print(f'O valor da passagem é {valor} R$, Boa viagem!')
# else:
#     valor = distancia * 0.45
#     print(f'O valor da passagem é {valor} R$, Boa viagem!')

distancia = float(input('Qual a distância da sua viagem? '))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da sua passagem é de {valor} R$, Boa viagem!')
