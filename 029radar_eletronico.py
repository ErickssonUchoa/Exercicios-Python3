velocidade = float(input('Qual a velocidade do carro: '))

if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7.0
    print(f'Sua velocidade ultrapassou o limite de 80km/h, você foi multado em {multa:.2f} R$')
else:
    print('Velocidade dentro do limete, tenha um bom dia e dirija com segurança!')
