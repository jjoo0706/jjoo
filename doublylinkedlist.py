# Doubly Linked List 
# Instead of ONLY having a pointer that goes forward, we'll also have a pointer that goes backwards. 

class ListNode:
    def __init__(self, data, next = None, prev = None):
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
