# linear probing
# this searches the empty space instead of making the linked list

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]


    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_solt(key, h)
            self.arr[new_h] = (key, value)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
        # return [*range(len(self.arr))] leads the following error
        #[('march 6', 10), ('march 17', 200), None, None, None, None, None, None, None, ('march 6', 20)]

    def find_solt(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key: # for already existed key,
                                                # so we have to replace this value with the new vlaue
                return prob_index
        raise Exception("Hashmap Full")

    def __delitem__(self, key): 
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found
            if self.arr[prob_index][0] == key:
                del self.arr[prob_index]

t = HashTable()
t["march 6"] = 20
t["march 6"] = 10
t["march 17"] = 88
t["march 17"] = 29
t["march 17"] = 200
print("t.arr = ", t.arr, "\n")
print('t["march 17"] = ', t["march 17"], "\n")
print('t["march 21"] = ', t["march 21"])
del t["march 17"]
print("\n t.arr = ", t.arr)

"""
output

t.arr =  [('march 17', 200), None, None, None, None, None, None, None, None, ('march 6', 10)] 

t["march 17"] =  200 

t["march 21"] =  None

t.arr =  [None, None, None, None, None, None, None, None, ('march 6', 10)]
"""



