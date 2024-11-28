#8.	Clasificación de edades:
#o	Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).
#o	Ejemplo: Entrada: 15 → Salida: "Eres adolescente".

try:
    #pedir valor al usuario
    edad = int(input("Ingresa tu edad: "))
    
    if edad <= 12:
        print("Tienes", edad, "años, eres un niño.")
    elif 13 <= edad and edad <= 17:  # Usar 'and' o esta forma más concisa
        print("Tienes", edad, "años, eres un adolescente.")
    else:
        print("Tienes", edad, "años, eres un adulto.")
        
except ValueError:
    print("Verificar datos ingresados")