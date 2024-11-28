#15.	Control de acceso:
#o	Solicita un nombre de usuario y contraseña, y valida si ambos son correctos. Permite tres intentos antes de bloquear el acceso.
#o	Ejemplo: Entrada: Usuario: admin, Contraseña: 1234 → Salida: "Bienvenido, admin.".

# Definir las credenciales correctas
usuario_correcto = "admin"
contraseña_correcta = "1234"

# Número máximo de intentos
intentos = 3

while intentos > 0:
    # Solicitar nombre de usuario y contraseña
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    # Verificar si las credenciales son correctas
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break  # Salir del bucle si las credenciales son correctas
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")
        else:
            print("Acceso bloqueado. Has agotado todos los intentos.")
