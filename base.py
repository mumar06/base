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
#   Insert at the end of Linked List
    def insert(self, value):
        # If head is None means the Linked List is empty
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # If head is not None means the Linked List is not empty, hence inserting at the tail
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
#   O(1)
#   Insert at the beginning of Linked List
    def push(self, value):
        # If head is None means the Linked List is empty
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # If head is not None means the Linked List is not empty, hence inserting at the head
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
#   O(n)
#   For Updating a Node in the Linked List, return True if value is updated or False if value not found
    def update(self, old_value, new_value):
        # If the Node, which has to be updated, is the head Node
        if self.head.value == old_value:
            self.head.value = new_value
        # If the Node, which has to be updated, is the tail Node
        elif self.tail.value == old_value:
            self.tail.value = new_value
        # If the Node, which has to be updated, is between head and tail Node
        else:
            temp_node = self.head.next
            while temp_node.value != old_value:
                temp_node = temp_node.next
                # When temp_node reach the end of the linked list and value still not found
                if temp_node == None:
                    return False
            temp_node.value = new_value
        return True
#   O(n)
# For searching a Node, based on value, in the Linked List. Return True if Node is found and False if not found
    def search(self, value):
        # If the Node, which we are searching, is the head Node or tail Node
        if self.head.value == value or self.tail.value == value:
            return True
        # If the Node, which we are searching, is between head Node and tail Node
        else:
            temp_node = self.head.next
            while temp_node.next != None:
                if temp_node.value == value:
                    return True
                temp_node = temp_node.next
            return False
#   O(n)
#   For deleting a Node, based on value, in the Linked List. return True if value is deleted or False if value not found
    def delete(self, value):
        # If the Node, which we want to delete, is the head Node
        if self.head.value == value:
            self.head = self.head.next
        # If the Node, which we want to delete, is the not head Node
        else:
            current_node = self.head.next
            previous_node = self.head
            while current_node.value != value:
                previous_node = current_node 
                current_node = current_node.next
                # If value not found in the Linked List
                if current_node == None:
                    return False
            # If Node, to be deleted, is the Tail Node
            if current_node == self.tail:
                previous_node.next = None
                previous_node = self.tail
            # If Node, to be deleted, is other than Head Node and Tail Node
            else:
                previous_node.next = current_node.next
        return True

#   O(n)
#   For deleting a Node present at the end of the Linked List
    def pop(self):
        current_node = self.head.next
        previous_node = self.head
        while current_node != self.tail:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        previous_node = self.tail
#   O(1)
#   For sorting a Linked List, using merge sort algorithm with divide and conqure approach, sort -> mergesort -> merge
    def sort(self):
        self.head = self.mergesort(self.head)
#   O(nlogn)
    def mergesort(self, head):
        size = self.length(head)
        if size < 2:
            return head
        mid = size // 2
        # For Dividing Linked List which is on the left side
        new_node = Node(head.value)
        head_left = new_node
        tail_left = new_node
        temp_node = head.next
        for i in range(mid-1):
            new_node = Node(temp_node.value)
            tail_left.next = new_node
            tail_left = new_node
            temp_node = temp_node.next
        # For Dividing Linked List which is on the right side
        new_node = Node(temp_node.value)
        head_right = new_node
        tail_right = new_node
        temp_node = temp_node.next
        for i in range(mid,size-1):
            new_node = Node(temp_node.value)
            tail_right.next = new_node
            tail_right = new_node
            temp_node = temp_node.next
        # Recursive calls for remaining node untill Linked List length comes to 1
        head_left = self.mergesort(head_left)
        head_right = self.mergesort(head_right)
        # For merging the Linked List in increasing order
        return self.merge(head_left,head_right)

    def merge(self, left_temp, right_temp):
        temp_node = Node()
        head = temp_node
        tail = temp_node
        while left_temp != None and right_temp != None:
            if left_temp.value <= right_temp.value:
                tail.next = left_temp
                tail = left_temp
                left_temp = left_temp.next
            else:
                tail.next = right_temp
                tail = right_temp
                right_temp = right_temp.next
        # If a Node still present in the left_temp linked list which is still not yet merge
        if left_temp != None:
            tail.next = left_temp
            tail = left_temp
        # If a Node still present in the right_temp linked list which is still not yet merge
        if right_temp != None:
            head.next = right_temp
            tail = right_temp
        # Returning the Next node after head, as head is an empty Node
        return head.next

#   O(n)
#   For calculating the lenght of the Linked List
    def length(self, head = None):
        # When lenght() method is called by the user
        if head == None:
            temp_node = self.head
        # When lenght() method is called by the mergesort() method
        else:
            temp_node = head
        count = 0
        while temp_node != None:
            count += 1
            temp_node = temp_node.next
        return count
#   O(n)
#   For getting all the nodes' value, it will return an array
    @dispatch()
    def getElements(self):
        temp_node = self.head
        data_list = []
        while temp_node != None:
            data_list.append(temp_node.value)
            temp_node = temp_node.next
        return data_list
#   O(n)
#   For getting first n nodes's value, it will return an array
    @dispatch(int)
    def getElements(self,n):
        # When n is greater then the length of the Linked List
        if(n > self.length()):
            return False
        temp_node = self.head
        # Creating an array of size n with 0 as a default value at each index
        data_list = [0] * n
        for i in range(0,n):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
#   For getting Node's value between start index till end index, it will return an array
    @dispatch(int,int)
    def getElements(self,start,end):
        # When start and end is out of renge of the Linked List
        if(end >= self.length() or start > end):
            return False
        temp_node = self.head
        getSize = (end - start) + 1
        # Creating an array of size n with 0 as a default value at each index
        data_list = [0] * getSize
        for i in range(0,start):
            temp_node = temp_node.next
        for i in range(0,getSize):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
#   For getting last n Node's value, it will return an array
    def getLastElements(self,n):
        size = self.length()
        # When n is out of renge of the Linked List
        if(n > size):
            return False
        temp_node = self.head
        # Creating an array of size n with 0 as a default value at each index
        data_list = [0] * n
        for i in range(0,size-n):
            temp_node = temp_node.next
        for i in range(0,n):
            data_list[i] = temp_node.value
            temp_node = temp_node.next
        return data_list
#   O(n)
#   For displaying whole Linked List
    def display(self):
        temp_node = self.head
        # To replace new line with a space when printing the whole Linked List 
        end = ' '
        while temp_node != None:
            print(temp_node.value, end=end)
            temp_node = temp_node.next
        print()


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