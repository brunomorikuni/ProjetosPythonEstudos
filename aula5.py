#jogo de forca

secreta = 'bruno'
digitados = []
while True:
    letra = input("Digite uma letra : ")

    if len(letra) > 1:
        print("isso não pode ")
        continue

    digitados.append(letra)

    if letra in secreta:
        print(f"essa {letra} está na palavra secreta")
    else:
        print(f"essa {letra} não está na palavra secreta")
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += "*"
    print(secreto_temporario)