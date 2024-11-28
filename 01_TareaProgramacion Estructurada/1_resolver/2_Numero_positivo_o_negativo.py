#2.	Número positivo o negativo:
#o	Solicita al usuario un número y determina si es positivo, negativo o cero.
#o	Ejemplo: Entrada: -3 → Salida: "Es un número negativo".

try:
# Solicitar un número al usuario
    numero = float(input("Por favor, ingresa un número: "))
    
    # Verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("Es un número positivo.")
    elif numero < 0:
        print("Es un número negativo.")
    else:
        print("Es cero.")
except ValueError:
    print("Verificar datos ingresados")