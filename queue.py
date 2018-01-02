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


class Queue():
    def __init__(self, size=10):
        """
        Initialize python List with size of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        self.size = size
        self.queue = []
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.isFull():
            raise IndexError("queue is full")
        else:
            self.queue.append(value)
            self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        else:
            value = self.queue[self.head - 1]
            self.queue.pop(0)
            self.head += 1
            return value

    def isFull(self):
        return self.tail - self.head + 1 == self.size

    def isEmpty(self):
        return self.head == self.tail

    def showQueue(self):
        print(self.queue)


if __name__ == '__main__':
    q = Queue(6)
    for i in range(5):
        q.enqueue(i)
    q.showQueue()
    q.dequeue()
    q.enqueue(5)
    q.showQueue()
