from LinkedLists import *

class HashTable:
    def __init__(self, size = 1000):
        self.size = size
        self.array = [LinkedList() for item in range(size)]

    def hash(self, key):
        sum = 0
        to_hash = str(key)
        for elem in to_hash:
            sum += ord(elem)
        return sum % self.size

    def insert(self, key, value):
        position = self.hash(key)
        self.array[position].insert_beginning([key, value])

    def retrieve(self, key):
        position = self.hash(key)
        searching_key = self.array[position].get_head_node()
        if searching_key.get_value()[0] == key:
            return searching_key.get_value()[1]
        while key != searching_key or searching_key == None:
            searching_key = searching_key.get_next_node()
            if searching_key.get_value()[0] == key:
                return searching_key.get_value()[1]
