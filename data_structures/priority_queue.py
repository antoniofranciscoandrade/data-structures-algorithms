class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def get_child(self, index):
        left = 2*index + 1
        right = left + 1 if left + 1 < len(self.heap) else None
        return left, right
    
    def get_parent(self, index):
        return int((index-1)/2)

    def switch(self, fro, to):
        temp = self.heap[to]
        self.heap[to] = self.heap[fro]
        self.heap[fro] = temp

    def insert(self, val):
        self.heap.append(val)
        pos = len(self.heap) - 1

        while pos > 0:
            parent = self.get_parent(pos)
            if self.heap[parent] <= self.heap[pos]:
                break
            else:
                self.switch(pos, parent)
            pos = parent

    def pop(self):
        out = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        pos = 0
      
        while pos < (len(self.heap)-1)/2:
            left, right = self.get_child(pos)
            if right == None:
                if self.heap[left] < self.heap[pos]:
                    self.switch(pos, left)
                    pos = left
                else:
                    break
            else:
                to_switch = left if self.heap[left] < self.heap[right] else right
                if self.heap[to_switch] < self.heap[pos]:
                    self.switch(pos, to_switch)
                    pos = to_switch 
                else:
                    break
        return out
