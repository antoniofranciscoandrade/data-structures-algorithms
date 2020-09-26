
class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Linkedlist:

    def __init__(self):
        self.head = Node()
        self.len = 0

    def append(self, data):
        current = self.head
        
        while current.next != None:
            current = current.next
        
        current.next = Node(data)
        self.len += 1

    def display(self):
        elements = []
        current = self.head

        while current.next != None:
            current = current.next
            elements.append(current.data)   
    
    def get(self, index):
        if index >= self.len:
            raise Exception('index out of bounds!')
        current = self.head

        for i in range(index+1):
            current = current.next
        
        return current.data
    
    def remove(self, index):
        if index >= self.len:
            raise Exception('index out of bounds!')
        current = self.head
        for i in range(index):
            current = current.next
        current.next = current.next.next

class DoubleLinkedlist:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        if self.len == 0:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head
            self.len += 1
            return
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.len += 1

    def prepend(self, data):
        if self.len == 0:
            self.append(data)
            return
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.lem += 1

    def display(self):
        elements = []
        current = self.head
        for i in range(self.len):
            current = current.next
            elements.append(current.data)   
            
    def get(self, index):
        if index >= self.len:
            raise Exception('index out of bounds!')
        current = self.head

        for i in range(index+1):
            current = current.next
        
        return current.data
    
    def remove(self, index):
        if index >= self.len:
            raise Exception('index out of bounds!')

        current = self.head
        for i in range(index):
            current = current.next

        if index == self.len - 1:
            current.next = self.tail
            self.tail.prev = current
        else:
            current.next.next.prev = current
            current.next = current.next.next
        self.len-=1




