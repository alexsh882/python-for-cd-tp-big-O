def bubble_sort(arr):
    """
    Función que ordena un arreglo de números de menor a mayor.
    """
    n = len(arr)
    if type(arr) != list:
        return None
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_n(n):
    arr = [i for i in range(n, 0, -1)]
    return bubble_sort(arr)
