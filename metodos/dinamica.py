def tsp_dinamica(M):
    n = len(M)
    memo = {}
    padre = {}

    def dp(ciudad, mask):
        if (ciudad, mask) in memo:
            return memo[(ciudad, mask)]

        if mask == (1 << n) - 1:
            return M[ciudad][0]

        mejor = float("inf")
        mejor_nxt = -1

        for nxt in range(n):
            if (mask & (1 << nxt)) == 0:
                nuevo = M[ciudad][nxt] + dp(nxt, mask | (1 << nxt))
                if nuevo < mejor:
                    mejor = nuevo
                    mejor_nxt = nxt

        padre[(ciudad, mask)] = mejor_nxt
        memo[(ciudad, mask)] = mejor
        return mejor

    costo_min = dp(0, 1)

    # reconstruir la ruta
    ruta = [0]
    mask = 1
    ciudad = 0
    for _ in range(n - 1):
        nxt = padre[(ciudad, mask)]
        ruta.append(nxt)
        mask |= (1 << nxt)
        ciudad = nxt

    return ruta, costo_min