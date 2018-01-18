# -*- encoding: utf-8 -*-

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList2Quene():
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

    def append(self, value):
        temp = Node(value)
        if self.isEmpty():
            self.head = temp
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
            self.size += 1

    def enquene(self, value):
        self.append(value)

    def dequene(self):
        if self.isEmpty():
            raise IndexError("linkedlist is empty")
        self.head = self.head.next
        self.size -= 1

    def showLinkedList(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    L = SinglyLinkedList2Quene()
    for i in range(5):
        L.add(i)
    L.showLinkedList()
    L.enquene(8)
    L.enquene(23)
    L.showLinkedList()
    L.dequene()
    L.showLinkedList()
