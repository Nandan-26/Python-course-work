Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a*=10
>>> a
100
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> l is m
False
>>> id(l)
2086536542336
>>> id(m)
2086533873856
>>> # is -checks the id's of the objects same or not
>>> m=n
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    m=n
NameError: name 'n' is not defined
>>> n=m
