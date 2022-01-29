from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero
soma_total = 0
reverso = 10

for index in range(19):
    if index > 8:
        index -= 9

    soma_total += int(novo_cpf[index] * reverso)


    reverso -= 1
    if reverso < 2:
        reverso = 11

        d = 11 - (soma_total % 11)

        if d > 9:
            d = 0
        soma_total = 0
        novo_cpf += str(d)

print(novo_cpf)
