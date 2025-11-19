import time
import matplotlib.pyplot as plt
from metodos.utilidades import matriz_dist
from metodos.fuerza_bruta import tsp_fuerza_bruta
from metodos.greedy import tsp_greedy
from metodos.dinamica import tsp_dinamica

def dibujar_ruta(ciudades, ruta, titulo):

    if ruta is None:
        print(f"No se puede dibujar {titulo} (demasiadas ciudades)")
        return
    
    # Convertir ruta a lista si es tupla y preparar coordenadas x e y (incluyendo regreso al inicio)
    ruta_lista = list(ruta) if isinstance(ruta, tuple) else ruta
    x = [ciudades[i][0] for i in ruta_lista + [ruta_lista[0]]]
    y = [ciudades[i][1] for i in ruta_lista + [ruta_lista[0]]]
    
    # Crear figura
    plt.figure()
    plt.plot(x, y, 'o-', label=titulo)
    
    # Etiquetar cada ciudad con su número
    for i, (xi, yi) in enumerate(ciudades):
        plt.text(xi, yi, str(i))
    
    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ciudades = [
        (0, 0), 
        (3, 2),
        (8, 3),
        (6, 1),
        (1, 5),
        (9, 0),
        (12, 3),
        (13, 1),
        (15, 2),
        (17, 4),
        (19, 7)
    ]

    M = matriz_dist(ciudades)

    print("Número de ciudades:", len(ciudades))
    print("")

    # Fuerza Bruta
    t1 = time.time()
    r1, c1 = tsp_fuerza_bruta(M)
    t1 = time.time() - t1

    # Greedy
    t2 = time.time()
    r2, c2 = tsp_greedy(M)
    t2 = time.time() - t2

    # Dinámica
    t3 = time.time()
    r3, c3 = tsp_dinamica(M)
    t3 = time.time() - t3

    print("=== Resultados ===")
    print("Fuerza Bruta:")
    print("  Ruta:", r1)
    print("  Costo:", round(c1, 2))
    print("  Tiempo:", round(t1, 5), "s\n")

    print("Greedy:")
    print("  Ruta:", r2)
    print("  Costo:", round(c2, 2))
    print("  Tiempo:", round(t2, 5), "s\n")

    print("Dinámica:")
    print("  Ruta:", r3)
    print("  Costo mínimo:", round(c3, 2))
    print("  Tiempo:", round(t3, 5), "s")

    # Menú para elegir qué gráfica mostrar
    while True:
        print("\n Rutas de los metodos:")
        print("1. Ver gráfica de Fuerza Bruta")
        print("2. Ver gráfica de Greedy")
        print("3. Ver gráfica de Programación Dinámica")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            dibujar_ruta(ciudades, r1, "Fuerza Bruta")
        elif opcion == "2":
            dibujar_ruta(ciudades, r2, "Greedy")
        elif opcion == "3":
            dibujar_ruta(ciudades, r3, "Programación Dinámica")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")