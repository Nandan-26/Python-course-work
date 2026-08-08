Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input
a=input()
5
a
'5'
type(a)
<class 'str'>
a=int(input())
10
a
10
type(a)
<class 'int'>
a=float(input())
10.678
a
10.678
type(a)
<class 'float'>
#list
names=input().split()
nandan ram krishna
names
['nandan', 'ram', 'krishna']
names=tuple(input().split())
nandan ram krishna
names
('nandan', 'ram', 'krishna')
cousre='python-java-css-flask'
course.split('-')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    course.split('-')
NameError: name 'course' is not defined. Did you mean: 'cousre'?
cousre.split('-')
['python', 'java', 'css', 'flask']
tuple(cousre.split('-'))
('python', 'java', 'css', 'flask')
set(cousre.split('-'))
{'flask', 'java', 'css', 'python'}
names=set(input().split())
names=set(input().split())
nandan ram krishna
SyntaxError: invalid syntax
names=set(input().split())
nandan ram krishna
names
{'nandan', 'ram', 'krishna'}
{'nandan', 'ram', 'krishna'}
{'nandan', 'ram', 'krishna'}


#map function has two parameters one is what to convert and ,other is how to we have to convert - map(int,input().split())
#map while iterate the list and conert each and every element to int or float on user requirement
marks=intput().split()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    marks=intput().split()
NameError: name 'intput' is not defined. Did you mean: 'input'?
marks=input().split()
36 45 56 39 54
marks
['36', '45', '56', '39', '54']
''' here we got marks as list of str so if we want to convert them to int we have no method specifically , so we use map to iterate through out the list of the string and convert each and everyvalue into int'''
' here we got marks as list of str so if we want to convert them to int we have no method specifically , so we use map to iterate through out the list of the string and convert each and everyvalue into int'
map(int,marks)
<map object at 0x000002CF0FE985C0>
list(map(int,marks))
[36, 45, 56, 39, 54]
s=map(int,marks)
s
<map object at 0x000002CF0FE985C0>
s=list(map(int,marks))
s
[36, 45, 56, 39, 54]
a,b=[1,2]
a
1
b
2
a,b,c=(1,23.4,"Str")
a
1
b
23.4
c
'Str'
email,password=input("enter the email and password: ").split()
enter the email and password: nandan@codegnan.com 12345
email
'nandan@codegnan.com'
password
'12345'
int(password)
12345
name,marks=list(map(int,input().split()))
nandan 99
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name,marks=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'nandan'
45 67
SyntaxError: invalid syntax
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
a,b,c=list(map(int,input().split()))
1 2 3 4
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: too many values to unpack (expected 3, got 4)
a,b,c,d=list(map(int,input().split()))
1 2
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,b,c,d=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 4, got 2)
name,marks=input().split

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    name,marks=input().split

... TypeError: cannot unpack non-iterable builtin_function_or_method object
>>> name,marks=input().split()
nandan 83
>>> name
'nandan'
>>> marks
'83'
>>> s=eval(input())
2+3j
>>> s
(2+3j)
>>> type(s)
<class 'complex'>
>>> s=eval(input())
[1,2,3,4]
>>> s
[1, 2, 3, 4]
>>> s=eval(input())
253 "str"
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s=eval(input())
  File "<string>", line 1
    253 "str"
        ^^^^^
SyntaxError: invalid syntax
>>> s=eval(input())
2 3 4
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s=eval(input())
  File "<string>", line 1
    2 3 4
      ^
SyntaxError: invalid syntax
>>> s=eval(input().split())
2 3 4
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> s=eval(input())
{1:2,3:4,5:6}
>>> s
{1: 2, 3: 4, 5: 6}
>>> s=eval(input())
{"names":"eswar","marks":34}
>>> s
{'names': 'eswar', 'marks': 34}
