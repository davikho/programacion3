#10.	Determinar un año bisiesto:
#o	Solicita un año y determina si es bisiesto (divisible entre 4 pero no entre 100, excepto si es divisible entre 400).
#o	Ejemplo: Entrada: 2024 → Salida: "Es bisiesto".

try:
    # Solicitar un año
    anio = int(input("Ingresa un año: "))

    # Verificar si es bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"{anio} es bisiesto.")
    else:
        print(f"{anio} no es bisiesto.")
except ValueError:
    print("Verificar datos ingresados")