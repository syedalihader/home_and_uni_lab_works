class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def size(self):
        return len(self.stack)


def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    # Push each character of the input string onto the stack
    for char in input_string:
        stack.push(char)

    # Pop characters from the stack and append them to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# Example usage:
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: !dlroW ,olleH
