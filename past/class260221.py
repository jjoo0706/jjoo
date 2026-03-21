# LinkedList and MergeSort 
# Code MergeSort using LinkedLists 

class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList: 
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
        self.tail = node
    
    def delete_end(self):
        if self.head == None:
            return None
        if self.head.next == None:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        now = self.head
        while now.next != self.tail:
            now = now.next
        data = self.tail.data
        now.next = None
        self.tail = now
        return data

    def __repr__(self):
        nodes = []
        now = self.head
        while now:
            nodes += [now.data]
            now = now.next
        return str(nodes)

    def insert_front(self, data):
        node = ListNode(data)
        node.next = self.head
        self.head = node

    def delete_front(self): 
        if not self.head:
            return None
        delete = self.head.data
        self.head = self.head.next
        return delete
    
def merge_step(x, y):
    temp = ListNode(0)
    k = temp
    i = x
    j = y
    while i and j:
        if i.data <= j.data:
            k.next = i
            i = i.next
        else:
            k.next = j
            j = j.next
        k = k.next
    while i:
        k.next = i
        i = i.next
        k = k.next
    while j:
        k.next = j
        j = j.next
        k = k.next
    return temp.next

def length_check(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def split(head, index):
    now = head
    for i in range(index - 1):
        now = now.next
    right = now.next
    now.next = None
    return right

def merge_sort(head):
    if head is None or head.next is None:
        return head
    len = length_check(head)
    middle = len // 2
    left = head
    right = split(head, middle)
    left_s = merge_sort(left)
    right_s = merge_sort(right)
    return merge_step(left_s, right_s)

ll = LinkedList()
ll.insert_end(4)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(1)
print(ll)
ll.head = merge_sort(ll.head)
print(ll)


