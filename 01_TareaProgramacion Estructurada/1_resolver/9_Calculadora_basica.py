#9.	Calculadora básica:
#o	Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.
#o	Ejemplo: Entrada: 3, 2, '+' → Salida: "Resultado: 5".

try:
    # Solicitar los números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Solicitar la operación
    operacion = input("Ingresa la operación (+, -, *, /): ")
    
    # Realizar el cálculo según la operación ingresada
    if operacion == '+':
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif operacion == '-':
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif operacion == '*':
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif operacion == '/':
        # Verificar división por cero
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Operación no válida. Por favor ingresa una de estas: +, -, *, /.")
        
except ValueError:
    print("Verificar datos ingresados")
