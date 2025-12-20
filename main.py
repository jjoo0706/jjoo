class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def addfirst(self, item):
        self.items = [item] + self.items

    def addlast(self, item):
        self.items += [item]

    def removefirst(self):
        if self.is_empty():
            return None
        first = self.items[0]
        self.items = self.items[1:]
        return first
    
    def removelast(self):
        if self.is_empty():
            return None
        last = self.items[-1]
        self.items = self.items[:-1]
        return last

    def len(self):
        return len(self.items)

d = Deque()
d.addfirst(2)
print(d.items)
d.addfirst(3)
print(d.items)
d.addfirst(4)
print(d.items)
d.addlast(1)
print(d.items)
print(d.items)
print(d.removelast())
print(d.removefirst())
print(d.items)

# 12-19-25: Look at stuff about LinkedLists, which Julie will send 
# Next time: talk more about relationship between Stack and Queue, and start coding LinkedLists 
