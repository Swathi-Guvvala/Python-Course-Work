Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="swathi"
a.startswith("i")
False
a.startswith("s")
True
a.endswith("z")
False
a.endswith("i")
True
a.isupper()
False
"z".isupper()
False
"A".isupper()
True
"s".islower()
True
" ".isspace()
True
"    *".isspace()
False
"swathi".isalpha()
True
"swathi9".isalpha()
False
"swathi124".isalnum()
True
"swathi&".isalnum()
False
"Swathi".istitle()
True
"swathi".istitle()
False
"swathi".isidentifier()
True
"swathi@".isidentifier()
False
"1234".isdecimal()
True
"1234".isdigit()
True
"1234".isnumeric()
True
"123.4".isdigit()
False
"swathi".split()
['swathi']
"swathi".split(",")
['swathi']
"swathi".split(',')
['swathi']
"a,b,c,d".split('_')
['a,b,c,d']
"a,b,c".rsplit(",")
['a', 'b', 'c']
"swathi".rsplit(",")
['swathi']
s="swathi parvathi bhavani"
s.splitlines()
['swathi parvathi bhavani']
s.splitline(",")
s.splitlines(",")
['swathi parvathi bhavani']
"amma".join(s)
'sammawammaaammatammahammaiamma ammapammaaammarammavammaaammatammahammaiamma ammabammahammaaammavammaaammanammai'
s="abcd"
"*".join(s)
'a*b*c*d'
s="swathi"
"amma*".join(s)
'samma*wamma*aamma*tamma*hamma*i'
s="swathi"
s.partition("a")
('sw', 'a', 'thi')
s.partition("h")
('swat', 'h', 'i')
s.rpartition("h")
('swat', 'h', 'i')
s.rpartition("s")
('', 's', 'wathi')
s="hello"
s.encode()
b'hello'
b'hello'.decode()
'hello'
lst=[1,2,2,3,4,5,6]
lst
[1, 2, 2, 3, 4, 5, 6]
lst=[2,True,"swathi",[223,24],(2,4,500),{23,34},{3:56}]
>>> lst
[2, True, 'swathi', [223, 24], (2, 4, 500), {34, 23}, {3: 56}]
>>> lst1=[1,2,3]
>>> lst2=[4,5,7]
>>> lst1+lst2
[1, 2, 3, 4, 5, 7]
>>> lst1*9
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> lst1[0]
1
>>> lst[2]
'swathi'
>>> lst1[2]
3
>>> lst1[::-1]
[3, 2, 1]
>>> "3"in lst1
False
>>> 5 in lst1
False
>>> 1 in lst1
True
>>> 9 not in lst1
True
>>> len(lst1)
3
>>> sorted(lst1)
[1, 2, 3]
>>> max(lst1)
3
>>> min(lst1)
1
>>> lst=[34,"swathi",7,9,78]
>>> id(lst)
2163958547904
>>> lst.append("swathi")
>>> lst.extend("swathi,bhavani")
>>> lst
[34, 'swathi', 7, 9, 78, 'swathi', 's', 'w', 'a', 't', 'h', 'i', ',', 'b', 'h', 'a', 'v', 'a', 'n', 'i']
>>> lst.extend(["swathi,bhavani"])
>>> lst
[34, 'swathi', 7, 9, 78, 'swathi', 's', 'w', 'a', 't', 'h', 'i', ',', 'b', 'h', 'a', 'v', 'a', 'n', 'i', 'swathi,bhavani']
>>> lst.insert(0,"parvathi")
>>> lst
['parvathi', 34, 'swathi', 7, 9, 78, 'swathi', 's', 'w', 'a', 't', 'h', 'i', ',', 'b', 'h', 'a', 'v', 'a', 'n', 'i', 'swathi,bhavani']
