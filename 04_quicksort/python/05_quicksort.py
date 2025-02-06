def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

# ----------

import random

def quicksort(array):
    if len(array) < 2:
        return array  # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    else:
        pivot_index = random.randint(0, len(array) - 1)  # Escolhe um pivô aleatório
        pivot = array[pivot_index]
        
        # Particionamento dos elementos em relação ao pivô
        less = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        
        return quicksort(less) + equal + quicksort(greater)

# Exemplo de uso
print(quicksort([10, 5, 2, 3]))
