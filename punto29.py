#Multiplicación de elementos de una lista. Crear una lista de 10 números. 
# Solicitar un número multiplicador y generar otra lista donde cada elemento sea el resultado de multiplicar 
# el elemento original por dicho valor.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplicador = int(input("Ingrese un número multiplicador: "))

resultado = []

for numero in numeros:
    resultado.append(numero * multiplicador)

print("Lista original:", numeros)
print("Lista multiplicada:", resultado)