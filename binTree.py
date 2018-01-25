# -*- encoding: utf-8 -*-

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

    def gettop(self):
        if self.isEmpty():
            raise IndexError("stack is full")
        else:
            value = self.stack[self.top - 1]
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


class TreeNode():
    def __init__(self, key=0):
        self.left = None
        self.right = None
        self.key = key

    def getKey(self):
        return self.key

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


class Bintree():
    def __init__(self):
        self.root = None

    def makeEmpty(self):
        if self.root.left and self.root.right:
            self.root = None
        if self.root.left is not None:
            self.root.left.makeEmpty()
        if self.root.right is not None:
            self.root.right.makeEmpty()

    def insert(self, value):
        temp = TreeNode(value)
        current = self.root

        if self.root is None:
            self.root = temp
            return True
        while True:
            if current.key == value:
                raise ValueError("The value is exit!")
            elif current.key >= value:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = temp
                    return True
            else:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = temp
                    return True

    def find(self, value):
        while (self.root is not None):
            if self.root.key == value:
                return self.root
            elif self.root.key > value:
                self.root = self.root.left
            else:
                self.root = self.root.right

        return None

    def getParent(self, node):
        if node.key == self.root.key:
            raise IndexError("Root node doesn't have parent!")
        current = self.root
        parent = p
        while (current != node):
            if current.key == node.key:
                break
            elif current.key > node.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        return parent

    def showTree(self, node):
        # 递归方法显示
        if node is not None:
            # print(node.key)
            self.showTree(node.left)
            print(node.key)
            self.showTree(node.right)

    def nonReShowTree(self, node):
        # 非递归方法遍历显示
        p = node
        s = Stack()
        s.push(p)
        flag = 0
        while (not s.isEmpty()):
            p = s.gettop()
            # flag标志位。如果flag为0则沿着树向下遍历，如果flag为1则沿着树向上遍历
            if flag == 0:
                if p.left is None:
                    print(p.key)
                    s.pop()
                    if p.right is None:
                        if s.isEmpty():
                            break
                        p = s.gettop()
                        print(p.key)
                        s.pop()
                        flag = 1
                    else:
                        s.push(p.right)
                        p = s.gettop()
                        flag = 0
                else:
                    s.push(p.left)
                    flag = 0

            if flag == 1:
                if p.right is None:
                    if s.isEmpty():
                        break
                    flag = 1
                    p = s.gettop()
                    print(p.key)
                    s.pop()
                s.push(p.right)
                flag = 0

    def getRoot(self):
        return self.root

    def getLeft(self):
        if self.root.left is not None:
            return self.root.left
        return None

    def getRight(self):
        if self.root.right is not None:
            return self.root.right
        return None


a = [5, 11, 32, 6, 9, 12, 15, 1, 10, 7]
tree = Bintree()
for i in a:
    tree.insert(i)
# tree.showTree(tree.getRoot())
tree.nonReShowTree(tree.getRoot())
