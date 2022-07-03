# Problem Link https://leetcode.com/problems/linked-list-cycle-ii/

def detect_cycle(head):
    if head is None:
        return

    visited = []
    current = head
    while current is not None:
        if current.next in visited:
            return current

        visited.append(current)
        current = current.next
