# Metodo de Jacobi

# pedir tamaño del sistema
n = int(input("Numero de variables: "))

# matriz de coeficientes
A = []
print("Ingrese la matriz de coeficientes:")
for i in range(n):
    fila = list(map(float, input().split()))
    A.append(fila)

# vector de resultados
b = list(map(float, input("Ingrese el vector de resultados: ").split()))

# valores iniciales
x = list(map(float, input("Ingrese los valores iniciales: ").split()))

# tolerancia
Di = float(input("Ingrese la tolerancia: "))

error = 1
iteracion = 0

while error > Di:
    
    x_new = [0]*n
    
    for i in range(n):
        suma = 0
        
        for j in range(n):
            if i != j:
                suma += A[i][j] * x[j]
        
        x_new[i] = (b[i] - suma) / A[i][i]

    error = max(abs(x_new[i] - x[i]) for i in range(n))

    iteracion += 1

    print("Iteracion", iteracion)
    print("Valores:", x_new)
    print("Error:", error)
    print()

    x = x_new.copy()

print("Resultado final:", x)
print("Error final:", error)