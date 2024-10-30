print ("Ingrese calificación 1: ")
cal1 = int(input())
print ("ingrese calificación 2: ")
cal2 = int(input())
print ("ingrese calificación 3: ")
cal3 = int(input())

suma=(cal1 + cal2 + cal3)
promedio=suma/3

if (promedio > 100):
    print("Esta no es una calificación válida")
elif (promedio < 70):
    print("ya jodiste")
elif (promedio >= 70):
    print("aprobo")

print("el promedio es: ", promedio)





