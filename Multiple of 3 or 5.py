maximo = 1000

divisor_1 = 3
divisor_2 = 5

contador = 0
suma = 0

while contador < maximo:

    if (contador % divisor_1) == 0:
        suma += contador

    elif (contador % divisor_2) == 0:
        suma += contador

    contador += 1

print(suma)