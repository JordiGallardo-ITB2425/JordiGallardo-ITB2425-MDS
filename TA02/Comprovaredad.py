# Jordi Gallardo - 1ASIXcD Prueba

# Solicitar la edad del usuario
edat = int(input("¿Cuántos años tienes? "))

# Comprobar si la persona es mayor o menor de edad
while edat < 0:
    print("Es imposible que aún no hayas nacido.")
    print("Pon una edad válida.\n")
    edat = int(input("¿Cuántos años tienes? "))

while edat > 130:
    print("No puedes ser tan viejo.")
    print("Pon una edad válida.\n")
    edat = int(input("¿Cuántos años tienes? "))

# Categorización de la edad
if edat <= 12:
    print("Eres un niño.\nDisfruta de tu infancia.")
elif edat <= 17:
    print("Eres un adolescente.\nSal de fiesta y diviertete.")
elif edat <= 65:
    print("Eres un adulto.\n Trabaja para vivir y no vivas para trabajar.")
else:
    print("Eres una persona mayor.\nAprobecha la poca vida que te queda.")

# Mensaje personalizado según si es mayor o menor de edad
if edat >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.\nQue tengas un buen día y aprovecha tu vida.")
