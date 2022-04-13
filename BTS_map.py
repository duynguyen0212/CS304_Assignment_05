"""
Binary Search Tree based implementation of the Map ADT.
"""
import random
import string


class _BSTNode(object):
    """ Private storage class for the BSTMap. """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + ": " + str(self.value)


class BSTMap(object):
    """ 
    A binary search tree implementation of the Map ADT.  This class
    implements a subset of the functionality provided by the built-in
    Python dictionary class.
    """

    def __init__(self):
        """ Construct an empty map. """
        self._root = None
        self._size = 0

    def __len__(self):
        """ Return the number of values stored in the map """
        return self._size

    def __contains__(self, key):
        """ Return true if key is in the map, False otherwise """
        return not self._findNode(self._root, key) is None

    def __getitem__(self, key):
        """ 
        Return the value associated with key. Raises a KeyError
        if key is not in the map. 
        """
        node = self._findNode(self._root, key)
        if node is None:
            raise KeyError("There's no key in the map")
        return node.value

    def __setitem__(self, key, value):
        """ Implements self[key] = value.  If key is already stored in
        the map then its value is modified.  If key is not in the map,
        it is added."""

        if self._root is None:
            self._root = _BSTNode(key, value)
            self._size += 1
        else:
            self._setItem(self._root, key, value)

    def __delitem__(self, key):
        """
        Remove the item with key equal to k. Raise KeyError if there's no such item
        """
        if self._root is None:
            raise KeyError("There's no key in the map")

        self._root = self._remove(self._root, key)
        self._size -= 1

    def _findNode(self, subtree, key):
        # Recursive helper method for __getitem__ and __contains__. 
        # Returns the _BSTNode that contains key, or None if key is not
        # in the map. 
        if subtree is None:
            return None
        elif subtree.key == key:
            return subtree
        elif subtree.key < key:
            return self._findNode(subtree.right, key)
        else:
            return self._findNode(subtree.left, key)

    def _setItem(self, subtree, key, value):
        # Internal helper method for __setitem__.

        assert subtree is not None

        # The key has been found: 
        if subtree.key == key:
            subtree.value = value

        # The key belongs on the left: 
        elif key < subtree.key:
            if subtree.left is None:
                subtree.left = _BSTNode(key, value)
                self._size += 1
            else:
                self._setItem(subtree.left, key, value)

        # The key belongs on the right:
        else:
            if subtree.right is None:
                subtree.right = _BSTNode(key, value)
                self._size += 1
            else:
                self._setItem(subtree.right, key, value)



    def _height(self, subtree):
        # Recursively calculate the height of the subtree. 
        # (Needed for the tree drawing method.)
        if subtree is None:
            return 0
        else:
            return 1 + max(self._height(subtree.left),
                           self._height(subtree.right))

    def _remove(self, subtree, key):
        # Recursively remove the node containing key from this subtree.
        # 
        # This method works by returning a modified version of the current
        # subtree that does not contain the indicated key. 
        #
        # Precondition: key is in the subtree. 
        # Returns: A _BSTNode, or None if this is a leaf that is being removed.

        assert subtree is not None, "Cannot remove non-existent key."

        # Key is in the left subtree: 
        if key < subtree.key:
            subtree.left = self._remove(subtree.left, key)
            return subtree

        # Key is in the right subtree: 
        elif key > subtree.key:
            subtree.right = self._remove(subtree.right, key)
            return subtree

        # The key has been located at the current node: 
        else:
            # This is a leaf node: 
            if subtree.left is None and subtree.right is None:
                return None

            # Only a left child:
            elif subtree.left is not None and subtree.right is None:
                return subtree.left

            # Only a right child:
            elif subtree.left is None and subtree.right is not None:
                return subtree.right

            # Two children:
            else:
                successor = self._minimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._remove(subtree.right, successor.key)
                return subtree

    def _minimum(self, subtree):
        # Return the minimum node in this subtree by recursively following
        # left children. 
        if subtree is None:
            return None
        if subtree.left is None:
            return subtree
        else:
            return self._minimum(subtree.left)


"""
testing
"""
if __name__ == "__main__":
    BST  = BSTMap()
    keys = []
    for i in range(0, 10000):
        k = random.randint(1, 100000000) + i
        letters = string.ascii_letters
        v = ''.join(random.choice(letters) for i in range(3))
        BST.__setitem__(k, v)
        keys.append(k)

    for item in keys:
        BST.__delitem__(item)


    print(BST.__len__())

