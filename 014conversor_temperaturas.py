#      Conversão celsius em Fahrenheit
#Para converter graus Celsius em graus Fahrenheit, multiplique por 1,8 e adicione 32.
#Para converter graus Fahrenheit em graus Celsius, subtraia 32 e divida por 1,8.

t = float (input('Informe a temperatudo em °C: '))
# t = ((9 * t)/5) + 32 ou 9 * t / 5 + 32 -> outro modo de converter °C em °F
t = t * 1.8 + 32
print(f'A temperatura em Fahrenheit é {t}°F ')




