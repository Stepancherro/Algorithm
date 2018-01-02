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


class TwoStack():
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self.size = size
        self.stack = [None] * size
        self.left_top = 0
        self.right_top = size + 1

    def push(self, value, mode="left"):
        if self.isFull():
            raise IndexError("stack is full")
        else:
            if mode == "left":
                self.left_top += 1
                self.stack[self.left_top - 1] = value

            else:
                self.right_top -= 1
                self.stack[self.right_top - 1] = value

    def pop(self, mode="left"):
        if self.isEmpty(mode):
            raise IndexError("stack is empty")
        else:
            if mode == "left":
                value = self.stack[self.left_top - 1]
                self.stack[self.left_top - 1] = None
                self.left_top -= 1
            else:
                value = self.stack[self.right_top - 1]
                self.stack[self.right_top - 1] = None
                self.right_top += 1

            return value

    def peek(self, mode="left"):
        if self.isEmpty(mode):
            raise IndexError("stack is empty")
        else:
            if mode == "left":
                return self.stack[self.left_top - 1]
            else:
                return self.stack[self.right_top - 1]

    def isFull(self):
        return self.left_top >= self.right_top

    def isEmpty(self, mode):
        if mode == "left":
            return self.left_top == 0
        else:
            return self.right_top == self.size

    def showStack(self):
        print(self.stack)


if __name__ == '__main__':
    stack = TwoStack(5)
    stack.push(5, mode="left")
    stack.push(8, mode="left")
    stack.showStack()
    stack.push(3, mode="right")
    stack.push(9, mode="right")
    stack.push(11, mode="right")
    stack.showStack()
    stack.pop(mode="left")
    stack.pop(mode="right")
    stack.pop(mode="right")
    stack.showStack()
