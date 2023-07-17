
nome = str(input('Digite seu nome:'))
print('*'*20, 'Mostrando tudo maiúsculo', '*'*20)
print(nome.upper())

print('*'*20, 'Mostrando tudo minúsculo', '*'*20)
print(nome.lower())

print('*'*20, 'Mostrando quantidade de letras sem contar espaços', '*'*20)
print(len(nome.replace(' ', '')))

print('*'*20, 'Mostrando quantidade de letras do primeiro nome', '*'*20)
div = nome.split()
print(len(div[0]))

# nome = str(input("\nDigite seu nome e sobrenome: ")).strip()
# dividido = nome.split()
# print(f'\nO seu nome com todas as letras maiúsculas ficará: {nome.upper()}')
# print(f'\nEm minúsculas: {nome.lower()}')
# print(f'\nA quantidade de letras é: {len(nome.replace(' ', ''))}')
# print(f'\nE a quantidade de letras do seu primeiro nome é de: {len(dividido[o])}')
