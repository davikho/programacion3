#13.	Calcular el signo zodiacal:
#o	Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.
#o	Ejemplo: Entrada: 22, marzo → Salida: "Tu signo es Aries".

try:
    # Solicitar el día y el mes de nacimiento
    dia = int(input("Ingresa el día de tu nacimiento: "))
    mes = input("Ingresa el mes de tu nacimiento (en texto o número): ").strip().lower()

    # Convertir el mes a número si es necesario
    meses = {
        "enero":        1, 
        "febrero":      2, 
        "marzo":        3, 
        "abril":        4, 
        "mayo":         5, 
        "junio":        6,
        "julio":        7, 
        "agosto":       8, 
        "septiembre":   9, 
        "octubre":      10, 
        "noviembre":    11, 
        "diciembre":    12
    }
    mes_num = meses.get(mes, int(mes) if mes.isdigit() and 1 <= int(mes) <= 12 else None)

    if not mes_num:
        raise ValueError("Mes no válido.")

    # Determinar el signo zodiacal
    if (mes_num == 3 and dia >= 21) or (mes_num == 4 and dia <= 19):
        signo = "Aries"
    elif (mes_num == 4 and dia >= 20) or (mes_num == 5 and dia <= 20):
        signo = "Tauro"
    elif (mes_num == 5 and dia >= 21) or (mes_num == 6 and dia <= 20):
        signo = "Géminis"
    elif (mes_num == 6 and dia >= 21) or (mes_num == 7 and dia <= 22):
        signo = "Cáncer"
    elif (mes_num == 7 and dia >= 23) or (mes_num == 8 and dia <= 22):
        signo = "Leo"
    elif (mes_num == 8 and dia >= 23) or (mes_num == 9 and dia <= 22):
        signo = "Virgo"
    elif (mes_num == 9 and dia >= 23) or (mes_num == 10 and dia <= 22):
        signo = "Libra"
    elif (mes_num == 10 and dia >= 23) or (mes_num == 11 and dia <= 21):
        signo = "Escorpio"
    elif (mes_num == 11 and dia >= 22) or (mes_num == 12 and dia <= 21):
        signo = "Sagitario"
    elif (mes_num == 12 and dia >= 22) or (mes_num == 1 and dia <= 19):
        signo = "Capricornio"
    elif (mes_num == 1 and dia >= 20) or (mes_num == 2 and dia <= 18):
        signo = "Acuario"
    elif (mes_num == 2 and dia >= 19) or (mes_num == 3 and dia <= 20):
        signo = "Piscis"
    else:
        raise ValueError("Día fuera de rango para el mes.")

    print(f"Tu signo es {signo}.")
except ValueError as e:
    print(f"Entrada no válida: {e}")
