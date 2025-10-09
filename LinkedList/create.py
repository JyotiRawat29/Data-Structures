class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None

  def print_ll(self):
    temp =self.head
    ll = ""
    while(temp):
      ll += str(temp.data)+">"
      temp= self.head.next
    return ll

linked_list = LinkedList()
linked_list.head = Node(5)
second = Node(4)
third = Node(6)
linked_list.head.next = second
second.next = third

linked_list.print_ll()
5 4 6 
inseting data 8 at index 2, position 3

linked_list.head.next = second_node
new_node = Node(8)

5 4 6 8
"""
The below 3 lines uses only knowledge about previous node to identify and connect the linked list with new element.
The trick is to store the pointer of the previous node and than using it.
Hence to insert new node only the info about the previous knowledge is required.
"""
nextnode = second_node.next
second_node.next = new_node
new_node.next = nextnode
linked_list.print_ll()

"""
In the below 3 lines we are using knowledge of previous and next node to insert the new element.
"""
second_node.next = new_node
new_node.next = third_node
third_node.next = fourth_node
linked_list.print_ll()

#insertion with modular programming
#insertion.py

#Now delete 6 from the linkedlist.

second.next = new_node
linked_list.print_list()
#deletion with modular programming
#deletion.py
    
