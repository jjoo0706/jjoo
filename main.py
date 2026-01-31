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

# ll_test = LinkedList()
# ll_test.insert_end(1)
# print(ll_test)
# ll_test.insert_end(2)
# print(ll_test)
# ll_test.insert_end(3)
# print(ll_test)
# print(ll_test.delete_end())
# print(ll_test)

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

# q= LL_Queue()
# q.enqueue(1)
# print(q)
# q.enqueue(2)
# print(q)
# q.enqueue(3)
# print(q)
# q.enqueue(4)
# print(q)
# print(q.dequeue())
# print(q.dequeue())
# print(q)

# Write a function that will take in a Linked List object and reverse the order.
# 1 -> 2 -> 3 -> 4 -> null 
# 4 -> 3 -> 2 -> 1 -> null 

def reverse(l):
    new_list = LinkedList()
    now = l.head
    while now is not None:
        new_list.insert_front(now.data)
        now = now.next
    return new_list

def reverse1(Linked_List):
    list = []
    num = []
    now = Linked_List.head
    while now is not None:
        num += [now.data]
        now = now.next
    i = len(num) - 1
    while i >= 0:
        list += [num[i]]
        i -= 1
    list += ["None"]
    return list


    # new = Linked_List
    # prev = None
    # now = new.head
    # new.tail = now
    # while now is not None:
        # next = now.next
        # now.next = prev
        # prev = now
        # now = next
    # new.head = prev
    # return (new)

l = LinkedList()
l.insert_end(1)
l.insert_end(2)
l.insert_end(3)
print(reverse(l))
print("l", l)
rl = reverse(l)
print("l", l)
print("rl", rl)



