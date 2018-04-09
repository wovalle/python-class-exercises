#Tema 1
def people_remaining(list):
  count = 0
  for item in list:
    count += item[0]
    count -= item[1]
  return count

# print(people_remaining([[10,0], [3,5], [5,8]])) # 5
# print(people_remaining([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])) # 17
# print(people_remaining([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])) # 21


#Tema 2
def change(client_list):
  total = 0
  for client in client_list:
    total = (client['quantity'] * 25) - client['bill']
    if total < 0:
      return False
  
  return True

# print(change([{ "quantity": 1, "bill": 25 }, { "quantity": 1, "bill": 25 }, {"quantity": 1, "bill": 25} ])) #True
# print(change([{ "quantity": 1, "bill": 25 }, { "quantity": 1, "bill": 100} ])) #False
# print(change([{ "quantity": 1, "bill": 50 }, { "quantity": 4, "bill": 100} ])) #False
# print(change([{ "quantity": 2, "bill": 50 }, { "quantity": 4, "bill": 100}, {"quantity": 1, "bill": 25} ])) #True

#Tema 3
def add_fracs(f_list):
  for f in f_list:
    parts =  f.split('/')



# add_fracs() #=> ''
# add_fracs(['1/2']) #=> '1/2'
# add_fracs(['1/2', '1/4']) #=> '3/4'
# add_fracs(['1/2', '3/4']) #=> '5/4'
# add_fracs(['2/4', '6/4', '4/4']) #=> '3'
# add_fracs(['2/3', '1/3', '4/6']) #=> '5/3'
# add_fracs(['-2/3', '5/3', '-4/6']) #=> '1/3'


#Tema 4
def persistence(n):
  s = str(n)
  count = 0

  while len(s) == 1:
    sum = 1
    for part in s:
      sum *= int(part)
    
    count += 1
    s = str(sum)
  
  return count

# print(persistence(39)) #3 
# print(persistence(999)) #4 
# print(persistence(4)) #0 

#Tema 4.1
def persistence_rec(n, count = 0):
  s = str(n)

  if len(s) == 1:
    return count
  
  sum = 1

  for part in s:
      sum *= int(part)
  
  return persistence_rec(sum, count + 1)

# print(persistence_rec(39)) #3 
# print(persistence_rec(999)) #4 
# print(persistence_rec(4)) #0

#Tema 5
def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n - 1) + fib(n - 2)

# print(fib(1))  #1
# print(fib(7)) #13
# print(fib(8)) #21

#Tema 5.1
cache = {}
def fib_opt(n):
  if n == 0 or n == 1:
    return n
  
  if n in cache:
    return cache[n]
  
  res = fib_opt(n - 1) + fib_opt(n - 2)

  cache[n] = res

  return res

# print(fib_opt(1))  #1
# print(fib_opt(7)) #13
# print(fib_opt(8)) #21
# print(fib_opt(35)) #9227465


#Tema 5.2
def fib_iter(n):
  first = 0
  second = 1
  for i in range(n):
    first, second = second, first + second 
  return first

# print(fib_iter(1))  #1
# print(fib_iter(7)) #13
# print(fib_iter(8)) #21
# print(fib_iter(35)) #9227465


def reverse(s):
  if len(s) <= 1:
    return s
  return s[-1] + reverse(s[0:-1])

# print(reverse("lol")) #"lol"
# print(reverse("take yourself to higher places")) #"secalp rehgih ot flesruoy ekat"
# print(reverse("Ella te da detalle")) #"ellated ad et allE"
