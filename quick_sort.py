# función llamada quicksort que tome una lista.
def quicksort(list: list) -> list:
    ''' Función que ordena una lista de números enteros de menor a mayor
    '''

    # Dentro de la función, veriﬁca si la sublista tiene 0 o 1 elementos
    # Cuando el índice de inicio es mayor o igual al índice de fin
    # si es así, no hay nada que ordenar y la función debe terminar.

    if len(list) <= 1:
        return list

    # Elige un elemento de la sublista como pivote.
    # Un método simple es elegir el primer elemento de la sublista.
    
    pivot = list[0]

    # Reorganiza los elementos de la sublista de manera que los menores que el
    # pivote estén a su izquierda y los mayores a su derecha.
    min_left = []
    middle = []
    max_right = []

    for i in list:
        if i < pivot:
            min_left.append(i)
        elif i > pivot:
            max_right.append(i)
        else:
            middle.append(i)

    return quicksort(min_left) + middle + quicksort(max_right)


