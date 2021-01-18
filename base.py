class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None


class Linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
    def update(self, old_value, new_value):
        pass
    def search(self, value):
        pass
    def delete(self, value):
        pass
    def sort(self):
        pass
    def display(self):
        temp_node = self.head
        data_list = []
        while temp_node.next != None:
            data_list.append(temp_node.value)
            temp_node = temp_node.next
        data_list.append(temp_node.value)
        print(data_list)


class DoublyLinkedlist:
    
    def __init__(self,a,b):
        pass

class CircularLinkedlist:
    
    def __init__(self,a,b):
        pass

class Stack:
    
    def __init__(self,a,b):
        pass

class Queue:
    
    def __init__(self,a,b):
        pass

class Hash:
    
    def __init__(self,a,b):
        pass

class Graph:
    
    def __init__(self,a,b):
        pass