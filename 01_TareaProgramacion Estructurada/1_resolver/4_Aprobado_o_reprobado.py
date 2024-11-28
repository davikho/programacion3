#4.	Aprobado o reprobado:
#o	Solicita la calificación de un estudiante y determina si está aprobado (mayor o igual a 7) o reprobado.
#o	Ejemplo: Entrada: 6.5 → Salida: "Reprobado".

try:
# Solicitar un número al usuario
    numero = float(input("Por favor, ingresa un número: "))

    # Verificar si el número es mayor o igual a 7
    if numero >= 7:
        print("aprobado.")
    else:
        print("reprobado.")
except ValueError:
    print("Verificar datos ingresados")