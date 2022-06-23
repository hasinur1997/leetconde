class Node:
    def __init__(self, data=0):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        return new_node

    def display(self):
        if self.head is None:
            print("The list is empty nothing to print")
        else:
            current_node = self.head

            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

    def merge(self, head):
        if self._is_empty():
            return head

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = head

        return self.head

    def sort(self):
        if self._is_empty():
            return

        current_node = self.head
        prev = None
        while current_node is not None:
            prev = current_node.next
            while prev is not None:
                if current_node.data > prev.data:
                    temp = current_node.data
                    current_node.data = prev.data
                    prev.data = temp
                prev = prev.next
            current_node = current_node.next

    def reverse(self):
        if self._is_empty():
            return

        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current

            current = next

        self.head = prev

    def delete_node(self, node):
        if self._is_empty():
            return False

        if self.head is node:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next is node:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def _is_empty(self):
        return self.head == None


list1 = LinkedList()

node1 = list1.append(10)
# node2 = list1.append(12)
# node3 = list1.append(15)
# node4 = list1.append(5)
# node5 = list1.append(4)

list1.delete_node(node1)

list1.display()

