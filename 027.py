nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print(f'Seu primeiro nome é:  {nome[0].title()}')
print(f'Seu ultimo nome é:  {nome[-1].title()}')
