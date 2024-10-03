# Crear una lista para almacenar los números ganadores
numeros_ganadores = []

# Preguntar al usuario cuántos números desea ingresar
cantidad = int(input("¿Cuántos números ganadores desea ingresar? "))

# Recoger los números ganadores
for i in range(cantidad):
    numero = int(input(f"Ingrese el número ganador {i + 1}: "))
    numeros_ganadores.append(numero)

# Ordenar la lista de menor a mayor
numeros_ganadores.sort()

# Mostrar la lista de números ganadores
print("\nNúmeros ganadores de la lotería en orden de menor a mayor:")
for numero in numeros_ganadores:
    print(numero)