import time

def benchmark(func, *args):
    '''
    Función que mide el tiempo de ejecución de una función e muestra por consola el resultado en segundos.
    '''
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    
    time_to_execute = end_time - start_time

    return time_to_execute
