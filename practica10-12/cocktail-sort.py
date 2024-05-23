import matplotlib.pyplot as plt
import time
import random
import math

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while swapped:

        # loop from left to right same as the bubble sort
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # from right to left, doing the same comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        start = start + 1

    return a

def theoretical_curve_nlogn(sizes):
    return [size * math.log(size) for size in sizes]

def theoretical_curve_n2(sizes):
    return [size**2 for size in sizes]

def theoretical_curve_n(sizes):
    return sizes

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

    # Calcular los valores teóricos para las cotas asintóticas
    theoretical_nlogn = theoretical_curve_nlogn(input_sizes)
    theoretical_n2 = theoretical_curve_n2(input_sizes)
    theoretical_n = theoretical_curve_n(input_sizes)
    
    # Graficar los resultados junto con las cotas asintóticas
    plt.figure(figsize=(10, 6))
    plt.scatter(input_sizes, times, color='g', label='Tiempo Empírico')
    plt.plot(input_sizes, theoretical_nlogn, linestyle='--', color='b', label='O(n log n)')
    plt.plot(input_sizes, theoretical_n2, linestyle='--', color='r', label='O(n^2)')
    plt.plot(input_sizes, theoretical_n, linestyle='--', color='m', label='O(n)')
    plt.title('Comparación de Tiempos de Ejecución con Cotas Asintóticas')
    plt.xlabel('Tamaño de Entrada')
    plt.ylabel('Tiempo de Ejecución (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()

measure_time()
