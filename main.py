# Build a ListNode class 

class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self): 
        self.head = None

    def insert_end(self, data): 
        node = ListNode(data)
        if not self.head:
            print("List empty")
            self.head = node
            print("Head: " + str(self.head.data))
            return
        print("List not empty")
        now = self.head
        print("Head: " + str(now.data))
        while now.next:
            print("Current node data: " + str(now.data))
            now = now.next
        now.next = node

    def delete_end(self): 
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        now = self.head
        while now.next.next:
            now = now.next
        now.next = None

    def __repr__(self):
        nodes = []
        now = self.head
        while now:
            nodes += [now.data]
            now = now.next
        return str(nodes) + " None"


    # def insert_front():
    #     pass 

    # def delete(): 
    #     pass 


ll_test = LinkedList()
ll_test.insert_end(1)
ll_test.insert_end(2)
ll_test.insert_end(3)
print(ll_test)

# Assigned Dec 27: Use the error messages to debug your code. 
# Focus on insert_end and printing it to be readable. 
# Work on other things 