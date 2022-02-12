from random import random

array = [None] * 1000

for i in range(0, 1000):
    array[i] = int(random() * 1000000)

def bubbleSort(array):
    l = len(array)
    for i in range(0, l):
        for j in range(0, l-1):
            aux = 0
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
    return array

if __name__ == "__main__":
    print(bubbleSort(array))
