# Problem Link https://leetcode.com/problems/add-two-numbers/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

def add_two_numbers(l1, l2):
    data1 = get_data(l1)
    data2 = get_data(l2)

    data1 = ''.join(data1)
    data2 = ''.join(data2)

    summation = int(data1) + int(data2)

    summation = reversed(list(str(summation)))
    list1 = LinkList()
    for num in summation:
        list1.insert(num)

    return list1.head


def get_data(head):
    if head is None:
        return

    current = head
    values = []

    while current is not None:
        values.append(str(current.val))
        current = current.next


    return reversed(values)


node1 = Node(2)
node2 = Node(4)
node3 = Node(3)

node1.next = node2
node2.next = node3

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)

node4.next = node5
node5.next = node6


print(add_two_numbers(node1, node4))
