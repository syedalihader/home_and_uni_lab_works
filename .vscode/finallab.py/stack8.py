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


def evaluate_prefix(expression):
    stack = Stack()

    # Iterate through each character in the expression in reverse order
    for char in reversed(expression):
        # If the character is an operand, push it onto the stack
        if char.isdigit():
            stack.push(int(char))
        else:
            # If the character is an operator, pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Perform the operation based on the operator
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2

            # Push the result back onto the stack
            stack.push(result)

    # The final result will be the only item left on the stack
    return stack.pop()


# Example usage:
prefix_expr = "+9*26"
result = evaluate_prefix(prefix_expr)
print(result)  # Output: 21
