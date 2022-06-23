# Problem Link https://leetcode.com/problems/intersection-of-two-linked-lists/
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def get_intersection_node(head_a, head_b):
    p1, p2 = head_a, head_b
    while p1 or p2:
        if p1 == p2:
            return p1
        p1 = p1.next if p1 else head_b
        p2 = p2.next if p2 else head_a
    return p1


def display(head):
    if head is None:
        return None

    current = head
    while current is not None:
        print(current.val)
        current = current.next


node1 = Node(4)
node2 = Node(1)
node3 = Node(8)
node4 = Node(4)
node5 = Node(5)

node6 = Node(5)
node7 = Node(6)
node8 = Node(1)
node9 = Node(8)
node10 = Node(4)
node11 = Node(5)



head_a = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None


# p1, p2 = headA, headB
#         while p1 or p2:
#             if p1 == p2:
#                 return p1
#             p1 = p1.next if p1 else headB
#             p2 = p2.next if p2 else headA
#         return p1



head_b = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = None

print(get_intersection_node(head_a, head_b))
# display(head_a)
# print('........................')
# display(head_b)