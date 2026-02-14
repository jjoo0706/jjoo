# Homework assigned on 1/31/26

# QUESTION 1
# Write a function that will detect a cycle.
# https://www.geeksforgeeks.org/dsa/floyds-cycle-finding-algorithm/
# 1 -> 2 -> 3 -> 4 -----> false
# 1 -> 2* - > 3 -> 4 -> 2* ------> true (4 points to 2*, which is the same 2* as the one between 1 and 3)

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c
# c.next = d
# d.next = b

# print(Cycle(a))

 # QUESTION 2
 # Write a function that will reorder nodes so that:
 # 1. All the nodes < x will come before
 # 2. All the nodes >= x will come after
 # 3. The order of the nodes is preserved
 # Example:
 # Input: 1 -> 4 -> 3 -> 2 -> 5 -> 1, x = 3
 # Output: 1 -> 2 -> 1 -> 3 -> 4 -> 5


def reorder(head, x):
    small = None
    s_tail = None
    big = None
    b_tail = None
    current = head
    while current:
        n_node = current.next
        current.next = None
        if current.val < x:
            if small is None:
                small = current
                s_tail = current
            else:
                s_tail.next = current
                s_tail = current
        else:
            if big is None:
                big = current
                b_tail = current
            else:
                b_tail.next = current
                b_tail = current
        current = n_node
    if s_tail:
        s_tail.next = big
        return small
    else:
        return big

a = Node(1)
b = Node(4)
c = Node(3)
d = Node(2)
e = Node(5)
f = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

new_head = reorder(a, 3)
print(new_head)