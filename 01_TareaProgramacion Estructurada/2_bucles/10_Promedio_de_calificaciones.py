#10.	Promedio de calificaciones:
#o	Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.
#o	Ejemplo: Entradas: 5, 7, 8, -1 → Salida: Promedio: 6.67.

# Inicializar variables
total_calificaciones = 0
contador = 0

# Solicitar calificaciones al usuario
while True:
    calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))
    
    if calificacion == -1:
        break 
    
    total_calificaciones += calificacion 
    contador += 1  

# Verificar que se haya ingresado al menos una calificación
if contador > 0:
    promedio = total_calificaciones / contador 
    print(f"Promedio: {promedio:.2f}")  
else:
    print("No se ingresaron calificaciones válidas.")
