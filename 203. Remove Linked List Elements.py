# Problem Link https://leetcode.com/problems/remove-linked-list-elements/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_element(head, val):
    values = []

    current = head
    new_head = None
    while current is not None:
        if current.val != val:
            values.append(current.val)
        current = current.next

    for value in values:
        new_node = Node(value)

        if new_head is None:
            new_head = new_node
        else:
            current2 = new_head
            while current2.next is not None:
                current2 = current2.next
            current2.next = new_node

    return new_head


node1 = Node(1)
node2 = Node(2)
node3 = Node(6)
node4 = Node(3)
node5 = Node(4)
node6 = Node(5)
node7 = Node(6)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None

new_head = remove_element(head, 6)

current = new_head

while current is not None:
    print(current.val)

    current = current.next

