from base import Queue, Stack

mystack = Stack()
myqueue = Queue()

mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')

mystack.display()
mystack.pop()
mystack.display()

myqueue.enqueue('A')
myqueue.enqueue('B')
myqueue.enqueue('C')
myqueue.enqueue('D')

myqueue.display()
myqueue.dequeue()
myqueue.display()