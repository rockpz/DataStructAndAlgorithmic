import collections

"""
collections.deque methods
extend
extendleft
pop
popleft
rotate
reverse
"""

de = collections.deque([1,2,3])
print("The deque is: ")
print(de)

de.extend([4,5,6])
print("The deque after extending deque at end is : ")
print(de)

de.extendleft([7,8,9])
print("The deque after extending deque at beginning is : ")
print(de)

de.rotate(-3)
print("The deque after rotating deque is : ")
print(de)

de.reverse()
print("The deque after reversing deque is : ")
print(de)