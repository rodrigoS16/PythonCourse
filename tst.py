inteiros = [1, 3, 4, 5, 7, 8, 9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

new_pares = [numero for numero in inteiros if numero % 2 == 0]
print("Fim")