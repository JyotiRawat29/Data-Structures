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

  def insert_node(pos,val):
    target = Node(val) # creating node for the data, pointing nowehere
    if pos == 0:
      target.next = self.head #making the target pointer as the current head as pos = 0 means its the new head.
      self.head = target # pointing the head pointer towards target
            #has to be done from both pointers i.e. target pointer( target.next) and head pointer(self.head) ↑ 
            #there is no previous node here
    def get_prev(pos):
      temp = self.head #pointer at current head
      count = 1
      while(count<pos): #because we want to stop at position one before pos, hence we used "<" and not "=".
        temp.next = pos
        count+=1
      return temp
    prev_node = get_prev(pos)#node prev
    # storing the pointer of the previous node that denotes the next node
    newnode_ptr = prev_node.next
    prev_node.next = temp
    temp.next = newnode_ptr

linked_list = LinkedList()
linked_list.head = Node(5)
second = Node(4)
third = Node(6)
linked_list.head.next = second
second.next = third
linked_list.print_ll()

#5-4-6
#insert the node 2 at 2 index
linked_list.insert_node(2,2)
linked_list.print_ll()
#5-4-6-2
    
