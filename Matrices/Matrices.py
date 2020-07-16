filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))
matriz0 = []
matriz1 = []
matriz2 = []
matriz3 = []
for i in range (filas):
    for o in range(columnas):
        valor=int(input("ingrese valor:"))
        matriz0.append(valor)
    matriz1.append(matriz0.copy())
    matriz0.clear()
print (matriz1)
for i in range (filas):
    for o in range(columnas):
        valor=int(input("ingrese valor:"))
        matriz0.append(valor)
    matriz2.append(matriz0.copy())
    matriz0.clear()
print(matriz2)
for i in range (filas):
    for o in range(columnas):
        matriz0.append(matriz1[i][o]+matriz2[i][o])
    matriz3.append(matriz0.copy())
    matriz0.clear()
print("LA MATRIZ ES: ")
print(matriz3)