from .utilidades import costo

def tsp_greedy(M):
    n = len(M)
    visitado = [False]*n
    ruta = [0]
    visitado[0] = True

    actual = 0
    for _ in range(n-1):
        menor = None
        sig = None
        for j in range(n):
            if not visitado[j]:
                if menor is None or M[actual][j] < menor:
                    menor = M[actual][j]
                    sig = j
        ruta.append(sig)
        visitado[sig] = True
        actual = sig

    return ruta, costo(ruta, M)