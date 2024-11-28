#3.	Tabla de multiplicar:
#o	Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
#o	Ejemplo: Entrada: 5 → Salida: 5 x 1 = 5, ..., 5 x 10 = 50.



numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")