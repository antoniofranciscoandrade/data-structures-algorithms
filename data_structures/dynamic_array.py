import ctypes

class dynamic_array(object):

    def __init__(self):
        
        self.len = 0
        self.capacity = 16
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        return self.len
    
    def __getitem__(self, i):
        
        if not 0 <= i < self.len:
            raise IndexError('Index out of bounds!')

        return self.arr[i]

    def append(self, item):
        self.len += 1
        self.arr[self.len-1] = item
        
        
    def insertAt(self, item, i):
        if not 0 <= i < self.len:
            raise IndexError('Index out of bounds!')

        if self.len == self.capacity:
            self._resize(self.capacity*2)

        for k in range(self.len-1, i-1, -1):
            self.arr[k+1] = self.arr[k]

        self.arr[i] = item

    def delete(self, item):
        for k in range(self.len):
            if self.arr[k] == item:
                self.removeAt(k)
                return

    def removeAt(self, i):
        for k in range(i, self.len):
            self.arr[i] = self.arr[i+1]

        self.arr[self.len-1] = None
        self.len -= 1

    def _resize(self, new_cap):
        new_arr = self.make_array(new_cap)
        for i in range(self.len):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_cap

    def make_array(self, capacity):
        return (capacity*ctypes.py_object)() 
        


    

    