from Nodes import *

class Queue:
    def __init__(self, limit = 10000):
        self.limit = limit
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self,value):
        to_insert = Node(value)
        if self.size == self.limit:
            print("Queue Overflow!")
        else:
            if self.head == None:
                self.head = to_insert
                self.tail = to_insert
                self.size += 1
            else:
                self.tail.next_node = to_insert
                self.tail = to_insert
                self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow!")
        else:
            to_return = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return to_return

    def peek(self):
        if self.size == 0:
            print("Queue Underflow!")
        else:
            return self.head.value
