#double linked list: each node having 2 pointers previous and next
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        temp = self.head
        ll = ""
        while(temp):
            ll += str(temp.data)+" "
            temp = temp.next
        print(ll)

linked_list = LinkedList()
linked_list.head = Node(5)
second = Node(4)
third = Node(5)
fourth = Node(3)
fifth = Node(10)
linked_list.head.next = second
second.next = third
second.prev = linked_list.head
third.next = fourth
third.prev = second
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth
linked_list.print_ll()
# 5 4 5 3 10
#making it modular
#creation_v1.py


