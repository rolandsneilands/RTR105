Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print __builtins__.__doc__
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print (__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print __builtins__.__doc

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print __builtins__.__doc
AttributeError: 'module' object has no attribute '__doc'
>>> abs(10)
10
>>> abs(-10)
10
>>> a = abs(-10)
>>> vars
<built-in function vars>
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> a
20
>>> a
20
>>> a * b

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a * b
NameError: name 'b' is not defined
>>> a = 10
>>> a
10
>>> print a.__doc__
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> type(a)
<type 'int'>
>>> print b.__doc__

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print b.__doc__
NameError: name 'b' is not defined
>>> b = 1.5
>>> print b.__doc__
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
>>> vars()
{'a': 10, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(b)
<type 'float'>
>>> vars(a)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    vars(a)
TypeError: vars() argument must have __dict__ attribute
>>> type(a)
<type 'int'>
>>> b
1.5
>>> print b.__doc__
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
>>> c = D

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c = D
NameError: name 'D' is not defined
>>>  C = 'D'
 
  File "<pyshell#32>", line 1
    C = 'D'
    ^
IndentationError: unexpected indent
>>> c = 'D'
>>> print c.__doc__
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
>>> vars()
{'a': 10, 'c': 'D', 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(c)
<type 'str'>
>>> 
