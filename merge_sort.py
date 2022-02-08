

array = [5,6,7,8,99, 1,2,3,4]

# O(n²)
# Omega (n²)


def merge_sort(array):
    array_length = len(array)

    half = array_length  // 2

    left = [None] * (half)

    right = [None] * (array_length - half)

    for i in range(0, half):
        left[i] = array[i]
    
    for i in range(0, array_length - half):
        right[i] = array[i+half]

    if len(left) > 1:
        left_merged = merge_sort(left)
    else:
        left_merged = left

    if len(right) > 1:
        right_merged = merge_sort(right)
    else:
        right_merged = right
     
    return intercala(left_merged+right_merged, 0, half, array_length)

def intercala(array, inicio, meio, fim):
    array_copy = [None] * (fim - inicio)
    atual = 0
    atual1 = inicio
    atual2 = meio

    while(atual1 < meio and atual2 < fim):
        if array[atual1] > array[atual2]:
            array_copy[atual] = array[atual2]
            atual2+=1
        else:
            array_copy[atual] = array[atual1]
            atual1+=1
        atual+=1
    
    while(atual1 < meio):
        array_copy[atual] = array[atual1]
        atual1+=1
        atual+=1

    while(atual2 < fim):
        array_copy[atual] = array[atual2]
        atual2+=1
        atual+=1
    
    for i in range(0, atual):
        array[i+inicio] = array_copy[i]
    
    return array


    

if __name__ == "__main__":
    print(merge_sort(array))
