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
    
