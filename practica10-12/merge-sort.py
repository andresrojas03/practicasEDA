import matplotlib.pyplot as plt
import time
import random
import math


def merge_sort(lista):
    
    if len(lista) < 2:
        return lista
    #dividir la lista en sublistas de manera recursiva
    else:
        middle = len(lista)//2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right,left)

def merge(lista1, lista2):
    i, j = 0, 0
    result = []

    while(i < len(lista1) and j < len(lista2)):
        if(lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1 
        else: 
            result.append(lista2[j])
            j += 1
    
    result += lista1[i:]
    result += lista2[j:]

    return result

def medir_tiempo():
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
    times = []

    for size in sizes:
        lista = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        merge_sort(lista)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f'Size: {size}, Time: {end_time - start_time} seconds')

    return sizes, times
    
def theoretical_curve(sizes):
    theoretical = [size * math.log(size) for size in sizes]
    max_time = max(times)
    max_theoretical = max(theoretical)
    normalization_factor = max_time / max_theoretical
    return [t * normalization_factor for t in theoretical]


def plot_time(sizes, times, theoretical_times):
    plt.figure(figsize=(10, 6))

    plt.scatter(sizes, times, color = 'b', label = 'Execution time')
    plt.plot(sizes, theoretical_times, marker='', linestyle='-', color = 'r', label = 'theoric curve $n \\log n$')

    plt.xlabel('Array size')
    plt.ylabel('Execution time (seconds)')
    plt.title('Execution time Merge-Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

sizes, times = medir_tiempo()
theoretical_times = theoretical_curve(sizes)
plot_time(sizes, times, theoretical_times)


