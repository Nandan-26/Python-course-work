Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='  hello  world   '
s.strip()
'hello  world'
s.lsrtip()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.lsrtip()
AttributeError: 'str' object has no attribute 'lsrtip'. Did you mean: 'lstrip'?
s.lstrip()
'hello  world   '
s.rstrip()
'  hello  world'
s.replace(' ','')
'helloworld'
c="python java mysql flask"                                                                           a
SyntaxError: invalid syntax
c="python java mysql flask"
list(c)
['p', 'y', 't', 'h', 'o', 'n', ' ', 'j', 'a', 'v', 'a', ' ', 'm', 'y', 's', 'q', 'l', ' ', 'f', 'l', 'a', 's', 'k']
list(c).split()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list(c).split()
AttributeError: 'list' object has no attribute 'split'
c.split()
['python', 'java', 'mysql', 'flask']
>>> d=c.split()
>>> "".join(d)
'pythonjavamysqlflask'
>>> " ".join(d)
'python java mysql flask'
>>> d.partition('.')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.partition('.')
AttributeError: 'list' object has no attribute 'partition'
>>> c.partition('.')
('python java mysql flask', '', '')
>>> a="strings.png"
>>> 
>>> a.startwith('str')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
>>> a.startswith('str')
True
>>> a.enswith('.py')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.enswith('.py')
AttributeError: 'str' object has no attribute 'enswith'. Did you mean: 'endswith'?
>>> a.endswith('.py')
False
>>> "strings.png".isupper()
False
>>> "strings.png".islower()
True
>>> "STRINGS.2132434PNG"isupper()
SyntaxError: invalid syntax
>>> "STRINGS.2132434PNG".isupper()
True
>>> "Strings.Png"istitle()
SyntaxError: invalid syntax
>>> "Strings.Png".istitle()
True
>>> "Strings.Png".isalpha()
False
>>> "Strings.Png".isalnum()
False
>>> KeyboardInterrupt
"Strings.Png"istitle()
>>> "Strings.Png".isspace()
False
>>> #
>>> ''' isupper(),islower(),isspace(),istitle(),isalpha(),isalnum() '''
' isupper(),islower(),isspace(),istitle(),isalpha(),isalnum() '
