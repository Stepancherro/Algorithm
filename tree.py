# -*- encoding: utf-8 -*-

class TreeNode():
    def __init__(self, key):
        self.left_child = None
        self.right_sibling = None
        self.key = key

    def getKey(self):
        return self.key

    def getLeft(self):
        return self.left_child

    def getRight(self):
        return self.right_sibling


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = TreeNode(value)
        current = self.root

        if self.root is None:
            self.root = temp
            return True
        while True:
            if current.key == value:
                raise ValueError("The value is exit")
            elif current.key >= value:
                if current.left_child is not None:
                    current = current.left_child
                else:
                    current.left_child = temp
                    return True
            else:
                if current.right_sibling is not None:
                    current = current.right_sibling
                else:
                    current.right_sibling = temp
                    return True

    def showTree(self, node):
        # 递归方法显示
        if node is not None:
            self.showTree(node.left_child)
            print(node.key)
            self.showTree(node.right_sibling)

    def getRoot(self):
        return self.root


if __name__ == '__main__':
    a = [3, 2, 11, 6, 9, 12, 15, 1, 10, 7]
    tree = Tree()
    for i in a:
        tree.insert(i)
    tree.showTree(tree.getRoot())
