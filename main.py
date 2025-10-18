# Code Selection Sort

def sel_sort(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[j] < x[i]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x


lst = [4, 1, 2, 7, 6, 25, 36, 12, 42]
# print(sel_sort(list))

# Code Insertion Sort
def ins_sort(x):
    for i in range(len(x)):
        j = i
        while j > 0 and x[j] < x[j-1]:
            temp = x[j]
            x[j] = x[j-1]
            x[j-1] = temp
            j -= 1
    return x


# print(ins_sort(lst))

# write helper function merge 
def merge_step(x, y):
    m = [0] * (len(x) + len(y))
    i = 0
    j = 0
    k = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            m[k] = x[i]
            i += 1
        else:
            m[k] = y[j]
            j += 1

        k += 1
    while i < len(x):
        m[k] = x[i]
        i += 1
        k += 1

    while j < len(y):
        m[k] = y[j]
        j += 1
        k += 1

    return m

list1 = [1, 3, 5, 8]
list2 = [2, 4, 7, 9]

print(merge_step(list1, list2))

# HOMEWORK ASSIGNED 10/18 - Code up MergeSort! Use the merge_step in order to code MergeSort. I want you to try to do it using recursion, but it's not entirely necessary. If you get stuck trying to do it in recursion, you can just use loops. 


