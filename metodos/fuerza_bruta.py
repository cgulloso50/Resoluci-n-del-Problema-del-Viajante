import itertools
from .utilidades import costo

def tsp_fuerza_bruta(M):
    n = len(M)
    mejor_ruta = None
    mejor_costo = float("inf")

    # fijamos ciudad 0 como inicio
    for perm in itertools.permutations(range(1, n)):
        ruta = (0,) + perm
        c = costo(ruta, M)
        if c < mejor_costo:
            mejor_costo = c
            mejor_ruta = ruta

    return mejor_ruta, mejor_costo