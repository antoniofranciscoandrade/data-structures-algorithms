class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.len = 0
    
    def push(self, val):
        if self.len == 0:
            self.head.val = val
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.len += 1

    def pop(self):
        if self.head.val == None:
            return
        if self.len == 1:
            self.head.val = None
            val = None
        else:
            val = self.head.val
            self.head.next.prev = None
            self.head = self.head.next
        self.len -= 1
        return val
        
    def show(self):
        temp = []
        curr = self.head
        while curr != None:
            temp.append(curr.val)
            curr = curr.next
