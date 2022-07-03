# Problem Link https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):

        if self.head is None:
            return -1

        current = self.head
        for i in range(index):
            current = current.next

            if current is None:
                return -1

        return current.val

    def add_at_head(self, val):
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def add_at_index(self, index, val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index-1):
                if current is None:
                    return
                current = current.next

            if current:
                new_node.next = current.next
                current.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if current.next is None:
                    return
                current = current.next

            if current.next:
                current.next = current.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next



l = LinkedList()

l.add_at_head(1)
l.add_at_tail(3)
l.add_at_index(3,2)