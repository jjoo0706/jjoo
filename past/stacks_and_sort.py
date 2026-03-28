# Code Selection Sort

# def sel_sort(x):
#     for i in range(len(x)):
#         for j in range(i + 1, len(x)):
#             if x[j] < x[i]:
#                 temp = x[i]
#                 x[i] = x[j]
#                 x[j] = temp
#     return x


# lst = [4, 1, 2, 7, 6, 25, 36, 12, 42]
# # print(sel_sort(list))

# # Code Insertion Sort


# def ins_sort(x):
#     for i in range(len(x)):
#         j = i
#         while j > 0 and x[j] < x[j-1]:
#             temp = x[j]
#             x[j] = x[j-1]
#             x[j-1] = temp
#             j -= 1
#     return x


# # print(ins_sort(lst))

# # write helper function merge
# def merge_step(x, y):
#     m = [0] * (len(x) + len(y))
#     i = 0
#     j = 0
#     k = 0
#     while i < len(x) and j < len(y):
#         if x[i] <= y[j]:
#             m[k] = x[i]
#             i += 1
#         else:
#             m[k] = y[j]
#             j += 1

#         k += 1
#     while i < len(x):
#         m[k] = x[i]
#         i += 1
#         k += 1

#     while j < len(y):
#         m[k] = y[j]
#         j += 1
#         k += 1

#     return m


# list1 = [1, 3, 5, 8, 11, 2, 4, 7, 9]

# # print(merge_step(list1, list2))

# # HOMEWORK ASSIGNED 10/18 - Code up MergeSort! Use the merge_step in order to code MergeSort. I want you to try to do it using recursion, but it's not entirely necessary. If you get stuck trying to do it in recursion, you can just use loops.


# def merge_sort(x):
#     if len(x) <= 1:
#         return x
#     middle = len(x) // 2
#     l = x[:middle]
#     r = x[middle:]

#     left_s = merge_sort(l)
#     right_s = merge_sort(r)

#     return merge_step(left_s, right_s)

# # print(merge_sort(list1))


# # HOMEWORK ASSIGNED OCT 25
# # I'll send you notes on quicksort
# # Try finishing this function!
# def quick_sort(x):
#     if len(x) <= 1:
#         return x
#     pivot_index = len(x) // 2
#     pivot = x[pivot_index]
#     left = []
#     mid = []
#     right = []
#     for y in x:
#         if y < pivot:
#             left += [y]
#         elif y == pivot:
#             mid += [y]
#         else:
#             right += [y]
#     left_s = quick_sort(left)
#     right_s = quick_sort(right)
#     return left_s + mid + right_s


# # print(quick_sort(list1))

# # Code Bubble Sort


# def bubble_sort(x):
#     n = len(x)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if x[j] > x[j + 1]:
#                 temp = x[j]
#                 x[j] = x[j + 1]
#                 x[j + 1] = temp
#     return x


# # print(bubble_sort(list1))

# # Code a stack using Object oriented programming


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items += [item]

    def pop(self):
        if not self.is_empty():
            top = self.items[-1]
            self.items = self.items[:-1]
            return top
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

# Write up the Queue class
# Also I'll give you some exercises using stacks and queues


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items += [item]

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.items[0]
        self.items = self.items[1:]
        return front

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def length(self):
        return len(self.items)

# q = Queue()
# l = [1, 2, 3, 4, 5]
# for i in l:
    # q.enqueue(i)

# Use your stack class to identify balaned parenthesis
# "(()())" -> True
# "(()" -> False
# "([{}])" -> True
# ")("


def balanced_paren(x):
    stack = Stack()
    list_open = "([{"
    close = "}])"

    print(stack)
    for i in x:
        if i in list_open:
            stack.push(i)
            print(stack)
        elif i in close:
            if stack.is_empty():
                print("return 1")
                return False
            top = stack.pop()
            match = False
            for j in range(len(list_open)):
                print(list_open[j], top)
                print(close[j], i)
                print("---")
                if list_open[j] == top and close[j] == i:
                    print("here")
                    match = True
                    break

    print("return 3")
    return stack.is_empty()


p = "(()())"
# print(balanced_paren(p))

# HOMEWORK: Build a queue using only two stacks


class QueueStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.is_empty():
            return None
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def length(self):
        return self.in_stack.size() + self.out_stack.size()

    def __repr__(self):
        temp_in = []
        temp_out = []
        for i in self.out_stack.items[::-1]:
            temp_out += [i]
        for i in self.in_stack.items:
            temp_in += [i]
        return str(temp_out + temp_in)


# q = QueueStack()
# for i in [1, 2, 3, 4, 5]:
#     q.enqueue(i)
# print(repr(q))
# print(q.length())
# print(q.peek())
# print(q.dequeue())
# print(q.dequeue())
# print(repr(q))
# print(q.length())
# print(q.peek())

# Use the Queue object to build a "Hot Potato"
# List of names, an integer number $n$
# After passing the number n times, remove the name at the top of queue
# Continue to do this until there is one name left.


def hot_potato(names, n):
    q = Queue()
    for i in names:
        q.enqueue(i)
    while q.length() > 1:
        for i in range(n):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


names = ["Russell", "Ethan", "Daniel", "Luke", "Ryan"]
# print(hot_potato(names, 3))

# Build a stack out of two queues.
# 12/6 - Start today, but finish for homework
# Write a test for your StackQueue


class StackQueue():
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def is_empty(self):
        return self.q1.is_empty()

    def push(self, item):
        self.q2.enqueue(item)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        if self.q1.is_empty():
            return None
        return self.q1.dequeue()

    def peek(self):
        return self.q1.peek()

    def size(self):
        return self.q1.length()

    def __repr__(self):
        return str(self.q1.items)

def simple():
    return 1

q = StackQueue()
q.push(1)
q.push(2)
q.push(3)
print("1", q)
print("2", q.pop())
print("3", q.pop())
q.push(4)
print("4", q)
print(simple)
