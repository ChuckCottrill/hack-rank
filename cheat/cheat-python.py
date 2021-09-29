



[f(x) for x in sequence if condition]

# comment
"""
this is a multiline comment
"""

x = 5
s = "Hello, world"
if x > 5:
    print("is {}".format(x))

# convert to type
v = int(3) # = 3
v = float(3) # = 3.0
v = str(3) # v == '3'

# what is type
type(v) # <class 'str'>
if type(v) == type('hello'): print("string")
type([]) # <class 'list'>
type({}) # <class 'dict'>
if type(v) == type([]): print("list")
if type(v) == type({}): print("dict")

myvar = "Chuck"
myVar = "Chuck" # camelcase
MyVar = "Chuck" # pascalcase
MYVAR = "Chuck" # capscase
my_var = "Chuck" # snakecase
_my_var = "Chuck" # leading _
myvar2 = "Chuck"

# multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x, y, z = ("Orange", "Banana", "Cherry")

# assign to multiple variables at once
x = y = z = "Cherry"

# different numbers in tuple,
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

for i in range( len(fruits) ):
    print("[{}] {}".format(i,fruits[i]))

while i < len(fruits):
    print("[{}] {}".format(i,fruits[i]))
    i += 1

# paste tuples together
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply/replicate tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

"""
data types:
str
int, float, complex
list, tuple, range
dict
set, frozenset
bool
bytes, bytearray, memoryview
type() gets the type
"""

s = {"apple", "banana", "cherry"}
fs = frozenset({"apple", "banana", "cherry"})
b = True
b = False

x = b"Hello"
print(x)
#display the data type of x:
print(type(x))
for b in x:
    print("b:",b)

for ch in "banana":
    print(ch) 

import random
print(random.randrange(1, 10))

hw = "Hello, World!"
print(hw.upper())
hw = "Hello, World!"
print(hw.lower())
hw = " Hello, World! "
print(hw.strip()) # returns "Hello, World!"
print(hw.replace("Hello", "Goodbye"))
print(hw.split(",")) # returns ['Hello', ' World!']

# format strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# list constructor
mylist = list(("apple", "banana", "cherry")) # note double round-brackets
print(mylist)
# addressing [included:notincluded]
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[:4])
print(mylist[2:])

if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")

# replace [1:2], one items with two,
mylist[1:2] = ["peach", "watermelon"]
print(mylist)
# replace [1:3], two items with one,
mylist[1:3] = ["watermelon"]
print(mylist)
# insert item(s)
mylist = ["apple", "banana", "cherry"]
mylist.insert(2, "peach")
print(mylist)
mylist.append("orange")
print(mylist)

# extend list
mylist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)
# remove list
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)
# pop/remove item
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
print(mylist)
# remove last item
mylist.pop()
print(mylist)
# remove first item
del mylist[0]
print(mylist)
# clear (empty) list
mylist.clear()
print(mylist)
# delete list
del mylist.clear()
print(mylist)

# loop over list
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)
# loop over list index
for x in range(len(mylist)):
    print(x)
# while loop over list index
idx = 0
while idx < len(mylist):
    print(x)
    idx += 1
# list comprehension
[ print(x) for x in mylist ]

# loop to process list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
afruits = []
for x in fruits:
    if "a" in x:
        afruits.append(x)
print(afruits)

# list comprehension to process list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
afruits = [x for x in fruits if "a" in x]
print(afruits)

newfruit = [x.upper() for x in fruits]
newfruit = ['fruit' for x in fruits]
newfruit = [x if x != "banana" else "orange" for x in fruits]

# sort list of string
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)
# sort list of numeric
mylist = [100, 50, 65, 82, 23]
mylist.sort()
print(mylist)
# reverse sort
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort(reverse = True)
print(mylist)

# complex
z = complex(2, -3)
print(z)
z = complex(1)
print(z)
z = complex()
print(z)
z = complex('5-9j')
print(z)

# create dict(ionary)
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))
empty = dict()
print('empty =', empty)
print(type(empty))
# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)
# keyword argument is passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)
# zip() creates iterable (Python 3)
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)

# create dict using {}
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)
# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)
# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)

# frozenset manipulations
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
D = frozenset([5, 6])
# copy a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)
# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})
# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})
# difference
print(A.difference(B))  # Output: frozenset({1, 2})
# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
# isdisjoint() method
print(A.isdisjoint(D))  # Output: True
# issubset() method
print(D.issubset(B))  # Output: True
# issuperset() method
print(B.issuperset(D))  # Output: True

numbers = [1, 2, 3]
result = isinstance(numbers, list)
print(numbers,'instance of list?', result)
result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)
result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)
number = 5
result = isinstance(number, list)
print(number,'instance of list?', result)
result = isinstance(number, int)
print(number,'instance of int?', result)

# string
seq_string = 'Python'
# tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# range
seq_range = range(5, 9)
# list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_string)))
print(list(reversed(seq_tuple)))
print(list(reversed(seq_range)))
print(list(reversed(seq_list)))

# vowels list
mylist = ['e', 'a', 'u', 'o', 'i']
print(sorted(mylist))
# string
mylist = 'Python'
print(sorted(mylist))
# vowels tuple
mylist = ('e', 'a', 'u', 'o', 'i')
print(sorted(mylist))
# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))
# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))
# frozenset
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))

# take the second element for sort
def take_second(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sorted_list = sorted(random, key=take_second)
# print list
print('Sorted list:', sorted_list)

# see: https://www.programiz.com/python-programming/methods/built-in/sorted

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')

d1 = Dog()

# sort list
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(mylist)
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort(key = str.lower)
print(mylist)
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.reverse()
print(mylist)

# copy list with copy()
mylist = ["apple", "banana", "cherry"]
mylist = mylist.copy()
print(mylist)
# copy list with list()
mylist = ["apple", "banana", "cherry"]
mylist = list(mylist)
print(mylist)

# join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# join lists using append()
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
# join lists using extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

myset = {"apple", "banana", "cherry"}
myset.add("orange")
myset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)
myset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
myset.update(mylist)

myset = {"apple", "banana", "cherry"}
myset.remove("banana")
myset = {"apple", "banana", "cherry"}
myset.discard("banana")
myset = {"apple", "banana", "cherry"}
x = myset.pop()

thisset = {"apple", "banana", "cherry"}
thisset.clear()
thisset = {"apple", "banana", "cherry"}
del thisset
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)

















