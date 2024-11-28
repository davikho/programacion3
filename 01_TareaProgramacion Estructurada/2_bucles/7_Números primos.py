#7.	Números primos:
#o	Encuentra e imprime todos los números primos entre 1 y 50.
#o	Salida esperada: 2, 3, 5, 7, ..., 47.


for num in range(2, 51):  # Comenzamos desde 2, ya que 1 no es primo
    es_primo = True  # Suponemos que el número es primo
    for i in range(2, int(num ** 0.5) + 1):  # Verificamos si el número tiene divisores
        if num % i == 0:  # Si el número es divisible por i, no es primo
            es_primo = False
            break  # No es necesario seguir comprobando, ya sabemos que no es primo
    if es_primo:
        print(num, end=", ")  # Imprime el número primo
