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


class Deque():
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

    def enqueue(self, value, mode="left"):
        if self.isFull():
            raise IndexError("queue is full")
        else:
            if mode == "left":
                if self.head == 0:
                    self.head = self.size - 1
                    self.queue.insert(self.head, value)
                else:
                    self.head -= 1
                    self.queue.insert(self.head, value)
            else:
                if self.tail == self.size - 1:
                    self.queue.insert(self.tail, value)
                    self.tail = 0
                else:
                    self.queue.insert(self.tail, value)
                    self.tail += 1

    def dequeue(self, mode="left"):
        if self.isEmpty():
            raise IndexError("stack is empty")
        else:
            if mode == "left":
                if self.head == self.size - 1:
                    value = self.queue[self.head]
                    self.queue.pop(self.head)
                    self.head = 0
                else:
                    value = self.queue[self.head]
                    self.queue.pop(self.head)
                    self.head += 1
            else:
                if self.tail == 0:
                    value = self.queue[self.size - 1]
                    self.queue.pop(self.size - 1)
                    self.tail = self.size - 1
                else:
                    value = self.queue[self.tail - 1]
                    self.queue.pop(self.tail - 1)
                    self.tail -= 1
            return value

    def isFull(self):
        return self.head == self.tail + 1

    def isEmpty(self):
        return (self.head == self.tail) or (self.tail - self.head + 1 == self.size)

    def showQueue(self):
        print(self.queue)


if __name__ == '__main__':
    q = Deque(5)
    q.enqueue(1, mode="right")
    q.enqueue(2, mode="right")
    q.enqueue(3, mode="left")
    q.enqueue(4, mode="left")
    q.showQueue()
    q.dequeue(mode="left")
    q.dequeue(mode="right")
    q.showQueue()
