import random

class Node(object):

    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        # list to hold references to node of different level 
        self.forward = [None] * (level + 1)


class SkipList(object):

    def __init__(self, max_lvl, P):
        # Maximum level for this skip list
        self.MAXLVL = max_lvl

        # P is the fraction of the nodes with level 
        # i references also having level i+1 references
        self.P = P

        # create header node and initialize key to -1
        self.header = self.createNode(self.MAXLVL, None, -1)

        # current level of skip list
        self.level = 0

    # create  new node
    def createNode(self, lvl, value, key):
        n = Node(key, value, lvl)
        return n

    # create random level for node
    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and \
                lvl < self.MAXLVL: lvl += 1
        return lvl

    # insert given key in skip list
    def __setitem__(self, key, value):
        # create update array and initialize it
        update = [None] * (self.MAXLVL + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current == None or current.key != key:
            # Generate a random level for node
            rlevel = self.randomLevel()

            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            # create new node with random level generated
            n = self.createNode(rlevel, value, key)

            # insert node by rearranging references 
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            #print("Successfully inserted key {}".format(key))

    def __delitem__(self, search_key):

        # create update array and initialize it
        update = [None] * (self.MAXLVL + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < search_key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # If current node is target node
        if current is not None and current.key == search_key:

            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Remove levels having no elements
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            #print("Successfully deleted key {}".format(search_key))

    def __getitem__(self, key):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        # reached level 0 and advance reference to 
        # right, which is our desired node
        current = current.forward[0]

        # If current node have key equal to
        # search key, we have found our target node
        if current and current.key == key:
            return current.value
        else:
            raise KeyError("Couldn't find key value")