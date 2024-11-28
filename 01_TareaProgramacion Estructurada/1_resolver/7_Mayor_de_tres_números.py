#7.	Mayor de tres números:
#o	Solicita tres números y determina cuál es el mayor.
#o	Ejemplo: Entrada: 4, 9, 2 → Salida: "El número mayor es 9".

try:
    #pedir valor al usuario
    uno = int(input("ingresa un número: "))
    dos = int(input("ingresa otro número: "))
    tres = int(input("ingresa el último número: "))
    if uno > dos and uno > tres :
        print("el número mayor es: ", uno)
    elif dos > uno and dos > tres :
        print("el número mayor es: ", dos)
    else:
        print("el número mayor es: ", tres)
        
except ValueError:
    print("Verificar datos ingresados")