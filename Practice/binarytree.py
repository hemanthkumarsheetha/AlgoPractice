class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right= None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self):
        self.preorder_print(self.root)

    def preorder_print(self,node):
        if node is None:
            return
        print(node.value)
        self.preorder_print(node.left)
        self.preorder_print(node.right)

    def search(self,key):
        return self.preorder_search(self.root,key)

    def preorder_search(self,node,key):
        if node is None:
            return(False)

        if node.value == key:
            return(True)

        return self.preorder_search(node.left,key) or self.preorder_search(node.right,key)

b = BinaryTree(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.root.left.right = Node(5)

b.print_tree()

p = b.search(4)
print(p)
p= b.search(100)
print(p)