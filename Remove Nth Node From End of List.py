# Problem Link https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_nth_from_end(head, n):
   first = second = head

   for i in range(n):
       first = first.next

   if not first:
       return head.next

   while first.next:
       second = second.next
       first = first.next

   second.next = second.next.next

   return head

def display(head):
    if head is None:
        print("Nothing to print")
        exit()

    current = head

    while current is not None:
        print(current.val)
        current = current.next


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4



display(remove_nth_from_end(node1, 3))
