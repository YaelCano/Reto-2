# Reto 2: Multiplicación Rusa

# El método de multiplicación rusa consiste en multiplicar sucesivamente por 2 el multiplicando y dividir por 2 el multiplicador hasta que el multiplicador tome el valor 1.
# Luego, se suman todos los multiplicandos correspondientes a los multiplicadores impares.
# Dicha suma es el producto de los dos números. La siguiente tabla muestra el cálculo realizado para multiplicar 37 por 12, cuyo resultado final es 12 + 48 + 384 = 444.


# Desarrolle un programa que reciba como entrada el multiplicador y el multiplicando, y entregue como resultado el producto de ambos, calculado mediante el método de multiplicación rusa.
def rusa_mult(m,n):
    suma = 0
    while n > 0:
        if n % 2 == 1:
            suma += m
        m *= 2
        n //= 2
    return suma
multiplicador = int(input("Ingrese el multiplicador: "))
multiplicando = int(input("Ingrese el multiplicando: "))

resultado = rusa_mult(multiplicador, multiplicando)
print("El producto de ambos numeros es:", resultado)
