# how index works

list = ['steelix', 'barbaro', 'manuel', 'snow']

# for idx in range(0, 4):
# 	print(idx, list[idx])

# create a function that recieves a list as argument and prints the second position of the list

def print_second(lst):
	print('The second position is', lst[2])


def print_even(lst):
	for idx in range(0, len(lst)):
		if(idx % 2 == 0):
			print(idx, lst[idx])

# print_second(list)
# print_even(list)


list2 = ('Ruby', 'Rainer', 'numero_1')
# print('List elements', list2)

# list2[0] = 'Javipo'
# list2[1] = 'Irina'
# print('After modification', list2)


# slicing

list3 = ['Ruby', 'Rainer', 'numero_1', 'Massih', 'Fofi', 'Irina', 'Rainer', 'Snow']

# print('original list', list3)
# print('sliced list', list3[1:7])

# print('original list', list3[2])
# print('sliced list', list3[1:7][2])

# Write a function that recieves a list and returns all elements but the first and the last

def not_first_last(lst):
	print(lst[1:len(lst) -1])

# not_first_last(list3)


list4 = ('Javipo', 'Federico', ' numero_2', 'Bido')
list5 = ('Osvardu', "Tom Clancy's")

print(list4 + list5)
# print(list5 * 2)
# print(list5 * list5)




































