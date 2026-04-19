import time
import random
import matplotlib.pyplot as plt

# Arreglo construido con los digitos de mi cedula: 1020456331
# Los ceros se reemplazan por el ultimo digito no cero (1)
# Signos alternados: positivo, negativo, positivo...
# Cedula: 1 0 2 0 4 5 6 3 3 1
# Ceros -> 1  => 1 1 2 1 4 5 6 3 3 1
# Alternado  => [1, -1, 2, -1, 4, -5, 6, -3, 3, -1]

MI_ARREGLO = [1, -1, 2, -1, 4, -5, 6, -3, 3, -1]


# --- FUERZA BRUTA ---
# Revisa todas las combinaciones posibles de subarreglos
# Complejidad: O(n^2)

def fuerza_bruta(arr):
    n = len(arr)
    mejor_suma = float('-inf')
    inicio = 0
    fin = 0

    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += arr[j]
            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                inicio = i
                fin = j

    return mejor_suma, inicio, fin


# --- DIVIDE Y VENCERAS ---
# Caso base: un solo elemento
# Divide el arreglo en mitad izquierda, mitad derecha y cruce
# Complejidad: O(n log n)

def subarreglo_cruzado(arr, izq, mid, der):
    suma_izq = float('-inf')
    acum = 0
    limite_izq = mid

    for i in range(mid, izq - 1, -1):
        acum += arr[i]
        if acum > suma_izq:
            suma_izq = acum
            limite_izq = i

    suma_der = float('-inf')
    acum = 0
    limite_der = mid + 1

    for j in range(mid + 1, der + 1):
        acum += arr[j]
        if acum > suma_der:
            suma_der = acum
            limite_der = j

    return suma_izq + suma_der, limite_izq, limite_der


def divide_y_venceras(arr, izq, der):
    if izq == der:
        return arr[izq], izq, der

    mid = (izq + der) // 2

    suma_izq, i_izq, f_izq = divide_y_venceras(arr, izq, mid)
    suma_der, i_der, f_der = divide_y_venceras(arr, mid + 1, der)
    suma_cruz, i_cruz, f_cruz = subarreglo_cruzado(arr, izq, mid, der)

    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return suma_izq, i_izq, f_izq
    elif suma_der >= suma_izq and suma_der >= suma_cruz:
        return suma_der, i_der, f_der
    else:
        return suma_cruz, i_cruz, f_cruz


def dyv(arr):
    return divide_y_venceras(arr, 0, len(arr) - 1)


# --- PRUEBA CON MI ARREGLO ---

suma_fb, i, j = fuerza_bruta(MI_ARREGLO)
print("Arreglo:", MI_ARREGLO)
print(f"\nFuerza bruta      -> subarreglo: {MI_ARREGLO[i:j+1]}, suma: {suma_fb}")

suma_dv, i, j = dyv(MI_ARREGLO)
print(f"Divide y venceras -> subarreglo: {MI_ARREGLO[i:j+1]}, suma: {suma_dv}")


# --- MEDICION DE TIEMPOS ---

tamanos = [10, 50, 100, 200, 500, 1000]
tiempos_fb = []
tiempos_dv = []
repeticiones = 5

for n in tamanos:
    t_fb = 0
    t_dv = 0
    for _ in range(repeticiones):
        arr = [random.randint(-100, 100) for _ in range(n)]

        t0 = time.perf_counter()
        fuerza_bruta(arr)
        t_fb += time.perf_counter() - t0

        t0 = time.perf_counter()
        dyv(arr)
        t_dv += time.perf_counter() - t0

    tiempos_fb.append(t_fb / repeticiones)
    tiempos_dv.append(t_dv / repeticiones)

print("\nn          Fuerza bruta (s)    Divide y venceras (s)")
print("-" * 52)
for n, tf, td in zip(tamanos, tiempos_fb, tiempos_dv):
    print(f"{n:<12} {tf:<20.6f} {td:<20.6f}")


# --- GRAFICA ---

COLOR_FB   = "#7B3F8C"   
COLOR_DV   = "#C47DB5"   
COLOR_BG   = "#FAF7F2"   
COLOR_GRID = "#EDE5DC"   
COLOR_TEXT = "#3D2B3D"   

plt.rcParams.update({
    "font.family":      "serif",
    "axes.facecolor":   COLOR_BG,
    "figure.facecolor": COLOR_BG,
    "axes.edgecolor":   "#C5B4C5",
    "axes.linewidth":   0.8,
    "grid.color":       COLOR_GRID,
    "grid.linewidth":   0.9,
    "xtick.color":      COLOR_TEXT,
    "ytick.color":      COLOR_TEXT,
    "text.color":       COLOR_TEXT,
})

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor(COLOR_BG)

ax.plot(tamanos, tiempos_fb,
        color=COLOR_FB, linewidth=1.2,
        marker="o", markersize=9,
        markerfacecolor=COLOR_FB, markeredgecolor="white", markeredgewidth=1.5,
        label="Fuerza Bruta  ·  O(n²)")

ax.plot(tamanos, tiempos_dv,
        color=COLOR_DV, linewidth=1.2,
        marker="o", markersize=9,
        markerfacecolor=COLOR_DV, markeredgecolor="white", markeredgewidth=1.5,
        label="Divide y Vencerás  ·  O(n log n)")

ax.set_title(
    "¿Cómo crece el tiempo al buscar el subarreglo máximo?\n"
    "Fuerza Bruta O(n²) vs. Divide y Vencerás O(n log n)",
    fontsize=13, fontweight="bold", color=COLOR_TEXT, pad=18, linespacing=1.6
)
ax.set_xlabel("Tamaño del arreglo  (n)", fontsize=11, labelpad=10)
ax.set_ylabel("Tiempo promedio de ejecución  (segundos)", fontsize=11, labelpad=10)

ax.set_xticks(tamanos)
ax.grid(True, linestyle="--", alpha=0.7)
ax.tick_params(axis="both", labelsize=10)

ax.legend(fontsize=10, framealpha=0.9, facecolor="#F3EBF3",
          edgecolor="#C5B4C5", loc="upper left")

fig.text(0.5, -0.02,
         "Cada punto representa el promedio de 5 ejecuciones con arreglos aleatorios.",
         ha="center", fontsize=9, color="#7A6A7A", style="italic")

plt.tight_layout()
plt.savefig("graficas/grafica_subarreglo.png", dpi=180, bbox_inches="tight", facecolor=COLOR_BG)
print("\nGrafica guardada graficas/grafica_subarreglo.png")
plt.show()
