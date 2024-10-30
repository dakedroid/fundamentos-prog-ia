# Variables de diferentes tipos de datos
entero = 10
flotante = 20.5
cadena = "Hola, Mundo!"
booleano = True

# Función que imprime el tipo de dato y su valor
def imprimir_valores():
    print(f"Entero: {entero}")
    print(f"Flotante: {flotante}")
    print(f"Cadena: {cadena}")
    print(f"Booleano: {booleano}")

# Comparaciones simples
def comparar_numeros(a, b):
    if a > b:
        return f"{a} es mayor que {b}"
    elif a < b:
        return f"{a} es menor que {b}"
    else:
        return f"{a} es igual a {b}"

# Función con una condición y un ciclo while
def adivinar_numero():
    numero_secreto = int(input("Ingreseel numero"))
    intento = 0
    while intento != numero_secreto:
        intento = int(input("Adivina el número entre 1 y 10: "))
        if intento > numero_secreto:
            print("El número es menor.")
        elif intento < numero_secreto:
            print("El número es mayor.")
    print("¡Felicidades! Adivinaste el número.")

# Ejecutar las funciones
imprimir_valores()
print(comparar_numeros(entero, 15))
adivinar_numero()
