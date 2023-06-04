def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

# Assume my_list is a pre-defined linked list
my_list.head = insert_at_beginning(my_list.head, 0)
my_list.display_list()
