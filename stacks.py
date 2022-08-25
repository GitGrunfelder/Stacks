# A stack is much like a list, however you can only add and remove from the last item of the list. Think of it as LIFO(Last in first out)
class Stack:
    def __init__(self):
        self.items= []
        
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.is_empty())

stack.push(1)
print(stack.is_empty())
item = stack.pop()
print(item)
print(stack.is_empty())


# You can pass a string/sentence in via a for loop. For each character, push that character onto the stack.
# Then you can reverse via for loop, adding each item in the len of the stack back in reverse order to a new var.

for char in "Hello":
    stack.push(char)
    
print(stack.size())
print(stack.peek())

reverse = ""

for char in range(len(stack.items)):
    reverse += stack.pop()
    
print(reverse)