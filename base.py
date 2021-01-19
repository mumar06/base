from multipledispatch import dispatch

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
#   O(1)
    def insert(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
#   O(1)
    def push(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
#   O(n)
    def update(self, old_value, new_value):
        if self.head.value == old_value:
            self.head.value = new_value
        elif self.tail.value == old_value:
            self.tail.value = new_value
        else:
            temp_node = self.head.next
            while temp_node.value != old_value:
                temp_node = temp_node.next
            temp_node.value = new_value
#   O(n)
    def search(self, value):
        if self.head.value == value or self.tail.value == value:
            return True
        else:
            temp_node = self.head.next
            while temp_node.next != None:
                if temp_node.value == value:
                    return True
                temp_node = temp_node.next
            return False
#   O(n)
    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            current_node = self.head.next
            previous_node = self.head
            while current_node.value != value:
                previous_node = current_node 
                current_node = current_node.next
            if current_node == self.tail:
                previous_node.next = None
                previous_node = self.tail
            else:
                previous_node.next = current_node.next
    def sort(self):
        pass
#   O(n)
    def length(self):
        temp_node = self.head
        count = 0
        while temp_node != None:
            count += 1
            temp_node = temp_node.next
        return count
#   O(n)
    @dispatch()
    def getElements(self):
        temp_node = self.head
        data_list = []
        while temp_node != None:
            data_list.append(temp_node.value)
            temp_node = temp_node.next
        return data_list
#   O(n)
    @dispatch(int)
    def getElements(self,n):
        if(n > self.length()):
            return False
        temp_node = self.head
        data_list = [0] * n
        for i in range(0,n):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
    @dispatch(int,int)
    def getElements(self,start,end):
        if(end >= self.length() or start > end):
            return False
        temp_node = self.head
        getSize = (end - start) + 1
        data_list = [0] * getSize
        for i in range(0,start):
            temp_node = temp_node.next
        for i in range(0,getSize):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
    def getLastElements(self,n):
        size = self.length()
        if(n > size):
            return False
        temp_node = self.head
        data_list = [0] * n
        for i in range(0,size-n):
            temp_node = temp_node.next
        for i in range(0,n):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
    def display(self):
        temp_node = self.head
        end = ' '
        while temp_node != None:
            print(temp_node.value, end=end)
            temp_node = temp_node.next


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

class Tree:
    
    def __init__(self,a,b):
        pass

class Graph:
    
    def __init__(self,a,b):
        pass