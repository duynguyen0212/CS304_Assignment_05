from BTS_map import BSTMap
from HashTableChaining import HashTableChaining
from HashTableProbing import HashTableProbing
from SkipList import SkipList
import time
import numpy as np
import random
import string
import matplotlib.pyplot as plt

"""
BST: Binary search tree
HT1: hash table (separate chaining)
HT2: hash table (linear probing)
SL: Skip list

Comment: 
"""
BST = BSTMap()
HT1 = HashTableChaining()
HT2 = HashTableProbing(10000)
SL = SkipList(1000, 0.5)

letters = string.ascii_letters

t1 = []
t2 = []
t3 = []
t4 = []
n = 10000


# Insertion plot
def plot1():

    for i in range(0, n):
        start_t = time.time()
        key = random.randint(1, 1000000000) + i
        value = ''.join(random.choice(letters) for _ in range(3))
        BST.__setitem__(key, value)
        t1.append(time.time() - start_t)

    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        HT1.__setitem__(key, value)
        t2.append(time.time() - start_t)
    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        HT2.__setitem__(key, value)
        t3.append(time.time() - start_t)
    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        SL.__setitem__(key, value)
        t4.append(time.time() - start_t)

    plt.title("1) Comparing map performance: Insertion")
    plt.plot(t1, label="BST", color="red")
    plt.plot(t2, label="Hash table (chaining)", color="blue")
    plt.plot(t3, label="Hash table (probing)", color="green")
    plt.plot(t4, label="Skip list", color="magenta")
    plt.legend(loc="upper left")
    plt.xlabel("Number of elements")
    plt.ylabel("Times in ms")
    plt.show()

# Return plot
def plot2():
    for i in range(0, n):
        start_t = time.time()
        key = random.randint(1, 1000000000) + i
        value = ''.join(random.choice(letters) for _ in range(3))
        BST.__setitem__(key, value)
        BST.__getitem__(key)
        t1.append(time.time() - start_t)

    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        HT1.__setitem__(key, value)
        HT1.__getitem__(key)
        t2.append(time.time() - start_t)
    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        HT2.__setitem__(key, value)
        HT2.__getitem__(key)
        t3.append(time.time() - start_t)
    for i in range(0, n):
        start_t = time.time()
        key = ''.join(random.choice(letters) for _ in range(2))
        value = ''.join(random.choice(letters) for _ in range(3))
        SL.__setitem__(key, value)
        SL.__getitem__(key)
        t4.append(time.time() - start_t)

    plt.title("2) Comparing map performance: Insert and return")
    plt.plot(t1, label="BST", color="red")
    plt.plot(t2, label="Hash table (chaining)", color="blue")
    plt.plot(t3, label="Hash table (probing)", color="green")
    plt.plot(t4, label="Skip list", color="magenta")
    plt.legend(loc="upper left")
    plt.xlabel("Number of elements")
    plt.ylabel("Times in ms")
    plt.show()

def plot3():

    keys1 = []
    keys2 = []
    keys3 = []
    keys4 = []
    # Add key-value to maps
    for i in range(0, n):
        k1 = random.randint(1, 1000000000) + i
        v1 = ''.join(random.choice(letters) for _ in range(3))
        BST.__setitem__(k1, v1)
        keys1.append(k1)

    for i in range(0, n):
        k2 = ''.join(random.choice(letters) for _ in range(2))
        v2 = ''.join(random.choice(letters) for _ in range(3))
        HT1.__setitem__(k2, v2)
        keys2.append(k2)

    for i in range(0, n):
        k3 = ''.join(random.choice(letters) for _ in range(2))
        v3 = ''.join(random.choice(letters) for _ in range(3))
        HT2.__setitem__(k3, v3)
        keys3.append(k3)

    for i in range(0, n):
        k4 = ''.join(random.choice(letters) for _ in range(2))
        v4 = ''.join(random.choice(letters) for _ in range(3))
        SL.__setitem__(k4, v4)
        keys4.append(k4)

    # Time for plot
    for item in keys1:
        start_t = time.time()
        BST.__delitem__(item)
        t1.append(time.time() - start_t)

    for item in keys2:
        start_t = time.time()
        HT1.__delitem__(item)
        t2.append(time.time() - start_t)

    for item in keys3:
        start_t = time.time()
        HT2.__delitem__(item)
        t3.append(time.time() - start_t)

    for item in keys4:
        start_t = time.time()
        SL.__delitem__(item)
        t4.append(time.time() - start_t)


    plt.title("3) Comparing map performance: Delete keys")
    plt.plot(t1, label="BST", color="red")
    plt.plot(t2, label="Hash table (chaining)", color="blue")
    plt.plot(t3, label="Hash table (probing)", color="green")
    plt.plot(t4, label="Skip list", color="magenta")
    plt.legend(loc="upper left")
    plt.xlabel("Number of elements")
    plt.ylabel("Times in ms")
    plt.show()


if __name__ == "__main__":
   plot1()
   #plot2()
   #plot3()
