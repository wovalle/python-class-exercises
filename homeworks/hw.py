def find_max(*nums):
    max = 0
    for i in nums:
        if i > max:
            max = i
    return max


print(find_max(1, 2, 3, 3, 4))
print(find_max(1, 2, 3))
print(find_max(4, 0, 3))
print(find_max(1, 8, 3))
print(find_max(16, 2, 6))


def find_max_hack(*nums):
    return max(nums)


print(find_max_hack(1, 2, 3, 3, 4))
print(find_max_hack(1, 2, 3))
print(find_max_hack(4, 0, 3))
print(find_max_hack(1, 8, 3))
print(find_max_hack(16, 2, 6))


def reverse(str):
    reversed = ''
    for i in range(len(str) - 1, -1, -1):
        reversed += str[i]
    return reversed


def reverse_while(str):
    idx = len(str) - 1
    reversed = ''
    while idx >= 0:
        reversed += str[idx]
        idx -= 1
    return reversed


print(reverse("hello world!"))
print(reverse_while("hello world!"))


def check_range(number, lower, upper):
    return number >= lower and number <= upper


print(check_range(10, 3, 16))
print(check_range(10, 3, 6))
print(check_range(10, 3, 10))
print(check_range(10, 3, -1))
