📊 Laboratorio 1 – Análisis de Algoritmos
👩‍💻 Descripción del proyecto

En este proyecto desarrollé el Laboratorio 1 de la asignatura Análisis de Algoritmos, en el cual trabajé de manera práctica dos conceptos fundamentales: la recursividad y el paradigma de divide y vencerás.

Mi objetivo fue no solo implementar los algoritmos, sino también analizar su comportamiento real, comparando tiempos de ejecución y contrastando los resultados con la teoría de complejidad algorítmica.

🎯 Objetivos
Aplicar la recursividad en la solución de problemas.
Implementar el paradigma divide y vencerás.
Comparar algoritmos con diferentes complejidades.
Analizar el rendimiento mediante pruebas experimentales.
Relacionar resultados prácticos con teoría (notación Big-O).
🧩 Construcción de los datos

A partir de mi número de cédula construí dos arreglos:

Reemplacé los ceros por el último dígito no cero.
Generé:
Un arreglo con signos alternados (para subarreglo máximo).
Un arreglo positivo (para ordenamiento).

Arreglos utilizados:

Arreglo 1 (Subarreglo máximo):
[1, -1, 2, -1, 4, -5, 6, -3, 3, -1]

Arreglo 2 (Ordenamiento):
[1, 1, 2, 1, 4, 5, 6, 3, 3, 1]
⚙️ Algoritmos implementados
1. Subarreglo Máximo

Implementé dos enfoques:

🔴 Fuerza Bruta → Complejidad O(n²)
🟢 Divide y Vencerás → Complejidad O(n log n)

✔️ Resultado encontrado:

Subarreglo máximo: [6]
Suma máxima: 6
2. Ordenamiento

Comparé dos algoritmos:

🔵 Merge Sort → O(n log n)
🟡 Insertion Sort → O(n²)

✔️ Resultado final ordenado:

[1, 1, 1, 1, 2, 3, 3, 4, 5, 6]
⏱️ Metodología de medición
Implementé todos los algoritmos en Python.
Usé time.perf_counter() para medir tiempos.
Realicé 5 ejecuciones por cada tamaño de entrada.
Promedié los resultados para reducir ruido.
Generé arreglos aleatorios con random.randint().
📈 Resultados y análisis
🔹 Subarreglo máximo
Para tamaños pequeños (n ≤ 100), ambos algoritmos tienen tiempos similares.
A partir de n = 200, el algoritmo de fuerza bruta crece mucho más rápido.
Para n = 1000:
Divide y vencerás es casi 19 veces más rápido.

📌 Conclusión: La complejidad O(n²) se vuelve inviable rápidamente frente a O(n log n).

🔹 Ordenamiento
Para n pequeños (10–50), Insertion Sort es más rápido.
A partir de n = 100, Merge Sort domina claramente.
Para n = 5000:
Merge Sort es casi 49 veces más rápido.

📌 Conclusión: La notación Big-O se refleja en grandes volúmenes, pero no siempre en tamaños pequeños.

🧠 Aprendizajes

Durante este laboratorio aprendí que:

El caso base en recursividad es crítico; sin él, el algoritmo falla.
Divide y vencerás requiere entender bien la división y combinación.
La teoría (Big-O) sí se cumple en la práctica, pero depende del tamaño de entrada.
Los algoritmos simples pueden ser más eficientes en casos pequeños.
Elegir un algoritmo adecuado impacta directamente el rendimiento real.
🚀 Conclusión personal

Este proyecto me permitió entender que el análisis de algoritmos no es solo teoría. Al ver diferencias de hasta 49 veces en tiempo de ejecución, comprendí que elegir el algoritmo correcto puede definir si una solución es viable o no en escenarios reales.
