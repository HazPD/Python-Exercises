class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", stack) #Push: Adds items to the stack.

    print("Popped item:", stack.pop()) #Pop: Removes the top item from the stack.
    print("Stack after pop:", stack)

    print("Peek item:", stack.peek()) #Peek: Views the top item without removing it.
    print("Stack size:", stack.size()) #Size: Gets the number of items in the stack.    
    print("Is stack empty?", stack.is_empty()) #Is_empty: Checks if the stack is empty.