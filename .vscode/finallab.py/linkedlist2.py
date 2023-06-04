def search_element(head, target):
    current = head
    index = 0
    while current:
        if current.data == target:
            return index
        current = current.next
        index += 1
    return -1

# Assume my_list is a pre-defined linked list
index = search_element(my_list.head, 2)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
