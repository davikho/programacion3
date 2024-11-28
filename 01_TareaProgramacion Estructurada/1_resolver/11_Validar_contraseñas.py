#11.	Validar contraseñas:
#o	Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345).
#o	Ejemplo: Entrada: 12345 → Salida: "Acceso concedido".

try:
    # Solicitar un contraseña
    anio = int(input("Ingresa contraseña: "))
    passw = 12345
    # Verificar si es bisiesto
    if anio == passw:
        print(f"Acceso concedido")
    else:
        print(f"Acceso negado")
except ValueError:
    print("Verificar datos ingresados.")
