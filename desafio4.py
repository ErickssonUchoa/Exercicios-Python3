nome = input('Informe seu primeiro nome: ')

if len(nome) < 4:
    print('Seu nome é muito curto!')
elif len(nome) >= 4 and len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
