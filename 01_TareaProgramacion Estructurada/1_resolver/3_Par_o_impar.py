#3.	Par o impar:
#o	Solicita un número al usuario y determina si es par o impar.
#o	Ejemplo: Entrada: 4 → Salida: "Es par".f

try:
    # Solicitar un número al usuario
    numero = int(input("Por favor, ingresa un número: "))
    
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")
except ValueError:
    print("Verificar datos ingresados")