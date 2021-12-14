# letters = ["a", "b", "c"]
# matrix = [[0,1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers =list(range(20))
# chars = list("Hello World")
# print(len(chars))

# # Accessing Itmes
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"     # Modify first value
# print(letters[0])   # first value
# print(letters[-1])  # last value in list
# print(letters[:3])  # first value to 3rd
# print(letters[0:])  # first value to end
# print(letters[:])   # origianal list
# print(letters[::2]) # steps

# # numbers = list(range(20))
# # print(numbers)      # print 0 to 19
# # print(numbers[::2]) # print every other character, step 2
# # print(numbers[::-1])  # print in revers order

# # # List unpacking
# # numbers = [1, 2, 3]
# # first, second, third = numbers  # unpack numbers into variables
# # print(third)
# # numbers = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4]
# # first, second, *other = numbers # uppack unwanted values into other list
# # print(other)
# # print(first)

# # numbers = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 9]
# # first, *other, last = numbers
# # print(first, last)
# # print(other)

# # Looping over lists
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):   # returns enumberate opject index and item
#     print(index, letter)
    
# # Adding or removing items

# # add
# letters.append("d")     # add to end of list
# letters.insert(0, "-")   # add to beginning of list

# print(letters)


# # remove
# letters.pop()       # remove beginning
# print(letters)

# letters.pop(1)      # remove spceific index
# print(letters)

# letters.remove("b")     # remove item "b" (first occourance)
# print(letters)

# del letters [0:3]   # remove range of items

# letters.clear   # clear a list

# # finding items

# letters = ["a", "b", "c"]
# if "d" in letters:
#     print(letters.index("d")) # if 'd' is in lists, printit

# # or

# print(letters.count("d"))   # show how many occouraces of item

# # Sorting list
# numbers = [3, 52, 2, 8, 6]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# print(sorted(numbers))  # RETURN new sorted list
# print(sorted(numbers, reverse=True))

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

# # Lambda Functions
# # items.sort(key=lambda item:expression)
# items.sort(key=lambda item:item[1])
# print(items)

# Map Function
# Transform list into different shape.
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# use lambda for cleaner code
# x =map(lambda item: item[1], items)    
# for item in x:
#     print(item)

# # # convert map item into list

# # prices = list(map(lambda item: item[1], items))
# # print(prices)    

# # #Filter function

# # filtered = list(filter(lambda item: item[1] >= 10, items))
# # print(filtered)

# # # List Comprehensions
# # # [expression for item in items]
# # prices2 = [item[1] for item in items]
# # filtered2 = [item for item in items if item[1] >= 10]
# # print(prices2)
# # print(filtered2)

# # # Zip function - combine list to tuples
# # list1 = [1, 2, 3]
# # list2 = [10, 20, 30]

# # print(list(zip(list1, list2)))
# # # also pass other iterables
# # print(list(zip("abc",list1, list2)))

# # # Stacks
# # # LIFO
# # browsing_session = []
# # browsing_session.append(1)
# # browsing_session.append(2)
# # browsing_session.append(3)
# # print(browsing_session)
# # last = browsing_session.pop()
# # print(last)
# # print(browsing_session)
# # print("redirect", browsing_session[-1])
# # if not browsing_session:
# #     print("")
    
# # Queues
# # Fifo
# from collections import deque
# from typing_extensions import Unpack
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print(empty)
    
# # Tuples - Read only list
# point = (1, 2)
# print(type(point))
# print(point)

# point = (1, 2) + (3, 4)
# print(point)

# point = (1, 2) * 3
# print(point)

# #convert list to tuple
# point = tuple([1, 2, 3])
# print(type(point))
# print(point)

# # get objects
# print(point[0])
# print(point[0:2])

# unpack
point = (1, 2, 3)
x, y, z = point
if 3 in point:
    print("exist")
    
# Swaping variables
# hard way
x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)

# Easy Way
x = 10
y = 11
x,y = y, x
print("x", x)
print("y", y)

# Arrays - better performace for large amounts of data
# check typelist codes
from array import array
numbers = array("i", [1, 2, 3])
print(numbers)

# Sets - remove duplicates
# can't be referenced with index
numbers = [1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first)

print(first | second)   # union of sets
print(first & second)   # what they have in common
print(first - second)   # difference
print(first ^ second)   # remove not in both

if 1 in first:
    print("yes")
    
# Dictornaries - key value pairs
# point = {"X": 1, "Y": 2}
# or dict function
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20

print(point)
print(point.get("a", 0))    # return someting if key does not exist

del point["x"]
print(point)

for key in point:
    print(key, point[key])
    
for key, value in point.items():
    print(key, value)
    
# dictornary comprehensions
# for list
values = [x * 2 for x in range(5)]
print(values)

# or for a set
values = {x * 2 for x in range(5)}
print(values)

# or for a dictionary
values = {x: x * 2  for x in range(5)}
print(values)

# Generator expressions - large amounts of values
# from sys import getsizeof
# values = (x * 2 for x in range(10000))
# print(values)
# for x in values:
#     print(x)
# print("gen:", getsizeof(values)) # show memory use

# Unpacking Operator
numbers = [1, 2, 3]
print(numbers)
print(*numbers) # unpacking operator

values = list(range(5))
print(values)
values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# Dictionaries, use **
first = {"x": 1}
second = {"x": 10, "y":2}
combined = {**first, **second, "z": 1}
print(combined)

