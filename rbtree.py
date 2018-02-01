# -*- encoding: utf-8 -*-


class TreeNode(object):
    def __init__(self, key=0):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "black"


class RBTree(object):
    def __init__(self):
        self.nil = TreeNode()
        self.root = self.nil

    def search(self, key):
        x = self.root
        while x is not self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def isEmpty(self):
        return self.root == self.nil

    def inorder_walk(self, x):
        if x is not None:
            self.inorder_walk(x.left)
            if x.key != 0:
                print("key: ", x.key, "parent: ", x.parent.key, "color: ", x.color)
            self.inorder_walk(x.right)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, z):
        # z = TreeNode(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "red"
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def successor(self, x):
        # 返回x节点的后继
        if x.right is not self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y is not self.nil and x is y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left is not self.nil:
            return self.maximum(x.left)
        y = x.parent
        while y is not self.nil and x is y.left:
            x = y
            y = y.parent
        return y

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"


if __name__ == "__main__":
    tree = RBTree()
    tree.insert(TreeNode(41))
    tree.insert(TreeNode(38))
    tree.insert(TreeNode(31))
    tree.insert(TreeNode(12))
    tree.insert(TreeNode(19))
    tree.insert(TreeNode(8))
    tree.inorder_walk(tree.root)
    print("***********delete 8**************")
    tree.delete(tree.root.left.left.left)
    tree.inorder_walk(tree.root)
    print("***********delete 12**************")
    tree.delete(tree.root.left.left)
    tree.inorder_walk(tree.root)
    print("***********delete 19**************")
    tree.delete(tree.root.left)
    tree.inorder_walk(tree.root)
    print("***********delete 31**************")
    tree.delete(tree.root.left)
    tree.inorder_walk(tree.root)
    print("***********delete 38**************")
    tree.delete(tree.root)
    tree.inorder_walk(tree.root)
    print("***********delete 41**************")
    tree.delete(tree.root)
    tree.inorder_walk(tree.root)
