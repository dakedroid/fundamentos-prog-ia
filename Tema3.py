lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

diccionario = {
    1: "UNO",
    2: "DOS",
    3: "TRES",
    4: "CUATRO",
    5: "CINCO"
}

frutas = ["🍎", "🍐", "🍊"]
print(frutas[0]) # Imprimir una posición
frutas.append("🍉")
frutas.insert(0, "🍌")
print(frutas)
frutas.pop()
frutas.remove("🍐")
print(frutas)
print(frutas.index("🍊"))

print(len(frutas))
print(len(lista))

