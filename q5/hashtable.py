class hashtable:

    def __init__(self, length):
        self.length = length
        self.table = [ [] for i in range(length)]

    def __repr__(self):
        return str(self.table)

    def hash(self, s):
        return abs(hash(s)) % self.length

    def insert(self, s):
        index = self.hash(s)
        self.table[index].append(s)

    def delete(self, s):
        index = self.hash(s)
        for i in range(len(self.table[index])):
            if self.table[index][i] == s:
                return self.table[index].pop(i)

    def contains(self, s):
        success = False
        index = self.hash(s)
        for i in range(len(self.table[index])):
            if success: break
            else: success = self.table[index][i] == s
        return success
        
