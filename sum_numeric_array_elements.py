def sum_numeric_array_numbers(arr):
    """
    Función que retorna la suma de los elementos numéricos de un arreglo.
    """
    sum = 0
    for element in arr:
        if type(element) == int or type(element) == float:
            sum += element
    return sum

def sum_numeric_array_numbers_n(n):
    """
    Función que retorna la suma de los elementos numéricos de un arreglo.
    """
    arr = [i for i in range(n)]
    return sum_numeric_array_numbers(arr)