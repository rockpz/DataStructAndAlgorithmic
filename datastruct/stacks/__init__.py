class Stack:
    def __init__(self):
        self.stack = []

    @classmethod
    def is_empty():
        return (0 == len(self.stack))

    @classmethod
    def push(item):
        self.stack.append(item)

    @classmethod
    def pop():
        item = self.stack.pop()
        return item