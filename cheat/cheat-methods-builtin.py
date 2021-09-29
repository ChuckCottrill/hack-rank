

abs(num)
any(iterable)
all(iterable)
ascii(object)
bin(num)
bool(value)
bytearray() # bytearray(source, encoding, errors), mutable
bytes() # bytes(source, encoding, errors), immutable
callable(object)
chr(num) # num in [0,1_114_111], returns unicode codepoint
compile() # compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
complex() # complex([real[, imag]])
hasattr() # hasattr(object, name)
getattr() # getattr(object, name[, default])
delattr() # delattr(object, name)
setattr() # setattr(object, name, value)
dict() # class dict(**kwarg)
    # class dict(mapping, **kwarg)
    # class dict(iterable, **kwarg)
list() # list([iterable])
set() # set(iterable)
tuple() # tuple(iterable)
dir() # dir([object])
divmod() # divmod(x,y)
enumerate() # enumerate(iterable, start=0)
eval() # eval(expression, globals=None, locals=None)
exec() # exec(object, globals, locals)
float() # float([x])
format() # format(value[, format_spec])
    # see: https://www.programiz.com/python-programming/methods/built-in/format
frozenset() # frozenset([iterable])
help() # help(object)
hex() # hex(x)
oct() # oct(x)
ord() # ord(ch)
hash() # hash(object)
input() # input([prompt])
id() # id(object)
isinstance() # isinstance(object, classinfo)
int() # int(x=0, base=10)
issubclass() # issubclass(class, classinfo)
iter() # iter(object, sentinel)
len() # len(s)
# to find the largest item in an iterable
max() # max(iterable, *iterables, key, default)
# to find the largest item between two or more objects
max() # max(arg1, arg2, *args, key)
# to find the smallest item in an iterable
min() # min(iterable, *iterables, key, default)
# to find the smallest item between two or more objects
min() # min(arg1, arg2, *args, key)S
filter() # filter(function, iterable)
map() # map(function, iterable, ...)
next() # next(iterator, default)
memoryview() # memoryview(object)
object() # object()
open() # open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
pow() # pow(x, y, z)
print() # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
property() # property(fget=None, fset=None, fdel=None, doc=None)
range() # range(stop)
    # range(start, stop[, step])
repr() # repr(obj)
reversed() # reversed(seq)
round() # round(number, ndigits)
slice() # slice(start, stop, step)
sorted() # sorted(iterable, key=None, reverse=False)
    # sorted(iterable, key=len)
str() # str(object, encoding='utf-8', errors='strict')
sum() # sum(iterable, start)
type() # type(object)
    # type(name, bases, dict)
vars() # vars(object)
zip() # zip(*iterables)
super() # super()
__import__() # __import__(name, globals=None, locals=None, fromlist=(), level=0)

globals() # globals() dictionary of global symbol table
locals() # locals() dictionary of global symbol table

classmethod() # classmethod(function) (unpythonic)
@classmethod
def func(cls, args...)
# see: https://www.programiz.com/python-programming/methods/built-in/classmethod
staticmethod() # staticmethod(function)
@staticmethod
def func(args, ...)
# see: https://www.programiz.com/python-programming/methods/built-in/staticmethod


