# Tema 2
def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def next_prime(n):
	iterator = n + 1
	while True:
		if is_prime(iterator):
			return iterator
		iterator += 1

# Tema 3
def capitals(string):
	lst = string.split(" ")
	dict = {"count": 0, "indexes": []}

	for i in range(len(lst)):
		if(lst[i].iscapital()):
			dict["count"] += 1
			dict["indexes"].append(i)

	return dict

# Tema 4
def countAdjacentPairs(string):
	lst = string.split(' ')
	count = 0
	for i in range(len(lst) - 1):
		if lst[i] == lst[i +1]:
			count += 1
	return count
