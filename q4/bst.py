class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __repr__(self):
        return str(self.data)

class BST:

    def __init__(self, r_data):
        self.root = Node(r_data)


    def insert_node(self, node, x):
        if not node or node.data == x:
            return

        if node.data > x:
            if node.lchild:
                self.insert_node(node.lchild, x)
            else:
                node.lchild = Node(x)
        elif node.data < x:
            if node.rchild:
                self.insert_node(node.rchild, x)
            else:
                node.rchild = Node(x)


    def remove_node(self, x):
        parent = self.find_parent(None, self.root, x)
        node = self.find_node(self.root, x)

        if not node.lchild and not node.rchild:
            self.__replace_child(parent, node, None)

        elif not node.lchild and node.rchild:
            self.__replace_child(parent, node, node.rchild)

        elif node.lchild and not node.rchild:
            self.__replace_child(parent, node, node.lchild)

        elif node.lchild and node.rchild:
            lsub_max = self.find_max(node.lchild)
            self.remove_node(lsub_max.data)
            lsub_max.rchild = node.rchild
            lsub_max.lchild = node.lchild
            self.__replace_child(parent, node, lsub_max)

    def __replace_child(self, parent, orig, new):
        if parent:
            if parent.lchild == orig:
                parent.lchild = new
            elif parent.rchild == orig:
                parent.rchild = new
        else:
            self.root = new


    def find_node(self, node, x):
        if node.data == x:
            return node
        elif node.data > x:
            return self.find_node(node.lchild, x)
        elif node.data < x:
            return self.find_node(node.rchild, x)


    def find_parent(self, parent, node, x):
        if node.data == x:
            return parent
        elif node.data > x:
            return self.find_parent(node, node.lchild, x)
        elif node.data < x:
            return self.find_parent(node, node.rchild, x)


    def find_max(self, node):
        if node:
            cur = node
            if not cur.rchild and cur.lchild:
                cur = cur.lchild
            while cur.rchild:
                cur = cur.rchild
            return cur


    def inorder_traversal(self, node):
        if node.lchild:
            self.inorder_traversal(node.lchild)
        print node.data
        if node.rchild:
            self.inorder_traversal(node.rchild)


    def bfs_print(self):
        parents = [self.root]
        children = []

        while parents:
            for p in parents:
                if p.lchild:
                    children.append(p.lchild)
                if p.rchild:
                    children.append(p.rchild)

            print parents
            parents = children
            children = []


def bfs(t, x):
    if t.root:
        parents = [t.root]
        children = []

        while parents:
            for node in parents:
                if node.data == x:
                    return node
                if node.lchild:
                    children.append(node.lchild)
                if node.rchild:
                    children.append(node.rchild)

                parents = children
                children = []

def dfs(node, x):
    if node:
        if node.data == x:
            return node

        child = dfs(node.lchild, x)
        if child and child.data == x:
            return child

        child = dfs(node.rchild, x)
        if child and child.data == x:
            return child


tree = BST(40)
tree.insert_node(tree.root, 19)
tree.insert_node(tree.root, 67)
tree.insert_node(tree.root, 13)
tree.insert_node(tree.root, 25)
tree.insert_node(tree.root, 100)
tree.insert_node(tree.root, 80)

tree.bfs_print()
