class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def add(self, val):

        newNode = Node(val)
        if self.len == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.len += 1
    
    def remove(self):
        val = self.head
        self.head = self.head.next
        if self.len == 1:
            self.tail = self.tail.next
        
        self.len -= 1

        return val

    def show(self):
        temp = []
        curr = self.head
        while curr != None:
            temp.append(curr.val)
            curr = curr.next

