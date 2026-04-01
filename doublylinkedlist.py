# Doubly Linked List
# Instead of ONLY having a pointer that goes forward, we'll also have a pointer that goes backwards.

class ListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def delete_end(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return data

    def insert_front(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def delete_front(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return data

    def __repr__(self):
        nodes = []
        now = self.head
        while now:
            nodes += [now.data]
            now = now.next
        return str(nodes)


ll_test = DoublyLinkedList()

# Insert at front
ll_test.insert_front(3)
print(ll_test)
ll_test.insert_front(1)
print(ll_test)
# Insert multiple
ll_test.insert_end(5)
print(ll_test)
ll_test.insert_end(7)
print(ll_test)
ll_test.insert_end(9)
print(ll_test)
# Delete head
print(ll_test.delete_front())
print(ll_test)
# Delete middle
mid = ll_test.head.next.next
mid.prev.next = mid.next
mid.next.prev = mid.prev
print(ll_test)

# Exercise 1: Reverse a list
# Given a list as a DoubleLinkedList object, return a new a DoublyLinkedList object, where the list is reversed
# 1 -> 2 -> 3
# 3 -> 2 -> 1


def reverse_dllist(DLL):
    new_list = DoublyLinkedList()
    current = DLL.tail
    while current:
        new_list.insert_end(current.data)
        current = current.prev
    return new_list


DLL = DoublyLinkedList()
DLL.insert_end(1)
DLL.insert_end(2)
DLL.insert_end(3)
print(DLL)
rev = reverse_dllist(DLL)
print(rev)
print(DLL)

# Exercise 2: Split a DoublyLinkedList into two lists 
# You do not know the length of the list 
# hint: use a slow and fast pointer 
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# output: 1 <-> 2 <-> 3
#  4 <-> 5 

def split_dllist(DLL):
    if DLL.head is None:
        return DoublyLinkedList(), DoublyLinkedList()
    slow = DLL.head
    fast = DLL.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first = DoublyLinkedList()
    second = DoublyLinkedList()
    current = DLL.head
    while current != slow:
        first.insert_end(current.data)
        current = current.next
    while current:
        second.insert_end(current.data)
        current = current.next
    return first, second

DLL = DoublyLinkedList()
for i in range(1, 6):
    DLL.insert_end(i)
a, b = split_dllist(DLL)
print(a)
print(b)
