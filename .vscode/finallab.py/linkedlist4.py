def delete_node(head, target):
    if head is None:
        return head

    if head.data == target:
        return head.next

    current = head
    while current.next:
        if current.next.data == target:
            current.next = current.next.next
            return head
        current = current.next

    return head


my_list.head = delete_node(my_list.head, 2)
my_list.display_list()
