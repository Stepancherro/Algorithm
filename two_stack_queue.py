# -*- encoding: utf-8 -*-


# Queue Abstract Data Type (ADT)
# * Queue() creates a new queue that is empty.
#   It needs no parameters and returns an empty queue.
# * enqueue(item) adds a new item to the rear of the queue.
#   It needs the item and returns nothing.
# * dequeue() removes the front item from the queue.
#   It needs no parameters and returns the item. The queue is modified.
# * isEmpty() tests to see whether the queue is empty.
#   It needs no parameters and returns a boolean value.
# * size() returns the number of items in the queue.
#   It needs no parameters and returns an integer.


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


class Deque(Stack):
    # 此版本的显示队列函数有bug，即执行dequeue之后不能再用显示函数，只有enqueue()和dequeue()操作执行正常
    # 网上的一些参考并不是严格的两个栈实现一个队列，只是用了栈的结构，并没有使用栈的方法
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        super(Deque, self).__init__(size)
        self.stack1 = Stack(size)  # 主栈
        self.stack2 = Stack(size)  # 辅助栈

    def enqueue(self, value):
        if self.isFull():
            raise IndexError("queue is full")
        else:
            self.stack1.push(value)

    def dequeue(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            raise IndexError("queue is empty")
        if self.stack2.isEmpty():
            for i in range(self.stack1.top):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def showQueue(self):
        self.stack1.showStack()


if __name__ == '__main__':
    q = Deque(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.showQueue()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
