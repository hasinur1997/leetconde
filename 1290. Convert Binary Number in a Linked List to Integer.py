# Problem Link https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_decimal(head):
    if head is None:
        return

    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    values = bin(int(''.join(map(str, values)), 2))
    values = int(values, 2)


    return values


node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)

head = node1
node1.next = node2
node2.next = node3

print(get_decimal(head))

