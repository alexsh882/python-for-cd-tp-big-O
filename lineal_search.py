def lineal_search(list: list, target: int) -> int | None:
    '''
    Función que devuelve el índice del elemento ingresado en el segundo parámetro.
    '''

    # Se recorre la lista y se compara cada elemento con el elemento buscado.
    # Si son iguales, se devuelve un mensaje con el elemento, el indice y cantidad de elementos totales.
    # Al final del ciclo, si no se encontró el elemento, se devuelve el mensaje.
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None
