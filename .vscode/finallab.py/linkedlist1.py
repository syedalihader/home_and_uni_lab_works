class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Create a linked list
my_list = LinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.display_list()
