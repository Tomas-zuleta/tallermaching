import os
import sys

def mostrar_menu():
    print("\n" + "=" * 40)
    print("       MENU PRINCIPAL")
    print("=" * 40)
    print("1. Punto 17")
    print("2. Punto 27")
    print("3. Punto 29")
    print("4. Salir")
    print("=" * 40)

def ejecutar_opcion(opcion):
    archivos = {
        1: "punto17.py",
        2: "punto27.py",
        3: "punto29.py"
    }
    archivo = archivos.get(opcion)
    if archivo and os.path.exists(archivo):
        print(f"\n>>> Ejecutando espere un momentico mi papa  {archivo}...\n")
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            exec(codigo, {'__name__': '__main__'})
        except Exception as e:
            print(f"Error al ejecutar {archivo}: {e}")
    else:
        print(f"El archivo {archivo} no existe por lo tanto no lo puede ejecutar .")

def main():
    while True:
        mostrar_menu()
        entrada = input("Seleccione una opcion (1-4): ").strip()
        
        # Validar que sea un número
        if not entrada.isdigit():
            print("\n[!] Error: Debe ingresar un numero entre 1 y 4.o si no no ejecuta ome torta")
            continue
        
        opcion = int(entrada)
        
        # Validar que esté en el rango permitido
        if opcion < 1 or opcion > 4:
            print(f"\n[!] Error: La opcion {opcion} no es valida tuki tuki .")
            print("[!] Debe ingresar un numero entre 1 y 4 ya le dije que si pone otra cosa no le ejecuta .")
            continue
        
        # Opción salir
        if opcion == 4:
            print("\nla buena mi fafa por usar este programa hecho en python a conciencia ")
            break
        
        # Ejecutar la opción seleccionada
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
