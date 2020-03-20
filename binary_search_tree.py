class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        new = Node(val)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if val < node.key:
                    # go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, val):
        node = self.root
        while node is not None:
            if val == node.key:
                return node
            elif val < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete_min(self):
        if self.root is None:
            return None, None
        else:
            # go left until leaf node is reached
            node = self.root
            while node.left is not None:
                node = node.left
            # remove the node and promote its right subtree
            if node.parent is not None:
                node.parent.left = node.right
            else:
                # root is min
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.left = None
            node.right = None
            node.parent = None
            return node, parent

    def delete_max(self):
        if self.root is None:
            return None, None
        else:
            # go right until leaf node is reached
            node = self.root
            while node.right is not None:
                node = node.right
            # remove node and promote its left subtree
            if node.parent is not None:
                node.parent.right = node.left
            else:
                # root is max
                self.root = node.left
            if node.left is not None:
                node.left.parent = node.parent
            parent = node.parent
            node.left = None
            node.right = None
            node.parent = None
            return node, parent

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print (node.key, end = " ")
            self.inorder(node.right)


class Node(object):
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
        self.parent = None
    

if __name__ == '__main__':
    items = [30, 40, 20, 70, 10, 80, 60, 90, 5, 50]
    tree = BST()
    for item in items:
        tree.insert(item)
    
    tree.inorder(tree.root)
    print()

    max_node, max_parent = tree.delete_max()
    print (max_node.key, max_parent.key)

    min_node, min_parent = tree.delete_min()
    print (min_node.key, min_parent.key)