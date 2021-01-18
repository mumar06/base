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
        while temp_node.next != None:
            count += 1
            temp_node = temp_node.next
        count += 1
        return count
#   O(n)
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

class Tree:
    
    def __init__(self,a,b):
        pass

class Graph:
    
    def __init__(self,a,b):
        pass