import time

while True:
  for hora in range(24):
    for minuto in range(60):
      print("{:02d}:{:02d}".format(hora, minuto))
      time.sleep(0.01)
import time

horas = 0
minutos = 0
velocidad = 0.01

while True:
    # Formateamos las horas y minutos para que siempre tengan dos dígitos
    print(f"{horas:02}:{minutos:02}")

    # Pausa para simular un segundo o acelerar la actualización
    time.sleep(velocidad)  # Cambia a 1 para que sea 1 segundo, o menos para que sea más rápido

    # Incrementar los minutos
    minutos += 1

    # Si los minutos llegan a 60, reiniciamos a 0 y sumamos 1 a la hora
    if minutos == 60:
        minutos = 0
        horas += 1

    # Si las horas llegan a 24, reiniciamos a 0
    if horas == 24:
        horas = 0







# Realizar un codigo en python que simule un reloj
# formato 24 horas
# que empiece en 00:00 hasta 23:59 y se reinicie
# pero que implemente time.sleep(x) para que se actualice
# cada segundo o mas  acelerado.

