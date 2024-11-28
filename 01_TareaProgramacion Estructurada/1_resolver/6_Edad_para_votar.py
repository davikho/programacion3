#6.	Edad para votar:
#o	Solicita la edad del usuario y determina si es elegible para votar (mayor o igual a 18 años).
#o	Ejemplo: Entrada: 17 → Salida: "No puedes votar".

try:
    #pedir valor al usuario
    edad = float(input("ingresa tú edad: "))
    if edad >= 18:
        print("Puedes votar")
    else:
        print("No puedes votar")

except ValueError:
    print("Verificar datos ingresados")