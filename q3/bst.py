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
        pass

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




tree = BST(40)
tree.insert_node(tree.root, 19)
tree.insert_node(tree.root, 67)
tree.insert_node(tree.root, 13)
tree.insert_node(tree.root, 25)
tree.insert_node(tree.root, 100)
tree.insert_node(tree.root, 80)

tree.bfs_print()

node = tree.find_node(tree.root, 100)
print "find node 100? " + str(node.data)

parent = tree.find_parent(None, tree.root, 25)
print "find parent of 25? " + str(parent.data)
