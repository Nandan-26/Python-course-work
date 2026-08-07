Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=12.3
>>> c="codegnan"
>>> print(a,b,c)
10 12.3 codegnan
>>> print(a,b,c,sep='')
1012.3codegnan
>>> print(a,b,c,sep='',end='\n')
1012.3codegnan
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
>>> print(f'a={} b={} c={}')
SyntaxError: f-string: valid expression required before '}'
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={1} b={2} c={0}'.format(a,b,c))
a=12.3 b=codegnan c=10
