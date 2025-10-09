class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Method 1 (Mutate the list(self.head) and no return)
class LinkedList:
    def __init__(self):
        self.head = None
    def createList(self, arr):
        self.head = None
        prev = None
        for x in arr:
            node = Node(x)
            if prev is None:
                self.head = node
            else:
                prev.next = node
                node.prev = prev
            prev = node
    def printlist(self):
        temp = self.head
        ll1 = ""
        while(temp):
            ll1 += str(temp.data)+" "
            temp = temp.next 
        print(ll1)


        # no return
ll = LinkedList()
"""
ll = LinkedList().createList([1,3,2,5,6])
ll.printlist()
It doesnot work because createList() is returning None so ll becomes None and throws error to call printlist.
This method when nothing is returned is used to mutate the internal state and user just interact with
other methods, they donot poke the nodes. In this case the instance owns the structure.
It is the case of clear encapsulation.
Here you access the nodes via the instance you have created like in below lines.
"""
ll.createList([1,3,2,5,6])
ll.printlist()
#METHOD 2 (return self, same as method 1 but it supports chaining, useful for clean APIs)

class LinkedList:
    def createList(self, arr):
        self.head = None
        prev = None
        for x in arr:
            node = Node(x)
            if prev is None:
                self.head = node
            else:
                prev.next = node
                node.prev = prev
            prev = node
        return self
    def printList(self):
        temp = self.head
        ll = ""
        while(temp):
            ll += str(temp.data)+" "
            temp = temp.next # always point to next pointer
        print(ll)

ll =LinkedList().createList([4,3,2,5,6]).printList()
"""
ll =LinkedList().createList([4,3,2,5,6]).printList()

This method works here without any errors because createList is returning self
and self returns the object of the class as whole and not just a value like in method 3.
Encapsulation.

"""

#METHOD 3 standalone builder, returns head. Here the list does not live indśide the class instance, hence needed to keep track of head.
"""
arr = [1,2,3,4,5]
llist = LinkedList()
llist.printList(arr)
This is lsit inside the instance. The LinkedList objects owns the structure via an instance attribute self.head.
You call methods on instance and methods mutate the self.head and other internals.
The list is not destroyed here after createList- the llist keeps a reference to its head in self.head hence the node remains alive.

Outside the instance (raw head node/functional style)
There is no owning object like linkedList. 
def build_dll(arr):
    #logic for buiding list
    return head   # caller keeps the head → "outside any instance"

def printlist(head):
    #logic for printing list
head = build_dll([1,2,3,4,5])  # list exists "outside" any class instance
printlist(head)
Here the caller owns the list via the variable head. Ther is no self.head, you operate directly on node pointers.
If an operation changes the head (e.g., insert/delete at front), the function typically returns the new head.
One must pass/return head explicitly if structure changes.
While in above case self.head keeps the reference hence the node kept alive.

"""
class LinkedList():
    def __init__(self):
        self.head = None

    def createList(self,arr):
        n = len(arr)
        start = self.head
        temp = start
        i = 0
        while(i<n):
            newNode = Node(arr[i])
            if i == 0:
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i +=1
        self.head = start
        return start
    def printList(self):
        temp = self.head
        ll = ""
        while(temp):
            ll += str(temp.data)+" "
            temp = temp.next # always point to next pointer
        print(ll)

arr = [1,2,3,4,5]
llist = LinkedList()
llist.createList(arr)
llist.printList()                

"""
1. arr = [1,2,3,4,5] is a Python list (built-in type) and unrelated to the linked-list internals.
It’s just the input used to build nodes.
2. “Inside” doesn’t mean the nodes are physically inside the LinkedList object; 
it means the object stores a reference (self.head) so you always reach the
structure through that instance.
3. Returning self (fluent/chaining) is still “inside the instance.” Returning head is the “outside” pattern.
"""
