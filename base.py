# below model is used for function overriding
from multipledispatch import dispatch
###############################################################################################################################
#
#                                                       NODE
#
###############################################################################################################################
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

###############################################################################################################################
#
#                                               LINKED LIST DATA STRUCTURE
#
###############################################################################################################################
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
        # When Linked List is empty
        if self.head == None:
            return False
        # When Linked List has only one Node
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return True
        else:
            current_node = self.head
            previous_node = self.head
            while current_node != self.tail:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            previous_node = self.tail
            return True
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
        if self.head == None:
            return False
        else:
            temp_node = self.head
            # To replace new line with a space when printing the whole Linked List 
            end = ' '
            while temp_node != None:
                print(temp_node.value, end=end)
                temp_node = temp_node.next
            print()
            return True


class DoublyLinkedlist:
    
    def __init__(self,a,b):
        pass

class CircularLinkedlist:
    
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                               STACK DATA STRUCTURE
#
###############################################################################################################################
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
#   O(1)
#   Insert at the end of Stack
    def push(self,value):
        # If head is None means the Stack is empty
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # If head is not None means the Stack is not empty, hence inserting at the tail
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
#   O(1)
#   For deleting a Node present at the end of the Stack
    def pop(self):
        # When Queue is empty
        if self.head == None:
            return False
        # When Stack has only one Node
        elif self.head == self.tail:
            temp_node = self.head 
            self.head = None
            self.tail = None
            return temp_node.value
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node.value
#   O(n)
#   For Updating a Node in the Stack, return True if value is updated or False if value not found
    def update(self, old_value, new_value):
        # If the Node, which has to be updated, is the Head Node
        if self.head.value == old_value:
            self.head.value = new_value
        # If the Node, which has to be updated, is the Tail Node
        elif self.tail.value == old_value:
            self.tail.value = new_value
        # If the Node, which has to be updated, is between Head and Tail Node
        else:
            temp_node = self.head.next
            while temp_node.value != old_value:
                temp_node = temp_node.next
                # When temp_node reach the end of the Stack and value still not found
                if temp_node == None:
                    return False
            temp_node.value = new_value
        return True
#   O(n)
#   For deleting a Node, based on value, in the Stack. Return True if value is deleted or False if value not found.
    def delete(self, value):
        # If the Node, which we want to delete, is the Head Node
        if self.head.value == value:
            self.head = self.head.next
        # If the Node, which we want to delete, is the not Head Node
        else:
            current_node = self.head.next
            previous_node = self.head
            while current_node.value != value:
                previous_node = current_node 
                current_node = current_node.next
                # If value not found in the Stack
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
# For searching a Node, based on value, in the Stack. Return True if Node is found and False if not found
    def search(self, value):
        # If the Node, which we are searching, is the Head Node or Tail Node
        if self.head.value == value or self.tail.value == value:
            return True
        # If the Node, which we are searching, is between Head Node and Tail Node
        else:
            temp_node = self.head.next
            while temp_node.next != None:
                if temp_node.value == value:
                    return True
                temp_node = temp_node.next
            return False
#   O(n)
#   For calculating the lenght of the Stack
    def length(self):
        temp_node = self.head
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
#   For displaying whole Stack
    def display(self):
        if self.head == None:
            return False
        else:
            temp_node = self.head
            # To replace new line with a space when printing the whole Linked List 
            end = ' '
            while temp_node != None:
                print(temp_node.value, end=end)
                temp_node = temp_node.next
            print()
            return True
    
###############################################################################################################################
#
#                                               QUEUE DATA STRUCTURE
#
###############################################################################################################################
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
#   O(1)
#   Insert at the end of Queue
    def enqueue(self,value):
        # If head is None means the Queue is empty
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # If head is not None means the Queue is not empty, hence inserting at the Head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
#   O(1)
#   For deleting a Node present at the end of the Queue
    def dequeue(self):
        # When Queue is empty
        if self.head == None:
            return False
        # When Queue has only one Node
        elif self.head == self.tail:
            temp_node = self.head
            self.head = None
            self.tail = None
            return temp_node.value
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node.value
#   O(n)
#   For Updating a Node in the Queue, return True if value is updated or False if value not found
    def update(self, old_value, new_value):
        # If the Node, which has to be updated, is the Head Node
        if self.head.value == old_value:
            self.head.value = new_value
        # If the Node, which has to be updated, is the Tail Node
        elif self.tail.value == old_value:
            self.tail.value = new_value
        # If the Node, which has to be updated, is between Head and Tail Node
        else:
            temp_node = self.head.next
            while temp_node.value != old_value:
                temp_node = temp_node.next
                # When temp_node reach the end of the Queue and value still not found
                if temp_node == None:
                    return False
            temp_node.value = new_value
        return True
