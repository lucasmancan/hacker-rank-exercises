from random import random

array = [None] * 1000000

for i in range(0, 1000000):
    array[i] = int(random() * 1000)
# O(n²)
# Omega (n²)

def merge_sort(array, inicio, fim):
    array_length = fim - inicio
    metade = (inicio + fim)  // 2 
    if array_length > 1:
        merge_sort(array, inicio, metade)
        merge_sort(array, metade, fim)
        intercala(array, inicio, metade, fim)
 

def intercala(array, inicio, meio, fim):
    array_copy = [None] * (fim - inicio)
    atual = 0
    atual1 = inicio
    atual2 = meio

    while(atual1 < meio and atual2 < fim):
        if array[atual1] > array[atual2]:
            array_copy[atual] = array[atual2]
            atual2 += 1
        else:
            array_copy[atual] = array[atual1]
            atual1 += 1
        atual += 1

    while(atual1 < meio):
        array_copy[atual] = array[atual1]
        atual1 += 1
        atual += 1

    while(atual2 < fim):
        array_copy[atual] = array[atual2]
        atual2 += 1
        atual += 1

    for i in range(0, atual):
        array[i+inicio] = array_copy[i]
    


if __name__ == "__main__":
    merge_sort(array, 0, len(array))
    print(array)
