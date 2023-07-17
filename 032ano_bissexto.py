from datetime import date
ano = int(input('Digite o ano que quer analisar, ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
