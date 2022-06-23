# Problem Link https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_middle_node(head):
    if head is None:
        return
    nodes = count_node(head)
    mid = (nodes // 2) + 1

    current = head
    index = 1
    while index < mid:
        current = current.next
        index += 1

    return current


def count_node(head):
    if head is None:
        return 0

    counter = 0
    current = head

    while current is not None:
        counter += 1
        current = current.next

    return counter


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
# node6 = ListNode(6)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6

print(get_middle_node(head).val)


# total = 8

