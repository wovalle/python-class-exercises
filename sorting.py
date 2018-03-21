lst = [3,4,5,2,7,8,1,6]

def bubble_sort(l):
  for i in range(len(l)):
    for j in range(len(l) - 1):
      if l[j] > l[j+1]:
        temp = l[j]
        l[j] = l[j+1]
        l[j+1] = temp
  return l

def insertion_sort(l):
  for i in range(1, len(l)):
    key = l[i]
    j = i - 1

    while j > 0 and key < l[j]:
      l[j + 1] = l[j]
      j -= 1

    l[j+1] = key
  return l


def selection_sort(l):
  for i in range(len(l)):
    min = i

    for j in range(i, len(l)):
      if l[j] < l[i]:
        min = j
    
    temp = l[i]
    l[i] = l[min]
    l[min] = temp

  return l
 
 
print('bubble_sort', bubble_sort(lst))
print('insertion_sort', insertion_sort(lst))
print('selection_sort', insertion_sort(lst))
