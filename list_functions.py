# append
list = [1, 2, 3, 4, 5]
print('original list', list)

list.append(6)
list.append('massih')

print('after append', list)

list.insert(1, 1.5)
list.insert(0, 0)
print('after insert', list)

list.extend([9,9,9])
print('after extend', list)

list.remove(9)
print('after remove', list)

list.reverse()
print('after reverse', list)

print('index', list.index('massih'))
print('after index', list)

print('pop', list.pop(2))
print('after pop', list)

list.sort()
print('after sort', list)





