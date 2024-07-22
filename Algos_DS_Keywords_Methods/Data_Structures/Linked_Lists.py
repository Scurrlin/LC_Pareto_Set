# Linked List

# A linked list is a linear data structure where each element is a separate
# object, called a node. Each node contains data and a reference (or link) to
# the next node in the sequence.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)