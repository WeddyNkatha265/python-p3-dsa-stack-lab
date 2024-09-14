class Stack:
    def __init__(self, items=None, limit=100):
        # Initialize the stack with an optional list of items and a size limit
        self.items = items if items is not None else []
        self.limit = limit
    
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.items) == 0
    
    def push(self, item):
        # Add an item to the top of the stack if not full
        if not self.full():
            self.items.append(item)
    
    def pop(self):
        # Remove and return the top item of the stack if not empty
        if not self.isEmpty():
            return self.items.pop()
        return None
    
    def peek(self):
        # Return the top item of the stack without removing it
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        # Return the number of items in the stack
        return len(self.items)
    
    def full(self):
        # Check if the stack is full
        return len(self.items) >= self.limit
    
    def search(self, target):
        # Search for an item in the stack and return its distance from the top
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1
