class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.size = 0


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def display(self):
        if self.head is None:
            print("List is none. Nothing to display.")
            exit()

        current = self.head

        while current is not None:
            print(current.val)
            current = current.next

    def delete_first(self):
        if self.head is None:
            print("List is empty nothing to delete from this list")
            exit()

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("The list is empty. Nothing to delete from this list.")
            exit()

        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next

            current.next = None

    def delete_nth(self, k):
        if self.head is None:
            print("The list is empty. Nothing delete from this list")
            exit()

        if k == 1:
            self.head = self.head.next
        else:
            index = 1
            current = self.head
            while index < k:
                current = current.next
                index += 1

            current.next = current.next.next

    def delete_nth_end(self, n):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            exit()

        target = self.size() - n

        if n == self.size():
            target = 1
        self.delete_nth(target)

    def reverse(self):
        if self.head is None:
            return

        current = self.head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def size(self):
        if self.head is None:
            return 0

        size = 0

        current = self.head
        while current is not None:
            size += 1
            current = current.next

        return size


test = LinkedList()

test.append(10)
test.append(30)
test.append(120)
test.append(134)
test.append(131)
test.append(132)

test.delete_nth_end(2)
test.display()

