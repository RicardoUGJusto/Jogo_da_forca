palavra = input("Digite uma palvra: ")
print("\x1b[2J")

tentativas = 0

forca = []
for i in range(len(palavra)):
    forca.append("_")

ganhou = False

while tentativas < 6 and "".join(forca) != palavra:
    letra = input("Digite uma letra: ")

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                forca[i] = letra

    else:
        tentativas += 1

    print("Forca: " + "".join(forca))

if "".join(forca) == palavra:
    print("Você ganhou!")
else:
    print("Você perdeu!")

