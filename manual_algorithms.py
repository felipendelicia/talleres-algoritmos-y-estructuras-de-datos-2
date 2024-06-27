def lineal_search(arr:list[int], element:int)->int:
    # Inicializar un índice para recorrer la lista
    i = 0;

    # Iterar sobre la lista mientras el índice sea menor que la longitud de la lista
    # y el elemento en el índice actual no sea igual al elemento buscado
    while (i < len(arr) and arr[i]!= element):
        i += 1

    # Si el índice es menor que la longitud de la lista, significa que se encontró el elemento
    if i < len(arr): return i
    else: return -1

def binary_search(arr:list[int], element:int, left:int, right:int)->int:
    while left <= right:
        # Calcular el índice medio del arreglo
        mid = (left + right) // 2
        
        # Verificar si el objetivo está en el medio
        if arr[mid] == element:
            return mid
        
        # Si el objetivo es menor que el valor medio, buscar en la mitad izquierda del arreglo
        if arr[mid] > element:
            right = mid - 1
        # Si el objetivo es mayor que el valor medio, buscar en la mitad derecha del arreglo
        else:
            left = mid + 1
            
    # Si el objetivo no está en el arreglo, retornar -1
    return -1

def insertion_sort(arr: list[int]) -> list[int]:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # Desplazamos hacia la derecha los elementos de la lista
        # que sean mayores que 'key' para hacer espacio para 'key'
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1

        # Insertamos 'key' en su posición correcta
        arr[i + 1] = key

array = [34,2,5,6,8,7, 6]

def selection_sort(arr: list[int])->list[int]:
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(array)

print(array)