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


def are_parentheses_balanced(expression):
    stack = Stack()

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening parenthesis, push it onto the stack
        if char in '([{':
            stack.push(char)
        # If the character is a closing parenthesis
        elif char in ')]}':
            # If the stack is empty or the corresponding opening parenthesis is not at the top, parentheses are not balanced
            if stack.is_empty() or not is_matching_pair(stack.pop(), char):
                return False

    # If the stack is empty after evaluating the entire expression, parentheses are balanced
    return stack.is_empty()


def is_matching_pair(opening, closing):
    if opening == '(' and closing == ')':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True
    else:
        return False


# Example usage:
expression1 = "((2 + 3) * [5 - 1])"
expression2 = "({[}])"
print(are_parentheses_balanced(expression1))  # Output: True
print(are_parentheses_balanced(expression2))  # Output: False
