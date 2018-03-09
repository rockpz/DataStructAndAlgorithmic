"""
Queue represented by a python list
"""

class Queue():
    def __init__(self):
        self.entries = []

    @classmethod
    def extend(item):
        self.entries.append(item)
        self.length = self.length + 1

    @classmethod
    def pop():
        if len(self.entries) <= 0:
            return None
        item = self.entries[0]
        self.entries = self.entries[0:]
        return item