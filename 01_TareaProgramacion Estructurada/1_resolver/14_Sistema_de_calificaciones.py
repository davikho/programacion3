#14.	Sistema de calificaciones:
#o	Solicita una calificación numérica y devuelve la letra correspondiente:
#	90-100: A.
#	80-89: B.
#	70-79: C.
#	60-69: D.
#	Menor a 60: F.
#o	Ejemplo: Entrada: 85 → Salida: "Tu calificación es B".

try:
    # Solicitar la calificación numérica
    calificacion = float(input("Ingresa tu calificación (de 0 a 100): "))

    # Verificar el rango de la calificación y asignar la letra correspondiente
    if 90 <= calificacion <= 100:
        letra = "A"
    elif 80 <= calificacion < 90:
        letra = "B"
    elif 70 <= calificacion < 80:
        letra = "C"
    elif 60 <= calificacion < 70:
        letra = "D"
    elif 0 <= calificacion < 60:
        letra = "F"
    else:
        raise ValueError("La calificación debe estar entre 0 y 100.")

    print(f"Tu calificación es {letra}.")
except ValueError as e:
    print(f"Entrada no válida: {e}")
