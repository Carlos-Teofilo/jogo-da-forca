palavra = input('Digite a palavra: ').lower().strip()
digitadas = []
certas = []
errou = 0

for i in range(50):
    print()

while True:
    print(f"Você tem {6 - errou} chance's")
    secreta = ''
    for i in palavra:
        if i in certas:
            secreta += i
        else:
            secreta = ''
            break
    if secreta == palavra:
        print('Você ganhou!')
        break
    if errou == 6:
        print('Você foi enforcado!')
        break
    tentativa = input('Digite uma letra: ').lower().strip()
    if len(tentativa) > 1:
        print('Você só pode digitar uma letra por vez')
        del tentativa
        continue
    if tentativa in digitadas:
        print(f'Você já digitou a letra "{tentativa}"')
        del tentativa
        continue
    if tentativa not in palavra:
        print(f'A letra "{tentativa}" não existe na palavra')
        errou += 1
    digitadas.append(tentativa)
    for letra in palavra:
        if tentativa == letra:
            certas.append(tentativa)
    for i in palavra:
        if i in certas:
            secreta += i
        else:
            secreta += '.'
    print(secreta)
