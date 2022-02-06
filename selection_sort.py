array = [2, 3, 6, 90, 7, 98, 1]

# O(n²)
# Omega (n²)


def selection_sort(array):
    array_length = len(array)
    for i in range(0, array_length):
        # finding the smallest number position
        smallest_number_position = i
        for j in range(i, array_length):
            if array[smallest_number_position] > array[j]:
                smallest_number_position = j

        # swapping where i position with the position of the smallest number
        if smallest_number_position != i:
            aux = array[i]
            array[i] = array[smallest_number_position]
            array[smallest_number_position] = aux
    return array


if __name__ == "__main__":
    print(selection_sort(array))
