#12.	Juego de números:
#o	Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número. Usa if para verificar si acertó o no.
#o	Ejemplo: Entrada: 5 → Salida: "¡Felicidades, acertaste!" o "Intenta de nuevo.".

#importar libreria para generar números aleatorios
import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

try:
    # Solicitar al usuario que adivine el número
    numero_usuario = int(input("Adivina el número (entre 1 y 10): "))

    # Verificar si acertó
    if numero_usuario == numero_aleatorio:
        print("¡Felicidades, acertaste!")
    else:
        print(f"Intenta de nuevo. El número era: {numero_aleatorio}")
except ValueError:
    print("Verificar datos ingresados.")