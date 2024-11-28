#1.	Mayor o menor:
#o	Escribe un programa que solicite un número y determine si es mayor o menor que 10.
#o	Ejemplo: Entrada: 5 → Salida: "Es menor que 10".

try:
# Solicitar un número al usuario
    numero = int(input("Por favor, ingresa un número: "))

    # Verificar si es mayor, menor o igual a 10
    if numero > 10:
        print("Es mayor que 10.")
    elif numero < 10:
        print("Es menor que 10.")
    else:
        print("Es igual a 10.")
except ValueError:
    print("Verificar datos ingresados")
