class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
        prev = None
        current_ = self.head
        while current_.data != data or current_.next is None:
            prev = current_
            current_ = current_.next
        
        prev.next = current_.next
        current_ = None
            
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

l = LinkedList()
l.append(1)
l.append(1)
l.append(1)
l.append(3)
l.append(3)
l.delete(3)
l.print_list()

