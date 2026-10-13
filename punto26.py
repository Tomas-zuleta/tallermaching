numeros = [8, 3, 10, 1, 7, 4, 9, 2, 6, 5]

print("Lista desordenada:", numeros)
for i in range(len(numeros)):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print("Lista ordenada:", numeros)
