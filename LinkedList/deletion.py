class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_ll(self):
        temp = self.head
        ll = ""
        while(temp):
            ll += str(temp.data)+" "
            temp = temp.next
    
    def deltion(self,val):
        temp = self.head
        if temp is None:
            return 
        if temp.data == val:
            self.head = temp.next
            temp = None
            return
        while(temp.next.data !=val): # moving until the next node we want to delete
            temp = temp.next
        target_node = temp.next
        temp.next = target_node.next
        target_node.next = None

linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

#5 1 3 7
linked_list.deltion(3)
#5 1 7
linked_list.print_ll()
        
        


            
