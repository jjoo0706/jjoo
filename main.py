# Build a ListNode class 

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

        # node = ListNode(data)
        # if not self.head:
        #     print("List empty")
        #     self.head = node
        #     print("Head: " + str(self.head.data))
        #     return
        # print("List not empty")
        # now = self.head
        # print("Head: " + str(now.data))
        # while now.next:
        #     print("Current node data: " + str(now.data))
        #     now = now.next
        # now.next = node

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
        # if not self.head:
        #     return
        # if not self.head.next:
        #     self.head = None
        #     return
        # now = self.head
        # while now.next.next:
        #     now = now.next
        # now.next = None

    def __repr__(self):
        nodes = []
        now = self.head
        while now:
            nodes += [now.data]
            now = now.next
        return str(nodes) + " None"

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

    # def insert_loc(self, )

ll_test = LinkedList()
ll_test.insert_end(1)
print(ll_test)
ll_test.insert_end(2)
print(ll_test)
ll_test.insert_end(3)
print(ll_test)
print(ll_test.delete_end())
print(ll_test)

# Build a queue out of a linkedlist 

class LL_Queue:
    def __init__(self):
        self.list = LinkedList()
    
    def is_empty(self):
        return self.list.head == None

    def enqueue(self, item):
        self.list.insert_end(item)

    def dequeue(self):
        self.list.delete_front()
    
    def peek(self):
        if self.list.head == None:
            return None
        return self.list.head.data

    def length(self):
        l = 0
        current = self.list.head
        while current != None:
            l += 1
            current = current.next
        return l

    def __repr__(self):
        return repr(self.list)

q= LL_Queue()
q.enqueue(1)
# print(q)
q.enqueue(2)
# print(q)
q.enqueue(3)
# print(q)
q.enqueue(4)
# print(q)
# print(q.dequeue())
# print(q.dequeue())
# print(q)