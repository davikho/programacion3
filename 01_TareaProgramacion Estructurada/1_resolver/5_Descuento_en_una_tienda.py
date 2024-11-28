#5.	Descuento en una tienda:
#o	Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. Escribe un programa que calcule el monto final.
#o	Ejemplo: Entrada: $120 → Salida: "Monto final: $96".

try:
    #pedir valor al usuario
    valor = float(input("ingresa el valor de la compra: "))
    if valor >= 100:
        descuento =  valor * 0.2
        monto_final = valor - descuento
        print("El total de su compra es: ",monto_final)
    else:
        print("El total de su compra es: ",valor)

except ValueError:
    print("Verificar datos ingresados")