#   O(n)
#   For deleting a Node, based on value, in the Queue. Return True if value is deleted or False if value not found.
    def delete(self, value):
        # If the Node, which we want to delete, is the Head Node
        if self.head.value == value:
            self.head = self.head.next
        # If the Node, which we want to delete, is the not Head Node
        else:
            current_node = self.head.next
            previous_node = self.head
            while current_node.value != value:
                previous_node = current_node 
                current_node = current_node.next
                # If value not found in the Queue
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
# For searching a Node, based on value, in the Queue. Return True if Node is found and False if not found
    def search(self, value):
        # If the Node, which we are searching, is the Head Node or Tail Node
        if self.head.value == value or self.tail.value == value:
            return True
        # If the Node, which we are searching, is between Head Node and Tail Node
        else:
            temp_node = self.head.next
            while temp_node.next != None:
                if temp_node.value == value:
                    return True
                temp_node = temp_node.next
            return False
#   O(n)
#   For calculating the lenght of the Queue
    def length(self):
        temp_node = self.head
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
#   For displaying whole Queue
    def display(self):
        if self.head == None:
            return False
        else:
            temp_node = self.head
            # To replace new line with a space when printing the whole Linked List 
            end = ' '
            while temp_node != None:
                print(temp_node.value, end=end)
                temp_node = temp_node.next
            print()
            return True

###############################################################################################################################
#
#                                               HASH DATA STRUCTURE
#
###############################################################################################################################
class Hash:
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                               Generic TREE NODE
#
###############################################################################################################################
class GenericTreeNode:
    def __init__(self,value = None):
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        # self.children.append(child)
        self.children.insert(len(self.children),child)

###############################################################################################################################
#
#                                           Generic TREE DATA STRUCTURE
#
###############################################################################################################################
class GenericTree:
    def __init__(self):
        self.root = None

#   O(V + E)
    def insert(self,value,parent = None):
        if parent == None:
            new_node = GenericTreeNode(value)
            self.root = new_node
        else:
            parent = self.search_parent(parent)
            if parent == False:
                return False
            else:
                parent.add_child(GenericTreeNode(value))

#   O(V + E)
    def search_parent(self,parent):
        temp_node = self.root
        queue = []
        queue.append(temp_node)
        if temp_node.value == parent:
            return temp_node
        while queue:
            temp_node = queue.pop()
            for child in temp_node.children:
                if child.value == parent:
                    return child
                else:
                    temp_node = child
                    queue.append(child)
        return False

#   O(V + E)
    def display(self):
        if self.root == None:
            print(False)
        else:
            temp_node = self.root
            end = ' '
            queue = []
            queue.append(temp_node)
            print(f"Root -> {temp_node.value}")
            while queue:
                temp_node = queue.pop()
                if temp_node.children != []:
                    print(f"Parent -> {temp_node.value}\t Children -> ",end=end)
                for child in temp_node.children:
                    print(f"{child.value}\t",end=end)
                    queue.append(child)
                if temp_node.children != []:
                    print()



###############################################################################################################################
#
#                                             BINARY TREE DATA STRUCTURE
#
###############################################################################################################################
class BinaryTree:
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                         BINARY SEARCH TREE DATA STRUCTURE
#
###############################################################################################################################
class BinarySearchTree:
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                              MIN HEAP DATA STRUCTURE
#
###############################################################################################################################
class MinHeap:
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                              MAX HEAP DATA STRUCTURE
#
###############################################################################################################################
class MaxHeap:
    def __init__(self,a,b):
        pass

###############################################################################################################################
#
#                                               GRAPH DATA STRUCTURE
#
###############################################################################################################################
class Graph:
    def __init__(self,a,b):
        pass
