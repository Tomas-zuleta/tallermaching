import os

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Punto 17")
    print("2. Punto 27")
    print("3. Punto 29")
    print("4. Salir")

def ejecutar_opcion(opcion):
    archivos = {
        1: "punto17.py",
        2: "punto27.py",
        3: "punto29.py"
    }
    archivo = archivos.get(opcion)
    if archivo and os.path.exists(archivo):
        print(f"\nEjecutando {archivo}...\n")
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            exec(codigo, {'__name__': '__main__'})
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"El archivo {archivo} no existe.")

def main():
    while True:
        mostrar_menu()
        entrada = input("Opcion: ").strip()

        if not entrada.isdigit():
            print("Error: Ingrese un numero entre 1 y 4.")
            continue

        opcion = int(entrada)

        if opcion < 1 or opcion > 4:
            print("Error: Opcion no valida (1-4).")
            continue

        if opcion == 4:
            print("Adios.")
            break

        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
