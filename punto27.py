#Sumar elementos de dos listas. Crear dos listas de cinco números y construir una tercera que contenga
#  la suma de los elementos ubicados en las mismas posiciones.

Lista1 = [1,2,3,4,5]
Lista2 = [6,7,8,9,10]
suma = [a + b for a, b in zip(Lista1, Lista2)]

print(f"lista1:{Lista1}\nlista2:{Lista2}\nsuma de las listas:{suma}\n" )

