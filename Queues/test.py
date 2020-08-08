from Queues import *

qu = Queue(100)
qu.enqueue(13)
qu.enqueue(22)
qu.enqueue(10)


while qu.peek() != None:
    print(qu.dequeue())
