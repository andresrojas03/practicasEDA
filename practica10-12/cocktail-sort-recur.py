import time
import random
import matplotlib.pyplot as plt
import math

def cocktailSortRecursive(a, start, end):
    if start >= end:
        return

    swapped = False

    for i in range(start, end):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True

    if not swapped:
        return

    end -= 1
    swapped = False

    for i in range(end, start, -1):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            swapped = True

    start += 1
    cocktailSortRecursive(a, start, end)

def cocktailSort(a):
    cocktailSortRecursive(a, 0, len(a) - 1)

def theoretical_curve(sizes, times):
    theoretical = [size * math.log(size) for size in sizes]
    max_time = max(times)
    max_theoretical = max(theoretical)
    normalization_factor = max_time / max_theoretical
    return [t * normalization_factor for t in theoretical]
# Función para medir el tiempo de ejecución para diferentes tamaños de entrada
def measure_time():
    input_sizes = [1, 2, 10, 15, 20, 25, 30, 50, 70, 100, 150, 260, 300, 500, 1000, 2000]
    times = []

    for size in input_sizes:
        a = [random.randint(0, 10000) for _ in range(size)]  # Generar una lista aleatoria de tamaño `size`
        
        start_time = time.perf_counter()
        cocktailSort(a)
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000  # Convertir a milisegundos
        times.append(execution_time)
        print(f'Size: {size}, Time: {execution_time:.6f} ms')

    theoretical_times = theoretical_curve(input_sizes, times)
    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker = 'x', linestyle = '--', color = 'g', label = 'empirical time')
    plt.plot(input_sizes, theoretical_times, marker='o', linestyle='-', color='b', label = 'theorical time')
    plt.title('Cocktail Sort Execution Time')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Llamar a la función para medir el tiempo y graficar
measure_time()
