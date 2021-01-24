# base
# Basic implementation of important data structures in python.

Following data structures were implemented: <br>
### 1, Linked List

####    Initialization:
from base import Linkedlist
        myList = Linkedlist()

####    Functions/Methods Description:
**a, insert():** <br>
- Takes one argument, which is a Node value <br>
- Insert at the end of Linked List. <br>

**b, push():** <br>
- Takes one argument, which is a Node value. <br>
- Insert at the beginning of Linked List. <br>

**c, delete():** <br>
- Takes one argument, a Node value which has to be deleted. <br>
- For deleting a Node, based on value, in the Linked List. return True if value is deletedor False if value not found. <br>

**d, pop():** <br>
- Takes no argument. <br>
- For deleting a Node present at the end of the Linked List. <br>

**e, update():** <br>
- Takes two arguments, Node's old value and new value. <br>
- For Updating a Node in the Linked List, return True if value is updated or False if valuenot found. <br>

**f, search():** <br>
- Takes one argument, a Node's value which needs to be found. <br>
- For searching a Node, based on value, in the Linked List. Return True if Node is found andFalse if not found. <br>

**g, sort():** <br>
- Takes no argument. <br>
- For sorting a Linked List, using merge sort algorithm with divide and conqure approach.<br>

**h, length():** <br>
- Takes no argument. <br>
- For calculating the lenght of the Linked List. <br>

**i, display():** <br>
- Takes no argument. <br>
- For displaying whole Linked List. <br>

**j, getElements():**<br>
- Takes no arguments. <br>
- For getting all the nodes' value, it will return an array. <br>

**k, getElements(para_one):** <br>
- Takes one argument, which is number of Nodes needed. <br>
- For getting first n nodes's value, it will return an array. <br>

**l, getElements(para_one, para_two):** <br>
- Takes two arguments, starting point and ending point. <br>
- To get elements which are between Head Node and Tail Node. <br> 
- For getting Node's value between start index till end index, start and end point will alsobeincluded. It will return an array. <br>

**m, getLastElements(para_one):** <br>
- Takes one argument, which is number of Nodes needed. <br>
- For getting last n Node's value, it will return an array. <br>

### Doubly Linked List (On Hold) <br>
### Circular Linked List (On Hold) <br>
### 2, Stack <br>
### 3, Queue <br>
### 4, Priority Queue <br>
### 5, Hash <br>
### 6, Graph <br>
### 7, Tree <br>