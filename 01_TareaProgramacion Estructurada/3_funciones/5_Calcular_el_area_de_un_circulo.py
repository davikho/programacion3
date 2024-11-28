#5.	Calcular el área de un círculo:
#o	Crea una función que reciba el radio de un círculo y retorne su área.
#o	Fórmula: Área = π * radio^2.
#o	Ejemplo: Entrada: 3 → Salida: 28.27 (aproximado).

def calcular_cuadrado(radio):
    cuadrado = radio ** 2
    return 3.1416 * cuadrado

# Solicitar un número al usuario
radio = float(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = calcular_cuadrado(radio)
print(f"El radio es {radio} y su área es: {resultado}")