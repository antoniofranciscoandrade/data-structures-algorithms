class Node:
    def __init__(self, left=None, right=None, val=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def dig_left(self, curr):
        while curr.left:
            curr = curr.left
        return curr
    
    def dig_right(self, curr):
        while curr.right:
            curr = curr.right 
        return curr

    def add(self, val):
        if not val:
            return None
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            self.private_insert(self.root, newNode)
        self.size += 1

    def private_insert(self, node, newNode):
        if not node:
            return newNode
        if newNode.val < node.val:
            node.left = self.private_insert(node.left, newNode)
        else:
            node.right = self.private_insert(node.right, newNode)
        return node

    def remove(self, val):
        if not val:
            return
        self.root = self.private_remove(self.root, val)
        self.size -= 1

    def private_remove(self, node, val):
        if not node:
            return
        if val < node.val:
            node.left = self.private_remove(node.left, val)
        elif val > node.val:
            node.right = self.private_remove(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                to_swap = self.dig_left(node.right)
                node.val = to_swap.val
                node.right = self.private_remove(node.right, to_swap.val)
        return node

