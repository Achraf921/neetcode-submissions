class RandomizedSet:

    def __init__(self):
        self.key_val = {}
        self.val_key = {}
        self.last = 0
        #self.transfos = (lambda x: x) # let's try to make it a HOF of our transformations
        # HOF based transformation did NOT work infact
    def insert(self, val: int) -> bool:
        if val in self.val_key: return False
        self.key_val[self.last] = val
        self.val_key[val] = self.last
        self.last+=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_key: return False
        key = self.val_key[val]
        if key == self.last-1: # we just remove without ever swapping
            self.val_key.pop(val)
            self.key_val.pop(key)
        else: # we need to swap and then do the same
            last_val = self.key_val[self.last-1]
            self.key_val[key]= last_val# moving the last to this position
            self.val_key[last_val]=key
            self.key_val[self.last-1]=val
            self.val_key[val]=self.last-1
            self.val_key.pop(val)
            self.key_val.pop(self.last-1) # removing the very last value
        
        self.last-=1
        return True
        

    def getRandom(self) -> int:
        pick = random.randint(0,self.last-1)
        return self.key_val[pick]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()