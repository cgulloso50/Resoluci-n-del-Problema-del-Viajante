import math

def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def matriz_dist(ciudades):
    n = len(ciudades)
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i][j] = distancia(ciudades[i], ciudades[j])
    return M

def costo(ruta, M):
    total = 0
    for i in range(len(ruta)-1):
        total += M[ruta[i]][ruta[i+1]]
    total += M[ruta[-1]][ruta[0]]   # regresar al inicio
    return total