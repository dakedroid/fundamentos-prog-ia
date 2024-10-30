print("Bienvenido")
x = int(input("Ingrese su calificación"))
if 0 <= x <= 69:
    print("Reprobó")
elif 70 <= x <= 100:
    print("Aprobó")
    if x == 70:
        print("Alcanzó el mínimo aprobatorio")
    elif x == 100:
        print("Aprobó con excelencia")
else:
    print("Error")
"""

print("Hola")
x = int(input("Ingrese Altura en CM: "))
if x > 0 and x < 160:
    print("Eres Chaparro")
elif x > 160 and x < 170:
    print("Eres estatura Promedio")
elif x >= 170:
    print("Eres Alto")
else:
    print("Estatura No Considerada.")
print("Adios")
"""
