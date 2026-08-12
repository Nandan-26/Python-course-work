Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'''A tuple is an ordered, immutable collection used to store multiple values in a single variable. 
Tuples are created using parentheses ( ) or tuple() '''
'A tuple is an ordered, immutable collection used to store multiple values in a single variable. \nTuples are created using parentheses ( ) or tuple() '

t=
SyntaxError: invalid syntax
t=()
t=tuple()
t=(1)#this not coorect way as it become int
t
1
type(t)
<class 'int'>
t=(1,)#comma should be written explicitly
t=(1,1,1)
t=(1,23.4,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[len(t)-1]
True
lent(t)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lent(t)
NameError: name 'lent' is not defined. Did you mean: 'len'?
len(t)
8
t[::]
(1, 23.4, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[2:8]
('str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[-2:-4:]
()
t[-2:-4]
()
t[-2:-4:-1]
({1: 1, 2: 2}, {1, 2, 3})
t[-4:-2]
((1, 2, 3), {1, 2, 3})
t[-3:-1]
({1, 2, 3}, {1: 1, 2: 2})
1 in t
True
5 in t
False
#No—tuples don’t have a sort() method because they’re immutable.

#If you want to “sort” a tuple, convert it to a list, sort, then convert back:


sorted(t)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t=(1,2,3,4,5,6,7,8,9,10)
sorted
<built-in function sorted>

sorted(t)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t=(1,2,3[1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t=(1,2,3[1,2,3,4])
TypeError: 'int' object is not subscriptable
t=(1,2,3,[1,2,3,4])
t[3].append(5)
t
(1, 2, 3, [1, 2, 3, 4, 5])
t[3].insert(1,5)
t
(1, 2, 3, [1, 5, 2, 3, 4, 5])
t[3].pop()
5
t[3].del()
SyntaxError: invalid syntax
del(t[3])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    del(t[3])
TypeError: 'tuple' object doesn't support item deletion
#  imortant
s= set()
type(s)
<class 'set'>
s={}
type(s)
<class 'dict'>
# so we have to take empty set by using set constructor
s={1, 23.4, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True}
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s={1, 23.4, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s={1, 23.4, 'str', (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True}
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s={1, 23.4, 'str', (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True}
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s={1, 23.4, 'str', (1, 2, 3),
   , {1: 1, 2: 2}, True}
SyntaxError: invalid syntax
s={1, 23.4, 'str', (1, 2, 3),{1: 1, 2: 2}, True}
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s={1, 23.4, 'str', (1, 2, 3),{1: 1, 2: 2}, True}
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s={1, 23.4, 'str', (1, 2, 3), True}
# as we can observe set is heterogenous but not allow the list,set, dict elements as it cantake only immutable data type elemnts as its elemnt
a={1,2,3}
b={3,4,5}
a | b
{1, 2, 3, 4, 5}
a & b
{3}
a - b
{1, 2}
a ^ b
{1, 2, 4, 5}
# subset <=
a<=b
False
#superset >=
a>=b
False
a.isdisjoint(b)
False
sorted(a)
[1, 2, 3]
\
max(a,b)
{1, 2, 3}
max(a)
3
max(b)
5
max(b,*[1,2*3]}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
max(b,*[1,2*3])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    max(b,*[1,2*3])
TypeError: '>' not supported between instances of 'int' and 'set'
max(b,a)
{3, 4, 5}
max(a.union(b))
5
>>> a.add(50)
>>> a
{1, 2, 3, 50}
>>> max(b,a)
{3, 4, 5}
>>> max(b|a)
50
>>> a
{1, 2, 3, 50}
>>> a.add(100)
>>> a.add([10,40,50])
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.add([10,40,50])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> a.add({10,40,50})
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.add({10,40,50})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> a.update({10,40,50})
>>> a
{1, 2, 3, 100, 40, 10, 50}
>>> a.pop()
1
>>> a.pop()
2
>>> a.pop()
3
>>> a
{100, 40, 10, 50}
>>> a.remove(100)
>>> a
{40, 10, 50}
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
>>> a.remove(500)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.remove(500)
KeyError: 500
>>> a.discard(10)
>>> a
{40, 50}
>>> a.discard(7000)
>>> a
{40, 50}
>>> #discard doesn't return error even the element doen't present on the set
