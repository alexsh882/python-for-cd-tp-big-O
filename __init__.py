import matplotlib.pyplot as plt

from bubble_sort import bubble_sort_n
from binary_search import binary_search_n
from benchmark import benchmark
from quick_sort import quicksort_n
from first_element_array import first_element_array_n
from sum_numeric_array_elements import sum_numeric_array_numbers_n
from fibonacci_sequence import fibonacci_sequence

# Cantidad de veces que se ejecutará la función.
N = 20


# Función que mide el tiempo de ejecución de la función dada como argumento.
def o_test(func):
    """
    Función que mide el tiempo de ejecución de la función.
    """
    results = []
    for i in range(1, N + 1):
        results.append(benchmark(func, i))
    return results


def graph(results, label):
    """
    Función que gráfica los resultados de la función.
    """
    plt.plot(results, label=label)
    plt.xlabel("n")
    plt.ylabel("tiempo")
    plt.title("Trabajo Práctico sobre Notación Big O - Python")
    plt.legend()
    return plt


def main():
    """
    Función principal el benchmarking de las funciones.
    """
    # Gráfica de las funciones.
    pt = graph(o_test(first_element_array_n), "O(1) - Constante")
    pt = graph(o_test(binary_search_n), "O(log n) - Logarítmica")
    pt = graph(o_test(sum_numeric_array_numbers_n), "O(n) - Lineal")
    pt = graph(o_test(quicksort_n), "O(n log n) - Linealítmica")
    pt = graph(o_test(bubble_sort_n), "O(n^2) - Cuadrática")
    pt = graph(o_test(fibonacci_sequence), "O(2^n) - Exponencial")
    pt.show()


if __name__ == "__main__":
    main()
