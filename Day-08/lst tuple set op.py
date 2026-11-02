Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> lst=[23,34,45,56,67,89,90,98,87,76]
>>> lst
[23, 34, 45, 56, 67, 89, 90, 98, 87, 76]
>>> lst.pop()
76
>>> lst.pop()
87
>>> lst.pop(45)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lst.pop(45)
IndexError: pop index out of range
>>> lst.pop(1)
34
>>> lst.pop(9)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lst.pop(9)
IndexError: pop index out of range
>>> lst.pop(5)
90
>>> lst.remove(98)
>>> lst
[23, 45, 56, 67, 89]
>>> lst.remove(56)
>>> del lst[0]
>>> lst
[45, 67, 89]
>>> del lst[1]
>>> lst
[45, 89]
>>> lst.clear()
>>> lst
[]
>>> lst=[23,34,45,56,67,89,90,98,87,76]
>>> lst
[23, 34, 45, 56, 67, 89, 90, 98, 87, 76]
>>> lst.count(89)
1
>>> lst.index(89)
5
>>> sorted(lst)
[23, 34, 45, 56, 67, 76, 87, 89, 90, 98]
>>> lst.sort()
>>> lst
[23, 34, 45, 56, 67, 76, 87, 89, 90, 98]
>>> lst.reverse()
>>> lst
[98, 90, 89, 87, 76, 67, 56, 45, 34, 23]
>>> lst.sort(reverse=True)
>>> lst
[98, 90, 89, 87, 76, 67, 56, 45, 34, 23]
a=[12,13,14]
a=b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
a=[12,13,14]
b=a
b.append(989)
b
[12, 13, 14, 989]
a
[12, 13, 14, 989]
c=a.copy()
c
[12, 13, 14, 989]
c.append(29)
c
[12, 13, 14, 989, 29]
a
[12, 13, 14, 989]
#0,0.0,"",[],(),set(),{} are false values
a=[23,45,67,89,0]
any(a)
True
all(a)
False
a=[0,0.0,False,[],{},set()]
any(a)
False
all(a)
False
a=[0,0.0,False,[],{},set(),12]
any(a)
True
all(a)
False
a.sum()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.sum()
AttributeError: 'list' object has no attribute 'sum'
sum(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sum(a)
TypeError: unsupported operand type(s) for +: 'float' and 'list'
sum(c)
1057
c.sum()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c.sum()
AttributeError: 'list' object has no attribute 'sum'
sum(b)
1028
tuple=()
tuple=tuple()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tuple=tuple()
TypeError: 'tuple' object is not callable
t=tuple()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t=tuple()
TypeError: 'tuple' object is not callable
t=(1,23,34,45)
t
(1, 23, 34, 45)
type(t)
<class 'tuple'>
len(t)
4
t=1,2,3,4,5,6,7
type(t)
<class 'tuple'>
t=(1)
type(t)
<class 'int'>
t=(1,)
type(t)
<class 'tuple'>
t
(1,)
t=(1,23.4,1,1,1,1,1)
t
(1, 23.4, 1, 1, 1, 1, 1)
t=(1,23.4,True,2+3j,{1:98},[23,45],(78,)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
t=(1,23.4,True,2+3j,{1:98},[23,45],(78,))
t
(1, 23.4, True, (2+3j), {1: 98}, [23, 45], (78,))
t=tuple()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t=tuple()
TypeError: 'tuple' object is not callable
t=(11,2,3,45,54)
a,b,c,d,e=t
a
11
b
2
c
3
d
45
e
54
a,b,c,d,e=(1,2,3,4,5)
a
1
b
2
c
3
d
4
e
5
t=(1,23.4,True,2+3j,{1:98},[23,45],(78,))
t
(1, 23.4, True, (2+3j), {1: 98}, [23, 45], (78,))
t.count(1)
2
t.index(True)
0
t[-2]
[23, 45]
t[-2].append(98)
t
(1, 23.4, True, (2+3j), {1: 98}, [23, 45, 98], (78,))
#we can modify mutable elements inside the tuple but we canot modify tuple the length of the tuple should be same from start to end
a=(1,2,3,4,4)
b=(1,2,3,4,4)
a+b
(1, 2, 3, 4, 4, 1, 2, 3, 4, 4)
a*8
(1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4)
t=(1,23.4,True,2+3j,{1:98},[23,45],(78,))
t
(1, 23.4, True, (2+3j), {1: 98}, [23, 45], (78,))
t[0]
1
t[-1]
(78,)
t[4:6]
({1: 98}, [23, 45])
1 in t
True
23.4 in t
True
456 in t
False
567 not in t
True
2+3j not in t
False
a=(1,2,3,4,5,6,7)
len(a)
7
max(a)
7
min(a)
1
sorted(a)
[1, 2, 3, 4, 5, 6, 7]
# sorted function always gives list format as end result
a.count(1)
1
a.index(7)
6
sum(a)
28
any(a)
True
all(a)
True
a=(0,1,2)
any(a)
True
all(a)
False
a=set()
type(a)
<class 'set'>
a={1,2,3,4}
a
{1, 2, 3, 4}
# set is unordered,uniq elements,heterogenous data(allows only immutable data types),mutable
a=set()
a.add(9)
a
{9}
a.add(23.4)
a
{9, 23.4}
a.add(True)
a.add(23+3j)
a
{(23+3j), 9, True, 23.4}
a.add("swathi")
a
{(23+3j), True, 'swathi', 9, 23.4}
a.add((1,2,3,4))
a
{(23+3j), True, 'swathi', 9, (1, 2, 3, 4), 23.4}
a.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    a.add([1,2,3])
TypeError: unhashable type: 'list'
#we get TypeError because set canot allow mutable elements
a.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a.add({1,2,3})
TypeError: unhashable type: 'set'
a.add({1:2,2:3})
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a.add({1:2,2:3})
TypeError: unhashable type: 'dict'
a
{(23+3j), True, 'swathi', 9, (1, 2, 3, 4), 23.4}
a={1,2,3,4}
b={3,4,5,6,7}
1 in a
True
4 not in b
False
4 not in a
False
5 not in a
True
a|b
{1, 2, 3, 4, 5, 6, 7}
a&b
{3, 4}
a^b
{1, 2, 5, 6, 7}
a isdisjoint(b)
SyntaxError: invalid syntax
a.isdisjoint(b)
False
a-b
{1, 2}
b-a
{5, 6, 7}
a.isdisjoint({78,90})
True
a.issubset(b)
False
a.issuperset(b)
False
a.issuperset({23,24})
False
a.issubset({56,567})
False
a.issuperset({89,98})
False
a.issubset({23})
False
{2}.issubset(a)
True
{98,97}.issuperset(a)
False
