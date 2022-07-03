# Problem Link https://leetcode.com/problems/odd-even-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def odd_even_list(head):
    values = []

    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    odd = [values[i] for i in range(len(values)) if i % 2 == 1 or i == 0]
    even = [values[i] for i in range(len(values)) if i % 2 == 0]

    new_values = odd + even

    return new_values
    # h = None
    #
    # for i in new_values:
    #     new_node = Node(i)
    #     if h is None:
    #         h = new_node
    #
    #     current = h
    #     while current.next is not None:
    #         current = current.next
    #
    #     current.next = new_node
    #
    # return h



value = [1, 3, 4, 5]
h = None

for i in value:
    new_node = Node(i)
    if h is None:
        h = new_node
    else:
        current = h
        while current.next is not None:
            current = current.next

        current.next = new_node



def check(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    print(s1)

    if s1 == s2:
        return True

    if s1 in s2:
        return True

    return False

print(check('ab', 'eidbaooo'))


persons = ['Rahim', 'Karim', 'Badsha']

print(persons)


# append
# prepend
# pop

