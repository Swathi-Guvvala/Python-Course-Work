Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,4,5,6,7,7,7,8}
s
{1, 2, 3, 4, 5, 6, 7, 8}
len(s)
8
max(s)
8
min(s)
1
sorted(s)
[1, 2, 3, 4, 5, 6, 7, 8]
sum(s)
36
any(s)
True
all(s)
True
s={1,2,4,0,0}
s
{0, 1, 2, 4}
any(s)
True
all(s)
False
s={1,2,3,4,5,6,7,7,7,8}
s
SyntaxError: multiple statements found while compiling a single statement
s
{0, 1, 2, 4}
s.add(45)
s
{0, 1, 2, 4, 45}
s.update({78,90,99})
s
{0, 1, 2, 99, 4, 45, 78, 90}
s.add(256)
s
{0, 1, 2, 99, 4, 256, 45, 78, 90}
s.pop()
0
s.pop()
1
s.remove(99)
s
{2, 4, 256, 45, 78, 90}
s.discard(256)
s
{2, 4, 45, 78, 90}
s.discard(2000)
s
{2, 4, 45, 78, 90}
#here discard handle the error where as remove cannot handle the error
s.clear()
s
set()
s.add(256)
s.update({56,89,90,987,999,7890,8907,8970})
s
{256, 999, 8970, 8907, 7890, 56, 89, 90, 987}
a=s
a.add(90)
s
{256, 999, 8970, 8907, 7890, 56, 89, 90, 987}
a
{256, 999, 8970, 8907, 7890, 56, 89, 90, 987}
# this is deep copy here effecting s and a
c=a.copy()
c
{256, 999, 8970, 8907, 7890, 56, 89, 90, 987}
c.add(45)
c
{256, 999, 8970, 8907, 45, 7890, 56, 89, 90, 987}
a
{256, 999, 8970, 8907, 7890, 56, 89, 90, 987}
# here it is shallow copy not effecting a updating only c
dict={}
type(d)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    type(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
dict={}
type(dict)
<class 'dict'>
d={1:2,2:3}
d
{1: 2, 2: 3}
d=
SyntaxError: invalid syntax

d={}
d[1]="int"
d
{1: 'int'}
d[2.2]="float"
d
{1: 'int', 2.2: 'float'}
d[2+3j]="complex"
d
{1: 'int', 2.2: 'float', (2+3j): 'complex'}
d[False]="bool"
d
{1: 'int', 2.2: 'float', (2+3j): 'complex', False: 'bool'}
d["str"]="swathi"
d
{1: 'int', 2.2: 'float', (2+3j): 'complex', False: 'bool', 'str': 'swathi'}
d[(1,2,3)]="tuple"
d
{1: 'int', 2.2: 'float', (2+3j): 'complex', False: 'bool', 'str': 'swathi', (1, 2, 3): 'tuple'}
d[[1,2,3]]="list"
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d[[1,2,3]]="list"
TypeError: unhashable type: 'list'
d({1,2,3}]="set"
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
d[{1,2,3,4}]="set"
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d[{1,2,3,4}]="set"
TypeError: unhashable type: 'set'
d[{1:1,2:2}]="dict"
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d[{1:1,2:2}]="dict"
TypeError: unhashable type: 'dict'
# here key accept only mutable elements when we enter immutable elements it give  type error
d[1]=56
d
{1: 56, 2.2: 'float', (2+3j): 'complex', False: 'bool', 'str': 'swathi', (1, 2, 3): 'tuple'}
#here keys cannot be duplicates
d={}
d[1]=1
d[2]=89.9
d[3]=2+3j
d[4]=True
d[5]="swathi"
d[6]=[1,2]
d[7]=(1,2)
d[8]={1,2}
d[9]={1:2,2:2}
d
{1: 1, 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}}
d[10]=1
d[11]=1
d
{1: 1, 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1}
# here values has no condition values can be anything and duplicates also allow for values
\
d
{1: 1, 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1}
d[1]
1
d[3]
(2+3j)
d[9]
{1: 2, 2: 2}
d[12]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    d[12]
KeyError: 12
# to get ride of keyError we use get
d.get(12)
d.get(12,"key is notfound")
'key is notfound'
d.get(1)
1
d.get(9)'
SyntaxError: unterminated string literal (detected at line 1)
d.get(9)
{1: 2, 2: 2}
d.get(8)
{1, 2}
d.get(7)
(1, 2)
# membership op is for keys only
d
{1: 1, 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1}
1ind
SyntaxError: invalid syntax
1 in d
True
23.4 in d
False
23.4 not in d
True
d
{1: 1, 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1}
d[1]="int"
d
{1: 'int', 2: 89.9, 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1}
d[2]="float"
d[12]=1900
d[13]=990
d[14]="swathi"
d[15]=980
d
{1: 'int', 2: 'float', 3: (2+3j), 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
d.update({1:"swathi",2:"parvathi",3:"bhavani"})
d
{1: 'swathi', 2: 'parvathi', 3: 'bhavani', 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
d.update({16:900.17:90})
SyntaxError: invalid syntax
d.update({16:900,17:90})
d
{1: 'swathi', 2: 'parvathi', 3: 'bhavani', 4: True, 5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980, 16: 900, 17: 90}
d.popitem()
(17, 90)
d.popitem()
(16, 900)
d.pop(1)
'swathi'
d.pop(2)
'parvathi'
del d[3]
del d[4]
d
{5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
d.clear()
d
{}
d={5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
d
{5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
d.keys()
dict_keys([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
d.values()
dict_values(['swathi', [1, 2], (1, 2), {1, 2}, {1: 2, 2: 2}, 1, 1, 1900, 990, 'swathi', 980])
d.items()
dict_items([(5, 'swathi'), (6, [1, 2]), (7, (1, 2)), (8, {1, 2}), (9, {1: 2, 2: 2}), (10, 1), (11, 1), (12, 1900), (13, 990), (14, 'swathi'), (15, 980)])
sorted(d)
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
max(d)
15
min(d)
5
>>> len(d)
11
>>> c=d.copy()
>>> c
{5: 'swathi', 6: [1, 2], 7: (1, 2), 8: {1, 2}, 9: {1: 2, 2: 2}, 10: 1, 11: 1, 12: 1900, 13: 990, 14: 'swathi', 15: 980}
>>> d=dict.frromkeys(["a","b","c","d"],o)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    d=dict.frromkeys(["a","b","c","d"],o)
AttributeError: 'dict' object has no attribute 'frromkeys'. Did you mean: 'fromkeys'?
>>> d=dict.fromkeys(["a","b","c","d"],o)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    d=dict.fromkeys(["a","b","c","d"],o)
NameError: name 'o' is not defined
>>> d=dict.fromkeys(["a","b","c","d"],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
>>> d.setdefault("a")
0
>>> d.setdefault("h")
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None}
>>> d.setdefault("k")
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None, 'k': None}
>>> d.setdefault("j",5)
5
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None, 'k': None, 'j': 5}
>>> d.setdefault("c",1)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': None, 'k': None, 'j': 5}
>>> s=frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> type(s)
<class 'frozenset'>
>>> min(s)
1
>>> len(s)
4
>>> max(s)
4
>>> sorted(s)
[1, 2, 3, 4]
>>> 1 in s
True
>>> 45 not in s
True
