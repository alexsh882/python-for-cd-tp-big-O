def binary_search(list: list, target: int) -> list | None:
    """
    Función que devuelve el índice del elemento ingresado en el segundo parámetro.
    """
    left_index = 0
    right_index = len(list) - 1

    # Mientras el índice izquierdo sea menor o igual al derecho, se ejecutará el ciclo.
    while left_index <= right_index:

        # Se calcula el índice medio.
        middle = left_index + (right_index - left_index) // 2

        # Se compara el elemento en el índice medio con el elemento buscado.
        # Si son iguales, se devuelve un mensaje con el elemento, el indice y cantidad de elementos totales.
        # Si no son iguales, se actualiza el índice izquierdo o derecho según sea el caso.
        # Al final del ciclo, si no se encontró el elemento, se devuelve el mensaje.
        if list[middle] == target:
            return middle
        # Si el elemento en el índice medio es menor al elemento buscado, se actualiza el índice izquierdo.
        elif list[middle] < target:
            left_index = middle + 1
        # Si el elemento en el índice medio es mayor al elemento buscado, se actualiza el índice derecho.
        else:
            right_index = middle - 1

    return None


def binary_search_n(n):
    """
    Función que devuelve el índice del elemento ingresado en el segundo parámetro.
    """
    list = [i for i in range(n)]
    target = n - 1

    return binary_search(list, target)