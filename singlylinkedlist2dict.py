# -*- encoding: utf-8 -*-

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList2Dict():
    def __init__(self):
        self.nil = Node(0)
        self.nil.next = self.nil
        self.size = 0

    def insert(self, value):
        temp = Node(value)
        temp.next = self.nil.next
        self.nil.next = temp
        self.size += 1

    def search(self, value):
        current = self.nil.next
        self.nil.value = value  # 为了省略判断条件current != self.nil
        while current.value != value:
            current = current.next
        if current == self.nil:
            return None
        else:
            return current

    def delete(self, value):
        current = self.nil
        while current.next != self.nil:
            if current.next.value == value:
                to_be_deleted = current.next
                current.next = current.next.next
                del to_be_deleted
                self.size -= 1
            else:
                current = current.next

    def showLinkedList(self):
        current = self.nil.next
        while current != self.nil:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    L = SinglyLinkedList2Dict()
    for i in range(5):
        L.insert(i)
    L.showLinkedList()
    L.delete(3)
    L.showLinkedList()
    x = L.search(2)
    print(x.value)
