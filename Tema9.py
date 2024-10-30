# Variables Globlaes
opcion1 = "Tacos de Asada"
opcion2 = "Tacos de Pastor"
taqueroNombre = "Kevin"


def prepararTacoAsada():
    salsaRoja = "roja" # Variable local
    print("Preparando taco de ", opcion1, "Con salsa", salsaRoja)


def prepararTacoPastor():
    salsaVerde = "verde" # Variable local
    print("Preparando taco de ", opcion2, "Con salsa", salsaVerde)

def calentarEstufa():
    print("Calentando estufa")


print(taqueroNombre)
calentarEstufa() # singleton
prepararTacoAsada()
prepararTacoPastor()