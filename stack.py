# -*- encoding: utf-8 -*-

# Stack() creates a new stack that is empty.
#    It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack.
#    It needs the item and returns nothing.
# pop() removes the top item from the stack.
#    It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it.
#    It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty.
#    It needs no parameters and returns a boolean value.


class Stack():
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self.size = size
        self.stack = []
        self.top = 0

    def push(self, value):
        if self.isFull():
            raise IndexError("stack is full")
        else:
            self.stack.append(value)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        else:
            value = self.stack[self.top - 1]
            self.top -= 1
            self.stack.pop()
            return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.stack[self.top - 1]

    def isFull(self):
        return self.top == self.size

    def isEmpty(self):
        return self.top == 0

    def showStack(self):
        print(self.stack)


if __name__ == '__main__':
    stack = Stack(7)
    stack.push(15)
    stack.push(6)
    stack.push(2)
    stack.push(9)
    stack.showStack()
    last_element = stack.pop()
    print(last_element)
    stack.showStack()
    print(stack.peek())
