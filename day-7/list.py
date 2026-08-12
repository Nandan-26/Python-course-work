Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list() #CONSTRUCTOR
type(l)
<class 'list'>
l=[1,12.3,3i+4j,[1,2,3,4],'hi',(2,3,4),{1:1,2:2}]
SyntaxError: invalid decimal literal
l=[1,12.3,(3i+4j),[1,2,3,4],'hi',(2,3,4),{1:1,2:2
                                          
SyntaxError: invalid decimal literal
l=[1,12.3,3+4j,[1,2,3,4],'hi',(2,3,4),{1:1,2:2}]
                                          
a=[1,2,3]
                                          
b=[4,5,6]
                                          
a+b
                                          
[1, 2, 3, 4, 5, 6]
a*3
                                          
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[567,76,13,433,134,234]
                                          
a[0]
                                          
567
a[::-1]
                                          
[234, 134, 433, 13, 76, 567]
a[::+2]
                                          
[567, 13, 134]
a[-1:-4:-1]
                                          
[234, 134, 433]
76 in a
                                          
True
834797 in a
                                          
False
13 not in a
                                          
False
max(l)
                                          
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'complex' and 'float'
max(a)
                                          
567
min(a)
                                          
13
a.update(13,56)
                                          
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.update(13,56)
AttributeError: 'list' object has no attribute 'update'
a.append(44)
                                          
a
                                          
[567, 76, 13, 433, 134, 234, 44]
a.insert(2,400)
                                          
a
                                          
[567, 76, 400, 13, 433, 134, 234, 44]
a.append(2,3,4)
                                          
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.append(2,3,4)
TypeError: list.append() takes exactly one argument (3 given)
a.extend(2,3,4)
                                          
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.extend(2,3,4)
TypeError: list.extend() takes exactly one argument (3 given)
a.extend([2,3,4])
                                          
a
                                          
[567, 76, 400, 13, 433, 134, 234, 44, 2, 3, 4]
a.append([100,200,300])
                                          
a
                                          
[567, 76, 400, 13, 433, 134, 234, 44, 2, 3, 4, [100, 200, 300]]
a.sorted1()
                                          
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.sorted1()
AttributeError: 'list' object has no attribute 'sorted1'
a.sorted()
                                          
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> a.sort()
...                                           
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.pop()
...                                           
[100, 200, 300]
>>> a
...                                           
[2, 3, 4, 13, 44, 76, 134, 234, 400, 433, 567]
>>> a.sorted()
...                                           
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> a.sort()
...                                           
>>> a
...                                           
[2, 3, 4, 13, 44, 76, 134, 234, 400, 433, 567]
>>> sorted(a)
...                                           
[2, 3, 4, 13, 44, 76, 134, 234, 400, 433, 567]
>>> a.del()
...                                           
SyntaxError: invalid syntax
>>> del(a[7])
...                                           
>>> a
...                                           
[2, 3, 4, 13, 44, 76, 134, 400, 433, 567]
>>> a.clear()
...                                           
>>> a
...                                           
[]
