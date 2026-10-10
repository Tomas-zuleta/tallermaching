#Invertir un número. 
# Solicitar un entero positivo e invertir sus dígitos utilizando operaciones matemáticas.

lista = []
listaInvertida = []

while True:

    opc = input("Ingrese una opción: 1. Ingresar número, 2. invertir número , 3. Salir: ")
    
    if opc == "1":

        num = int(input("Ingrese un número entero positivo: ")) 
        lista.append(num)    

    elif opc == "2":

        print(f"Los numeros ingresados son: {lista}")

        listaInvertida = []
        numeros = 0
        
        for n in lista:
            numeros = (numeros * 10) + n

        while numeros > 0:
            digito = numeros % 10
            listaInvertida.append(digito)
            numeros = numeros // 10

        print(f"Los números invertidos son: {listaInvertida}")

    elif opc == "3":
        print("Saliendo del programa...")
        break

    else:   
        print("Opción no válida. Intente de nuevo.")
        continue