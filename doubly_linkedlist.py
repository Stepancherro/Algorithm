# -*- encoding: utf-8 -*-

class DoublyLinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        x = self.head
        count = 0
        while x != None:
            count += 1
            x = x.next
        return count

    def showLinkedList(self):
        x = self.head
        while x != None:
            print(x.value)
            x = x.next

    def add(self, value):
        """头部插入元素"""
        node = DoublyLinkedListNode(value)
        if self.isEmpty():
            # 如果链表为空，直接插入
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, value):
        """在末尾插入元素"""
        node = DoublyLinkedListNode(value)
        if self.isEmpty():
            # 如果链表为空，直接调用add()
            self.add(value)
        else:
            # 如果链表不为空，首先寻找到链表最后一个节点
            x = self.head
            while x.next != None:
                x = x.next
            # 此时x为最后一个节点
            x.next = node
            node.prev = x

    def search(self, value):
        # 寻找元素是否存在，如果存在并返回位置
        if self.isEmpty():
            raise IndexError("linkedlist is empty")
        x = self.head
        found = False
        while x.next != None and not found:
            if x.value == value:
                found = True
            else:
                x = x.next
        return found

    def insert(self, index, value):
        """在指定位置添加元素"""
        if index <= 0:
            self.add(value)
        if index > (self.size() - 1):
            self.append(value)
        else:
            # 寻找到要插入的位置
            node = DoublyLinkedListNode(value)
            x = self.head
            count = 0
            while count < index - 1:
                count += 1
                x = x.next
            node.next = x.next
            node.prev = x
            x.next.prev = node
            x.next = node

    def delete(self, value):
        """删除指定元素"""
        if self.isEmpty():
            raise IndexError("linkedlist is empty")
        else:
            x = self.head
            if x.value == value:
                # 如果第一个元素即使要删除的元素
                if x.next == None:
                    # 如果链表只有一个元素
                    self.head = None
                else:
                    x.next.prev = None
                    self.head = x.next
                return
            while x != None:
                if x.value == value:
                    x.prev.next = x.next
                    x.next.prev = x.prev
                    break
                else:
                    x = x.next


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.add(1)
    l.append(2)
    l.append(3)
    l.showLinkedList()
    l.insert(2, 4)
    l.insert(1, 5)
    l.showLinkedList()
    l.delete(4)
    l.showLinkedList()
    print(l.search(2))
    print(l.search(8))
