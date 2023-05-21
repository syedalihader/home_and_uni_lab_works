#ANSWER NO 6.4
'''def remove_all_elements(stack):
    if not stack:
        return  
    else:
        stack.pop()  
        remove_all_elements(stack)  

my_stack = [1, 2, 3, 4, 5]
print("Original Stack:", my_stack)

remove_all_elements(my_stack)

print("Stack after removal:", my_stack)'''
#ANSWER NO6.5
'''def reverse_list(lst):
    stack = []
    for element in lst:
        stack.append(element) 

    lst.clear()  

    while stack:
        lst.append(stack.pop())  

    return lst
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

reversed_list = reverse_list(my_list)

print("Reversed List:", reversed_list)'''

#ANSWER NO 6,6
'''Every opening symbol must be followed by its corresponding closing symbol.
Opening symbols cannot be closed by a different type of symbol. For example, a closing parenthesis ")" cannot match an opening square bracket "[".
The symbols must be nested correctly, meaning that a closing symbol should not precede its corresponding opening symbol.
The process of matching symbols in an arithmetic expression can be performed using a stack data structure. As the expression is parsed character by character, opening symbols are pushed onto the stack. When a closing symbol is encountered, it is compared with the top element of the stack. If they match and have the same type, the opening symbol is popped from the stack, indicating that the pair is properly matched. If they don't match or the stack is empty, it implies a mismatch in the expression.

By maintaining a stack and performing symbol matching, it becomes possible to determine whether an arithmetic expression has balanced and correctly matched symbols. This is crucial for ensuring the expression's syntactical validity and proper evaluation.'''
 
 #ANSWER NO 6.7
'''class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


def process_queue_operations():
    my_queue = Queue()

    # Perform the sequence of queue operations
    returned_values = []

    returned_values.append(my_queue.dequeue())
    my_queue.enqueue(2)
    my_queue.enqueue(8)
    returned_values.append(my_queue.dequeue())
    returned_values.append(my_queue.dequeue())
    my_queue.enqueue(9)
    my_queue.enqueue(7)
    my_queue.enqueue(6)
    returned_values.append(my_queue.dequeue())
    my_queue.dequeue()
    my_queue.dequeue()

    return returned_values


# Execute the program and display the returned values
results = process_queue_operations()
print("Returned Values:", results)
'''
#ANSWER NO 6,8
'''class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def calculate_queue_size(enqueue_operations, dequeue_operations, ignored_errors):
    my_queue = Queue()
    for _ in range(enqueue_operations):
        my_queue.enqueue(None)  # Adding None as a placeholder

    for _ in range(dequeue_operations):
        try:
            my_queue.dequeue()
        except Exception:
            if ignored_errors > 0:
                ignored_errors -= 1

   
    return my_queue.size()

enqueue_ops = 32
dequeue_ops = 15
ignored_errors = 5

current_size = calculate_queue_size(enqueue_ops, dequeue_ops, ignored_errors)
print("Current Size of the Queue:", current_size)
'''
#ANSWER NO 6.9
'''Initial front = 0 (assuming it starts at the beginning of the array)

After 15 dequeue operations:
front = (front + 15) % 30 = (0 + 15) % 30 = 15

Therefore, the final value of the front instance variable would be 15.
'''
#ANSWER NO 6.1
'''class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def process_stack_operations():
    my_stack = Stack()

    # Perform the series of stack operations
    returned_values = []

    my_stack.push(5)
    my_stack.push(3)
    returned_values.append(my_stack.pop())
    my_stack.push("?")
    my_stack.push("B")
    returned_values.append(my_stack.pop())
    returned_values.append(my_stack.pop())
    my_stack.push(9)
    my_stack.push(1)
    returned_values.append(my_stack.pop())
    my_stack.push(7)
    my_stack.push(6)
    returned_values.append(my_stack.pop())
    returned_values.append(my_stack.pop())
    my_stack.push(4)
    returned_values.append(my_stack.pop())
    returned_values.append(my_stack.pop())

    return returned_values


# Execute the program and display the returned values
results = process_stack_operations()
print("Returned Values:", results)
'''
#ANSWER NO 6.2
'''class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def calculate_stack_size(push_operations, top_operations, pop_operations, ignored_errors):
    my_stack = Stack()

    for _ in range(push_operations):
        my_stack.push(None)  # Adding None as a placeholder

    for _ in range(top_operations):
        try:
            my_stack.top()
        except Exception:
            if ignored_errors > 0:
                ignored_errors -= 1


    for _ in range(pop_operations):
        try:
            my_stack.pop()
        except Exception:
            if ignored_errors > 0:
                ignored_errors -= 1

    return my_stack.size()


# Execute the program and display the current size of the stack
push_ops = 25
top_ops = 12
pop_ops = 10
ignored_errors = 3

current_size = calculate_stack_size(push_ops, top_ops, pop_ops, ignored_errors)
print("Current Size of the Stack:", current_size)
'''
#answre no 6,3
'''class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def single_transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())

    bottom_element = T.pop()
    T_temp = Stack()
    while not T.is_empty():
        T_temp.push(T.pop())

    T.push(bottom_element)

    while not T_temp.is_empty():
        T.push(T_temp.pop())

stack_S = Stack()
stack_T = Stack()

stack_S.push(1)
stack_S.push(2)
stack_S.push(3)
stack_S.push(4)
stack_S.push(5)

single_transfer(stack_S, stack_T)

while not stack_T.is_empty():
    print(stack_T.pop())
'''
#answer no 6.11
'''from collections import deque


class QueueAdapter:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue = QueueAdapter()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.size())  
queue.enqueue(4)

print(queue.dequeue())  
print(queue.is_empty())'''
# answer no 6.12
'''from collections import deque



my_deque = deque()


returned_values = []

my_deque.appendleft(4)
my_deque.append(8)
my_deque.append(9)
my_deque.appendleft(5)
returned_values.append(my_deque[-1])
my_deque.popleft()
my_deque.pop()
my_deque.append(7)
returned_values.append(my_deque[0])
returned_values.append(my_deque[-1])
my_deque.append(6)
my_deque.popleft()
my_deque.popleft()

print("Returned Values:", returned_values)
''' 
#answer no 13
'''from collections import deque



D = deque([1, 2, 3, 4, 5, 6, 7, 8])

Q = deque()

while len(D) > 0:
    if len(D) % 2 == 0:
        Q.append(D.popleft())
    else:
        D.append(D.popleft())


while len(Q) > 0:
    D.append(Q.popleft())

print(D)
'''
#answer no 6,4
'''from collections import deque


# Initialize deque D with the numbers (1, 2, 3, 4, 5, 6, 7, 8)
D = deque([1, 2, 3, 4, 5, 6, 7, 8])

# Initialize an empty stack S
S = []

# Rearrange the elements in deque D
while len(D) > 0:
    if len(D) % 2 == 0:
        S.append(D.popleft())
    else:
        D.append(D.popleft())

# Add the elements from stack S back to deque D in the desired order
while len(S) > 0:
    D.append(S.pop())

# Display the elements in deque D after rearrangement
print(D)
'''
