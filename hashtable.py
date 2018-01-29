# -*- encoding: utf-8 -*-

class HashNode(object):
    # 散列表(哈希表)节点
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable(object):
    def __init__(self, size=11):
        self.size = size
        self._table = [None] * size  # 用于存储节点
        self._len = 0  # 哈希表中节点的数量

    def __len__(self):
        return self._len

    def _hash(self, key):  # _hash()散列函数,给出关键字k,计算其散列位置,即h(k)
        return abs(hash(key)) % self.size  # hash()用于获取一个对象(字符串或者数值等)的哈希值

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def search(self, key):
        # 给出关键字,查找节点
        j = self._hash(key)  # 计算出关键字k散列到表中的位置j
        node = self._table[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            raise KeyError("KeyError" + repr(key))  # repr()函数将对象转化为供解释器读取的形式

        return node

    def insert(self, key):
        # 插入节点
        initial_hash = j = self._hash(key)  # 计算出关键字k散列到表中的位置j

        while True:
            node = self._table[j]
            if node is None:
                # 可以插入该元素
                self._table[j] = HashNode(key)
                self._len += 1
                return
            elif node.key == key:
                # 元素已存在
                return

            j = self._rehash(j)  # 更新散列位置
            if initial_hash == j:
                # 散列表已满
                raise ValueError("Table is full")

    def delete(self, key):
        j = self._hash(key)
        node = self._table[j]
        if node is not None:
            if node.key == key:
                self._table[j] = node.next
                self._len -= 1
            else:
                while node.next != None:
                    temp = node
                    node = node.next
                    if node.key == key:
                        temp.next = node.next
                        self._len -= 1
                        break


if __name__ == "__main__":
    table = HashTable()
    for i in range(5):
        table.insert(i)

    print(table.size, table._len)
    node = table.search(3)
    print(node.key)

    table.delete(3)
    print(table.size, table._len)
