class UnionFind:
    def __init__(self, size):
        self.id = [i for i in range(size)]
        self.sz = [1 for i in range(size)]
        self.size = size
        self.num_components = size

    def find(self, index):
        root = index
        while root != self.id[root]:
            root = self.id[root]

        while index != root:
            nex = self.id[index]
            self.id[index] = root
            index = nex

        return root
    
    def component_size(self, index):
        return self.sz[self.find(index)]

    def connected(self, i1, i2):
        return self.find(i1) == self.find(i2)
    
    def unify(self, i1, i2):
        if self.connected(i1, i2):
            return

        root1 = self.find(i1)
        root2 = self.find(i2)

        if self.sz[root1] > self.sz[root2]:
            self.id[root2] = self.id[root1]
            self.sz[root1] += 1
        else:
            self.id[root1] = self.id[root2]
            self.sz[root2] += 1

        self.num_components -= 1
