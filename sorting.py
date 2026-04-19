import time
import random
import matplotlib.pyplot as plt

# Arreglo construido con los digitos de mi cedula: 1020456331
# Los ceros se reemplazan por 1 (ultimo digito no cero)
# Sin alternar signos, tal cual quedan los digitos
# => [1, 1, 2, 1, 4, 5, 6, 3, 3, 1]

MI_ARREGLO = [1, 1, 2, 1, 4, 5, 6, 3, 3, 1]


# --- MERGE SORT ---
# Divide el arreglo hasta tener partes de 1 elemento (caso base),
# luego las va fusionando en orden.
# Complejidad: O(n log n)

def fusionar(izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])

    return fusionar(izq, der)


# --- INSERTION SORT ---
# Toma cada elemento y lo ubica en su lugar correcto
# dentro de la parte ya ordenada del arreglo.
# Complejidad: O(n^2)

def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


# --- PRUEBA CON MI ARREGLO ---

print("Arreglo original:", MI_ARREGLO)
print("Merge Sort:      ", merge_sort(MI_ARREGLO))
print("Insertion Sort:  ", insertion_sort(MI_ARREGLO))


# --- MEDICION DE TIEMPOS ---

tamanos = [10, 50, 100, 500, 1000, 5000]
tiempos_ms = []
tiempos_is = []
repeticiones = 5

for n in tamanos:
    t_ms = 0
    t_is = 0
    for _ in range(repeticiones):
        arr = [random.randint(0, 10000) for _ in range(n)]

        t0 = time.perf_counter()
        merge_sort(arr)
        t_ms += time.perf_counter() - t0

        t0 = time.perf_counter()
        insertion_sort(arr)
        t_is += time.perf_counter() - t0

    tiempos_ms.append(t_ms / repeticiones)
    tiempos_is.append(t_is / repeticiones)

print("\nn          Merge Sort (s)      Insertion Sort (s)")
print("-" * 50)
for n, tm, ti in zip(tamanos, tiempos_ms, tiempos_is):
    print(f"{n:<12} {tm:<22.6f} {ti:<22.6f}")


# --- GRAFICA ---

COLOR_MS   = "#4A7C9E"   
COLOR_IS   = "#B5676B"   
COLOR_BG   = "#FAF7F2"   
COLOR_GRID = "#EDE5DC"   
COLOR_TEXT = "#2B2B3D"   

plt.rcParams.update({
    "font.family":      "serif",
    "axes.facecolor":   COLOR_BG,
    "figure.facecolor": COLOR_BG,
    "axes.edgecolor":   "#C0B8C5",
    "axes.linewidth":   0.8,
    "grid.color":       COLOR_GRID,
    "grid.linewidth":   0.9,
    "xtick.color":      COLOR_TEXT,
    "ytick.color":      COLOR_TEXT,
    "text.color":       COLOR_TEXT,
})

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor(COLOR_BG)

ax.plot(tamanos, tiempos_ms,
        color=COLOR_MS, linewidth=1.2,
        marker="o", markersize=9,
        markerfacecolor=COLOR_MS, markeredgecolor="white", markeredgewidth=1.5,
        label="Merge Sort  ·  O(n log n)")

ax.plot(tamanos, tiempos_is,
        color=COLOR_IS, linewidth=1.2,
        marker="o", markersize=9,
        markerfacecolor=COLOR_IS, markeredgecolor="white", markeredgewidth=1.5,
        label="Insertion Sort  ·  O(n²)")

ax.set_title(
    "¿Cuál algoritmo de ordenamiento escala mejor?\n"
    "Merge Sort O(n log n) vs. Insertion Sort O(n²)",
    fontsize=13, fontweight="bold", color=COLOR_TEXT, pad=18, linespacing=1.6
)
ax.set_xlabel("Tamaño del arreglo  (n)", fontsize=11, labelpad=10)
ax.set_ylabel("Tiempo promedio de ejecución  (segundos)", fontsize=11, labelpad=10)

ax.set_xticks(tamanos)
ax.grid(True, linestyle="--", alpha=0.7)
ax.tick_params(axis="both", labelsize=10)

ax.legend(fontsize=10, framealpha=0.9, facecolor="#EDF1F7",
          edgecolor="#C0B8C5", loc="upper left")

fig.text(0.5, -0.02,
         "Cada punto representa el promedio de 5 ejecuciones con arreglos aleatorios.",
         ha="center", fontsize=9, color="#7A6A7A", style="italic")

plt.tight_layout()
plt.savefig("graficas/grafica_sorting.png", dpi=180, bbox_inches="tight", facecolor=COLOR_BG)
print("\nGrafica guardada graficas/grafica_sorting.png")
plt.show()
