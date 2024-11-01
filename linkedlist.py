class Node():
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList():
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            
            curr_node.next = new_node

    def display(self):
        data = []
        curr_node = self.head
        while curr_node:
            data.append(curr_node.data)
            curr_node = curr_node.next

        return data
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node = self.head

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

    def search(self, key):
        curr = self.head
        while curr != None:
            if curr.data == key:
                return True
            curr = curr.next
        return False

