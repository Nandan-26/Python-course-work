 '''                       DATA TYPES
INTEGERS-int,float,complex
'''
# when ever the change results in change of object reference also then it is immutable
# object changed but object reference doesn't changed -mutable
#ordered-same order as user given (not sorted ordered)
'''sequenctial data types - str,list,tuple'''
#str - it is immutable ,and we observe every where as it is collection of characters enclosed in '' or" " quotes.
s="Codegnan"
id(s)
2136565989872
s+="python"
id(s)
2136561940784
#observe s reference or memory location is changed
#list - it is muttable,dynamiclly sized,heterogenous,ordered(same order as user given),duplicates allowed
l=[1,2,3,4,15.3,'hello world']
l
[1, 2, 3, 4, 15.3, 'hello world']
id(l)
2136534993856
l.append(356)
l
[1, 2, 3, 4, 15.3, 'hello world', 356]
id(l)
2136534993856
l.append([1,1,1])
l
[1, 2, 3, 4, 15.3, 'hello world', 356, [1, 1, 1]]
print(type(l))
<class 'list'>
                        
#tuple-immuttable ,dynamically sized,ordered,allow duplicates,heterogenous
#example - when ever dealing with fixed axes like longitude ,latitude in google maps etc
t=(1,2,3,1,1,4)
t
(1, 2, 3, 1, 1, 4)
s=(6,7,"string")
print(s+t)
(6, 7, 'string', 1, 2, 3, 1, 1, 4)
id(s)
2136564842560
s+=t
print(s)
(6, 7, 'string', 1, 2, 3, 1, 1, 4)
id(s)
2136563152064




#  set ,dict are mapping datatypes
''' set- muttable,doesn't allow duplicates,dynamically sized,heterogenous,unordered.
 example-  instagram followers as unordered,muttable,dynamically sized ,doen't allow dupplicate followers.
 **dict- collection of data in key and pair value ,enclosed in parenthesis{}-{key:pair}
 #dict - it is muttable,dynamiclly sized,heterogenous,ordered(same order as user given),duplicates allowed.
 '''
#**frozen set**
s=frozenset({1,1,1,116,18,2,3})
s
frozenset({1, 2, 3, 18, 116})
print(type(s))
<class 'frozenset'>
s={1, 2, 3, 18, 116}
s
{1, 2, 3, 18, 116}
print(type(s))
<class 'set'>
s=(1, 2, 3, 18, 116)
s
(1, 2, 3, 18, 116)
print(type(s))
<class 'tuple'>
s=({1, 2, 3, 18, 116})
s
{1, 2, 3, 18, 116}
print(type(s))
<class 'set'>




#boolean
#bool-True ,False

a=True
a
True
type(a)
<class 'bool'>
b=False
s=a+b
type(s)
<class 'int'>
type(a),type(b)
(<class 'bool'>, <class 'bool'>)
f= None
f
type(f)
<class 'NoneType'>
