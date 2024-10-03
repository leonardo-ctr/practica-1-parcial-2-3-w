# Almacenar las materias en una lista
materias = [
    "Pensamiento matemático",
    "humanidades",
    "Inglés",
    "ecosistemas",
    "metodologias",
    "Frameworks",
    "sociemocional",
    "lengua y comunicacion",
]

# Crear un diccionario para almacenar las calificaciones
calificaciones = {}

# Pedir al usuario que ingrese la calificación para cada materia
for materia in materias:
    calificacion = input(f"Ingrese la calificación para {materia}: ")
    calificaciones[materia] = calificacion

# Desplegar las calificaciones
print("\nCalificaciones obtenidas:")
for materia, calificacion in calificaciones.items():
    print(f"En {materia} has obtenido {calificacion}.")