# 1
my_tuple = (5, 10, 15, 20)
print(len(my_tuple))

print(my_tuple[3])

print(my_tuple.count(15))

print(my_tuple)

# 2
colors = ("red", "blue", "green")
colors_list = list(colors)

colors_list.append("yellow")

colors_list.remove("blue")

colors_list.sort()
print(colors_list)

# 3
num = (3, 7, 2, 9, 4)
print(num)

total = sum(num)
print(total)

if total % 2 == 0:
    print("Yig‘indi juft")
else:
    print("Yig‘indi toq")

print(total)

# 4
it = (1, 2, 2, 3, 4, 4, 1)
print(it)

it = list(it)

print(it.sort())
print(it)

# 5
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2
print(t3)

print(sum(t3))

print(t3[-1])

# 6
val = (12, 3, 8, 19, 3, 15)
print(val)

a = max(val)
b = min(val)
print(a, b)

d = a - b

print(d)

# 7
words = ('apple', 'banana', 'cherry', 'date')
print(words)

words = sorted(words, reverse=True)
print(words)

print(words[1::-1])

# 8
a = 10, 20, 30, 40, 50
print(a)

if 30 in a:
    print("bor")
else:
    print("yoq")

print(a.index(30))

print(a)

# 9
nums = (1, 2, 3, 4, 5, 6, 7, 8)

even_nums = tuple(num for num in nums if num % 2 == 0)

count_even = len(even_nums)

print("Juft sonlar:", even_nums)
print("Juft sonlar soni:", count_even)

# 10
data = ((1, 2), (3, 4), (5, 6))
print(data)
result = tuple(item[1] for item in data)

print(result)

# 11
fruits = "apple", "kiwi", 'banana', 'pear'
print(list(fruits))

# 12
num = (-3, 5, -7, 2, -1, 8)
print(list(num))


a = [0 if num < 0 else num for num in num]
print(a)

print(tuple(a))

# 13
score = (2, 4, 6, 8)
print(score)
score = list(score)

for i in range(len(score)):
    score[i] *= 2

score = tuple(score)
print(score)

# 14
r_tuple = 10, 20, 30, 40, 50, 60, 70
print(r_tuple)

a = r_tuple[2:6]
print(a)

print(sum(a))
