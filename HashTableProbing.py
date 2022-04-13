import random
import string


class node:
    key = ""
    value = 0

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def set(self, value):
        self.value = value

    def output(self):
        print("'" + self.key + "' : '" + self.value + "'")


class HashTableProbing:
    # bucket is the container for all nodes
    bucket = []
    # we maintain a set of all keys to check for unique vals.
    # this way, we don't have to handle checking
    # at insert during hash function. Spatial tradeoff for speed & convenience.
    keys = set([])
    # cap size of hashTable. Fixed, set at instantiation
    size = 0
    __loadSum = 0
    # load value
    __loadFactor = 0.0

    # takes in size
    def __init__(self, size):
        self.keys = set([])
        self.size = size
        self.bucket = [None] * size
        self.__loadCalc();
        self.count = 0

    # we recalculate load on every operation
    # this function gets called at set operations and delete operations
    def __loadCalc(self):
        if self.size == 0:
            self.__loadFactor = 0
        else:
            self.__loadFactor = self.__loadSum / self.size

    # returns value associated with key
    def __getitem__(self, k):
        k = str(k);
        if k in self.keys:
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    return self.bucket[hashed].value
            return None
        else:
            return None

    # sets value at given key. returns boolean indicating success or failure
    # we use linear probing for collision resolution
    def __setitem__(self, k, v):
        k = str(k);
        if k in self.keys:
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    self.bucket[hashed].value = v
                    self.count = self.count + 1
                    return True
        elif self.__loadFactor == 1.0:
            return False
        else:
            newNode = node(k, v)
            i = 0;
            hashed = (hash(k) + i) % self.size;
            while self.bucket[hashed] is not None:
                hashed = (hash(k) + i) % self.size
                i += 1
            self.bucket[hashed] = newNode
            self.keys.add(k)
            self.__loadSum += 1
            self.__loadCalc()
            return True

    # deletes value at given key. returns value.
    def __delitem__(self, k):
        k = str(k);
        if k in self.keys:
            i = 0
            hashed = (hash(k) + i) % self.size
            while self.bucket[hashed] is not None:
                if self.bucket[hashed].key != k:
                    hashed = (hash(k) + i) % self.size
                    i += 1
                else:
                    tmp = self.bucket[hashed].value
                    self.bucket[hashed] = None
                    self.keys.remove(k)
                    self.__loadSum -= 1
                    self.__loadCalc()
                    return tmp;
            return None
        else:
            return None

    # returns load
    def load(self):
        return self.__loadFactor


if __name__ == "__main__":
    hashTable = HashTableProbing(100000)
    letters = string.ascii_letters
    keys = []

    for i in range(0, 1000):
        key = ''.join(random.choice(letters) for i in range(10))
        value = i + random.randint(0, 1000000)
        hashTable.__setitem__(key, value)
        keys.append(key)

    for i in keys:
        print("deleting key: " + i)
        hashTable.__delitem__(i)
