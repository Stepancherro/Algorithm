# -*- encoding: utf-8 -*-

class SinglyLinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newvalue):
        self.value = newvalue

    def setNext(self, newnext):
        self.next = newnext


class SinglyLinkedList():
    def __init__(self):
        self.head = None  # 初始化链表为空
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        x = self.head
        count = 0
        while x.next != None:
            count += 1
            x = x.next
        return count

    def add(self, value):
        temp = SinglyLinkedListNode(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def append(self, value):
        temp = SinglyLinkedListNode(value)
        if self.isEmpty():
            self.head = temp
            self.size += 1
        else:
            x = self.head
            while x.next != None:
                x = x.next  # 找到最后一个节点
            x.next = temp
            self.size += 1

    def insert(self, index, value):
        if index <= 1:
            self.add(value)
        elif index > self.size:
            self.append(value)
        else:
            temp = SinglyLinkedListNode(value)
            count = 0
            prev = None
            x = self.head
            while x != None and count < index:
                count += 1
                prev = x
                x = x.next
            prev.next = temp
            temp.next = x

    def delete(self, value):
        if self.isEmpty():
            raise IndexError("linkedlist is empty")
        x = self.head
        prev = None
        while x != None:
            if x.getValue() == value:
                if not prev:
                    self.head = x.next
                else:
                    prev.next = x.next
                break
            else:
                prev = x
                x = x.next

    def search(self, value):
        x = self.head
        found = False
        while x.next != None and not found:
            if x.getValue() == value:
                found = True
            else:
                x = x.next
        return found

    def index(self, value):
        x = self.head
        count = 0
        found = None
        while x.next != None and not found:
            count += 1
            if x.getValue() == value:
                found = True
            else:
                x = x.next
        if found:
            return count
        else:
            raise IndexError("The value is not in linkedlist")

    def showLinkedList(self):
        x = self.head
        while x.next != None:
            print(x.getValue())
            x = x.next


if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(5):
        l.append(i)
    print(l.size)
    l.showLinkedList()
    print(l.search(3))
    print(l.search(8))
    print(l.index(2))
    l.add(8)
    l.append(11)
    l.insert(3, 15)
    l.showLinkedList()
    l.delete(15)
    l.showLinkedList()
