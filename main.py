# Code Selection Sort 

def sel_sort(x):
  for i in range(len(x)):
    for j in range(i + 1, len(x)):
      if x[j] < x[i]:
        temp = x[i]
        x[i] = x[j]
        x[j] = temp
  return x

list = [4, 1, 2, 7, 6]
print(sel_sort(list))
