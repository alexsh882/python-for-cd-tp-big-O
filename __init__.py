import matplotlib.pyplot as plt

from bubble_sort import bubble_sort_n
from binary_search import binary_search_n
from benchmark import benchmark
from lineal_search import lineal_search
from quick_sort import quicksort
from first_element_array import first_element_array
from sum_numeric_array_elements import sum_numeric_array_numbers

N = 100;


def o_test(func):
    """
    Función que mide el tiempo de ejecución de la función.
    """
    results = []
    for i in range(1, N + 1):
        results.append(benchmark(func, i))
    return results


def graph(results):
    """
    Función que grafica los resultados de la función.
    """
    plt.plot(results)
    plt.show()

def main():
    """
    Función principal el benchmarking de las funciones.
    """
    # Se ejecuta la función de búsqueda binaria.
    print('binary', o_test(binary_search_n))
    print('bubble', o_test(bubble_sort_n))



if __name__ == '__main__':
    main()