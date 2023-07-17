frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'Em que posição ela aparece a primera vez? {frase.find("A")+1}')
print(f'Em que posição ela aparece pela ultima vez? {frase.rfind("A")+1}')
