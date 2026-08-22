Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# dict-mut,ordered,dynamic,hetero,unique values only
d={}
type(d)
<class 'dict'>
d=dict()
>>> d[1]=1
>>> d[12.3]=1
>>> d['str']=1
>>> d[(2+3j)]=1
>>> d[(1,2,3,4)]=1
>>> d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d[{1,2,3}]=1
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[{1,2,3}]=1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
>>> d[{1:1,2:2}]=1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d[{1:1,2:2}]=1
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
>>> #as dict is heterogenous but the key doesn't allow muttable datatypes like list,set,dict
>>> 
>>> #values
>>> d[1]=1
>>> d[2]=12.4
>>> 
>>> d[3]='str'
>>> d[4]=2+3j
>>> d[5]=False
>>> d[6]=[1,2,3]
>>> d[7]=(1,2,2,34,5)
>>> d[8]={1,2,3,4}
>>> d[9]={1:2,3:4,5:6}
>>> d
{1: 1, 12.3: 1, 'str': 1, (2+3j): 1, (1, 2, 3, 4): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: False, 6: [1, 2, 3], 7: (1, 2, 2, 34, 5), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
>>> # duplicate values allowed but in keys
>>> 
...  
>>> d[1]=3
>>> d
{1: 3, 12.3: 1, 'str': 1, (2+3j): 1, (1, 2, 3, 4): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: False, 6: [1, 2, 3], 7: (1, 2, 2, 34, 5), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
>>> d[1]=146
>>> d
{1: 146, 12.3: 1, 'str': 1, (2+3j): 1, (1, 2, 3, 4): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: False, 6: [1, 2, 3], 7: (1, 2, 2, 34, 5), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
>>> #key should be unique ,duplicate not allowed for keys
>>> d[10]=None
>>> d
{1: 146, 12.3: 1, 'str': 1, (2+3j): 1, (1, 2, 3, 4): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: False, 6: [1, 2, 3], 7: (1, 2, 2, 34, 5), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}, 10: None}
