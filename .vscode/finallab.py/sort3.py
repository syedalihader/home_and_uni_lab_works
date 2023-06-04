def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [5, 2, 9, 1, 3]
selection_sort(my_list)
print("Sorted list:", my_list)
