




a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# shorthand if
if a > b: print("a is greater than b")
# shorthand if-else
print("A") if a > b else print("B")
# multiple if-else shorthand
print("A") if a > b else print("=") if a == b else print("B")

# logical and
if a > b and c > a:
    print("Both conditions are True")
# logical or
if a > b or a > c:
    print("At least one of the conditions is True")

# nested if-else
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# pass
if b > a:
    pass

# while
idx = 1
while i < 6:
    print(i)
    i += 1

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# while-else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")




# for each
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# for loop through string
for x in "banana":
    print(x)
# for loop with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# for loop with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
# for-continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# for range
for x in range(6):
    print(x)
# for range with start
for x in range(2, 6):
    print(x)
# for range, step
for x in range(2, 30, 3):
    print(x)
# for else
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# for-break
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
# nest for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# for-pass empty loop
for x in [0, 1, 2]:
    pass

# function
def my_function():
    print("Hello from function")

def my_function(fname):
    print("Hello from "+fname)
my_function("Torvalds")
my_function("Linus")

def my_function(fname, lname):
    print(lname+","+fname)
my_function("Chuck", "Strange")

# arbitrary arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Strange", "Torvalds", "Linus")

# keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# arbitrary keyword arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("Brazil")
my_function()

# list as argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# return value(s)
def my_function(x):
    return 5 * x
for x in [3,5,7]:
    print(my_function(x))
print(my_function(11))

# empty function, pass
def myfunction():
    pass

# recursion
def triple_recursion(k):
    if(k > 0):
        result = k + triple_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example:")
triple_recursion(6)

# lambda function
lf = lambda a : a + 10
print(lf(5))

# several arguments
lf = lambda a, b, c : a * b + c
print(lf(5, 6, 3))

# sum of args
lf = lambda a, b, c : a + b + c
print(lf(5, 6, 2))

# another lambda function
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# another lambda function
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# doubler, tripler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

class MyClass:
  x = 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)










