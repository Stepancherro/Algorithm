# -*- encoding: utf-8 -*-


class TreeNode(object):
    def __init__(self, key=0):
        self.key = key
        self.left = None
        self.right = None


class BSTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def inorder_walk(self, root):
        # 递归,中序遍历
        if root != None:
            self.inorder_walk(root.left)
            print(root.key)
            self.inorder_walk(root.right)

    def iterative_inorder_walk(self):
        # 非递归,中序遍历
        current_node = self.root
        while current_node is not None:
            left = current_node.left
            if left is not None:
                # 如果节点的左孩子不为空,则将该节点的左孩子的最右孩子指向该节点
                # 以便在中序遍历的时候遍历完left的最右孩子后能够跳转到当前节点
                while left.right is not None and left.right != current_node:
                    left = left.right

                # 根据最右节点的右指针是否为空来判断目前是在向下搜索还是向上回溯
                if left.right is None:
                    # 向下搜索的时候,将最右边的节点与下一个回溯点相连
                    left.right = current_node
                    current_node = current_node.left
                    continue
                else:
                    # 向上回溯
                    left.right = None

            # 左节点不存在或左子树已经遍历,则输出当前点
            print(current_node.key)
            current_node = current_node.right

    def search(self, root, key):
        if root is not None and root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)
        else:
            return None

    def iterative_search(self, key):
        # 迭代版本,递归搜索, 迭代版本效率更高
        current = self.root
        while current is not None and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return current

    def iterative_minimum(self):
        # 最小关键字元素,非递归版本
        if self.root is not None:
            current = self.root
            while current.left is not None:
                current = current.left

            return current
        else:
            return None

    def minimum(self, root):
        # 最小关键字元素,递归版本
        if root.left is None:
            return root
        else:
            return self.minimum(root.left)

    def iterative_maximum(self):
        if self.root is not None:
            current = self.root
            while current.right is not None:
                current = current.right

            return current
        else:
            return None

    def maximum(self, root):
        # 最大关键字,递归版本
        if root.right is None:
            return root
        else:
            return self.maximum(root.right)

    def successor(self, x):
        # 寻找节点x的后继
        succ = None
        current = self.root

        while current:
            if x < current.key:
                succ = current
                current = current.left
            else:
                current = current.right

        return succ

    def predecessor(self, x):
        # 寻找节点x的前驱
        pred = None
        current = self.root
        while current:
            if x > current.key:
                pred = current
                current = current.right
            else:
                current = current.left

        return pred

    def insert(self, root, key):
        # 插入,递归版本
        if root is None:
            root = TreeNode(key)
        else:
            if key < root.key:
                root.left = self.insert(root.left, key)
            elif key > root.key:
                root.right = self.insert(root.right, key)

        return root

    def iterative_insert(self, key):
        # 插入,迭代版本
        z = TreeNode(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, root, key):
        if root is None:
            return None

        if root.key == key:
            if root.left:
                # 寻找左子树的最右叶节点
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # 将根节点的右孩子连接为最右叶节点的右孩子
                left_right_most.right = root.right
                # 将左孩子返回作为根节点,删除原来根节点
                return root.left
            else:
                return root.right
        elif root.key > key:
            root.left = self.delete(root.left, key)
        else:
            root.right = self.delete(root.right, key)

        return root


if __name__ == "__main__":
    tree = BSTree()
    for i in range(11):
        tree.root = tree.insert(tree.root, i)
    tree.inorder_walk(tree.root)

    print(tree.search(tree.root, 5).key)
    tree.delete(tree.root, 5)
    tree.inorder_walk(tree.root)
    print(tree.successor(6).key)
    print(tree.predecessor(6).key)
    print(tree.minimum(tree.root).key)
    print(tree.maximum(tree.root).key)
