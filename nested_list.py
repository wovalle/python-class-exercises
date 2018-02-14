list = [
[1,2,3],
[6,5,4],
[7,8,9],
[12,11,10]
]

for row in range(len(list)):
	if row % 2 != 0:
		list[row].reverse()
	for col in range(len(list[row])):
		print(list[row][col])