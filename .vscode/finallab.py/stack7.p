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

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]


class UndoRedoStack:
    def __init__(self):
        self.state_stack = Stack()
        self.redo_stack = Stack()

    def push_state(self, state):
        self.state_stack.push(state)
        # Clear redo stack since a new state is pushed
        self.redo_stack = Stack()

    def undo(self):
        if self.state_stack.is_empty():
            return "Nothing to undo"
        state = self.state_stack.pop()
        self.redo_stack.push(state)
        return state

    def redo(self):
        if self.redo_stack.is_empty():
            return "Nothing to redo"
        state = self.redo_stack.pop()
        self.state_stack.push(state)
        return state


# Example usage:
stack = UndoRedoStack()
stack.push_state("State 1")
stack.push_state("State 2")
stack.push_state("State 3")

print(stack.undo())  # Output: State 2
print(stack.redo())  # Output: State 3
print(stack.undo())  # Output: State 2
print(stack.undo())  # Output: State 1
print(stack.redo())  # Output: State 2
