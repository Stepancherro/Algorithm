# -*- encoding: utf-8 -*-

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList2stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current.next != None:
            count += 1
            current = current.next

        return count

    def add(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def push(self, value):
        self.add(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("linkedlist is empty")
        self.head = self.head.next
        self.size -= 1

    def showLinkedList(self):
        current = self.head
        while current.next != None:
            print(current.value)
            current = current.next

if __name__ == "__main__":
    L = SinglyLinkedList()
    for i in range(5):
        L.add(i)
    L.showLinkedList()
    L.push(8)
    L.push(23)
    L.showLinkedList()
    L.pop()
    L.showLinkedList()
