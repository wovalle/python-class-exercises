path = 'db.txt'
path2 = 'homeworks/db2.txt'

file = open(path, 'r')
# content = file.readline()
# file.seek(1)
print('file1', file.readlines())
file.close()

file = open(path2, 'r')
print('file2', file.readlines())
file.close()
file = open(path2, 'w')
file.write('"Massih no forza\n"')
file.close()

with open(path2, 'r+') as f:
	f.write('yesssir')

print(f.readlines())
print(f.closed)
