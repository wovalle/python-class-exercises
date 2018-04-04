def binary_search(lst, look_for):
	first = 0 #9
	last = len(lst) - 1 #8 

	while last > first:

		mid = (first + last) // 2 #8

		if lst[mid] == look_for:
			return mid
		elif look_for > lst[mid]:
			first = mid + 1
		elif look_for < lst[mid]:
			last = mid - 1

	return -1

list_of_data = [1,2,3,4,5,6,7,8,9]

print('pos', binary_search(list_of_data, 8))
print('pos', binary_search(list_of_data, 10))












