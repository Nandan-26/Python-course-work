# stringoperations
''' 1.concatenation
    2.Repeatition
    3.indexing
    4.slicing
    5.membership  '''
#conactenation    
s='Codegnan'
l='-Hyderabad'
print(s+l)

#2.
a='Python'
print(a*5)
#3.
print(len(s))
print(s[0])
print(s[1])
print(s[3])
print(s[4])
print(s[5])
#4.
print(s[:])
#note- default  -s[0:len(s):step]
print(s[-1:-9:-1])
print(s[::-1])
#5.
print('c' in s)


# methods
""" len(),chr(),ord(),sorted(),max(),min()"""
print(len(s))
print(ord('c'))
print(max(s))
print(min(s))
print(chr(100))
print(sorted(s))

# case conversions
''' 1.upper()
    2.lower()
    3.swapcase()
    4.capitalize()
    5.casefold()
    6.title() '''

# allingment operators
''' 1.center()
    2.ljust()
    3.rjust()
    4.zfill()'''
print(s.ljust(50,'*'))
print(s.center(50,'*'))
#find(), index(),rfind(),count()
#replace(),maketrans(),translate(),encode(),decode()
print(s.replace('o','1'))
print(s.replace('Code','Hero'))
print(s.maketrans('aeiou','#$%&*'))
