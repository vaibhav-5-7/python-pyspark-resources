1. Datatypes in Python:
==================================
Datatypes in python are categorized into 5 broad category:
================================================================
i. Numeric Datatype:
==========================
a. Integer (+5,0,-5).
b. Float (1.25,1.00,2.3).
c. complex no (a+ib,3+2i).

ii. Sequence Datatype:
============================
a. List: 
================
my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
print("Datatype of list is: ",type(my_list))
o/p:
======
Datatype of list is:  <class 'list'>

b. Tuple:
===============
t1 = (1,2,3,4,5)
print("Datatype of tuple is: ",type(t1))
o/p:
==========
Datatype of tuple is:  <class 'tuple'>

c. String:
=====================
str1 = "hello"
print("Datatype of string is: ",type(str1))
o/p:
========
Datatype of string is:  <class 'str'>

iii. Boolean Datatype (T/F).
==================================
a. val1 = True
print("Datatype of val1 is: ",type(val1))
o/p:
==========
Datatype of val1 is:  <class 'bool'>

b. val1 = False
print("Datatype of val1 is: ",type(val1))
o/p:
=======
Datatype of val1 is:  <class 'bool'>

iv. set Datatype:
========================  
set1 = {1,2,3,4,5}
print("Datatype of set is: ",type(set1))
o/p:
===========
Datatype of set is:  <class 'set'>

v. Dictionary datatype:
==============================
dict1 = {"name":"['Prem','sourav','Abhishek']","age":25,"salary":30000}
print("Datatype of dictionary is: ",type(dict1))
o/p:
============
Datatype of dictionary is:  <class 'dict'>

NOTE: char is not a datatype in python.   

2. Difference b/t list and tuple:
================================
i. creation:
=============
a. List is represented by square bracket [].
   my_list = ["hello","world"]
   o/p:
========
Datatype of my_list is:  <class 'list'>

b. Tuple is represented by paranthesis().
   t1 = ("hello","world")
   t2 = "hello","world" 
   o/p:
=========
Datatype of t1 is:  <class 'tuple'>
Datatype of t2 is:  <class 'tuple'>

ii. Mutability:
=================
a. List is mutable which means after the ceration of list we can change the content of existing list.
   my_list = ["hello","world"]
   my_list[0] = "helloo"
   print(my_list)
   o/p:
===========
['helloo', 'world']

b. Tuple is immutable which means we cant change the content of existing tuple.
   t2 = "hello","world"
   t2[0] = "helloo"
   print(t2)
   o/p:
===========
TypeError: 'tuple' object does not support item assignment

iii. Comprehension concept:
============================
a. It is applicable for list.
   fruits = ["apple","orange","guava"]
   new_list = [x for x in fruits if "g" not in x]
   print(new_list)
   o/p:
============
['apple']

b. It is not applicable for tuple.
   fruits = ("apple","orange","guava")
   new_tuple = (x for x in fruits if "g" not in x)
   print(new_tuple)
   o/p:
=============
<generator object <genexpr> at 0x7f29988e7410>

iv. Memory Consumption:
===========================
a. List consume more memory than tuple which means for each element inside list it requires 2 block of memory
   List is mutable so due to which it require 2 block of memory.
   import sys
   my_list = ["hello","world","hello","world","hello","world","hello","world","hello","world","hello","world","hello","world"]
   print(sys.getsizeof(my_list))
   o/p:
===============
176

b. Tuple is immutable so for each element it require 1 block of memory so due to this reason it consumes less memory.
   import sys
   my_tuple = ("hello","world","hello","world","hello","world","hello","world","hello","world","hello","world","hello","world")
   print(sys.getsizeof(my_tuple))
   o/p:
=============
160

v. Speed :
=================
a. List consumes more memory so it is a more complex data structure, so it is less faster than tuple.
   import timeit
   print(timeit.timeit(stmt='["hello","world","hello","world"]',number=10000000))
   o/p:
   ========
   0.3597571402788162

b. Tuple is faster than list because it consumes less memory , so it is less complex data structure.
   import timeit
   print(timeit.timeit(stmt='("hello","world","hello","world")',number=10000000))
   o/p:
  ==========
  0.07208278775215149  

Note: Tuple is more efficient than list because it is less complex.

Similarity b/t list and tuple:
================================
a. list:
============
i. It can accept duplicates.
   my_list = ["hello","world","hello","world","hello","world","hello","world","hello","world","hello","world","hello","world"]
ii. It holds heterogenous element which means element of different datatypes.
    my_list = [1,"hello",3.15,3+4j]
    print(my_list)
    o/p:
   =====
   [1, 'hello', 3.15, (3+4j)]
iii. Slicing and indexing are supported.
     my_list = [1,"hello",3.15,3+4j]
     print(my_list[0:3])
     print(my_list[0])
     o/p:
     =======
     [1, 'hello', 3.15]
     1

b.  tuple:
============
i. It can accept duplicates.
   my_tuple = ("hello","world","hello","world","hello","world","hello","world","hello","world","hello","world","hello","world")
ii. It holds heterogenous element which means element of different datatypes.
    my_tuple = (1,"hello",3.15,3+4j)
    print(my_tuple)
    o/p:
   ==========
   (1, 'hello', 3.15, (3+4j))
iii. Slicing and indexing are supported.
     my_tuple = (1,"hello",3.15,3+4j)
     print(my_tuple[0:3])
     print(my_tuple[0])
     o/p:
=============
     (1, 'hello', 3.15)

Impt Notes to Rememeber about list vs tuple:
========================================================
Special Features:
===========================
i. List:
===========================
a. It holds elements of different datatypes (hetrogenous element).
   For example:
   ============================
   my_list = [1,'sql',3.15,2+3j,None]
   print(my_list)
   print(len(my_list))
   print(type(my_list))
   o/p:
====================
[1, 'sql', 3.15, (2+3j), None]
5
<class 'list'>

b. It can accept duplicate element.
   For example:
   =============================
   my_list = ['sql','python','etl','sql']
   print(my_list)
   o/p:
================
['sql', 'python', 'etl', 'sql']

c. Ordering is mantained in list.
   For example:
   =========================
   my_list = ['sql','python','etl','sql']
   print(my_list[0])
   print(my_list[1])
   print(my_list[2])
   print(my_list[3])
   o/p:
=============
sql
python
etl
sql

d. Indexing and slicing is used.
e. It can append,extend,concatenate.
f. It is mutable.
      1


3. Copying list in python:
==============================
i. In python we can create 3 different kind of  copies:
==============================================================
a. Reference Copy:
===============================
i. Reference means point to certain location.
ii. When we create a reference copy than in this case both list original and newlist point to same location.

    For ex:
================
org_list = [1,2,3,4,5]
new_list = org_list
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
============
Original list in the python is:  [1, 2, 3, 4, 5]
New list in the python is:  [1, 2, 3, 4, 5]
Original list in the python is:  139643973771784
New list in the python is:  139643973771784
iii. In this case if we change the content of newlist than originallist will also change because both point to same memory location.

     For ex:
====================
org_list = [1,2,3,4,5]
new_list = org_list
new_list[0] = 6
new_list[1] = 7
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
==========
Original list in the python is:  [6, 7, 3, 4, 5]
New list in the python is:  [6, 7, 3, 4, 5]
Original list in the python is:  139643973780232
New list in the python is:  139643973780232

iv. It is done using assignment operator(=).
v. It is not a appropriate approach because here we are not able to preserve our original list , if we are changing newlist and mainly we create copy to preserve original list .
vi. Usecase:
====================
If we only want to create a newlist from original list but we dont wnat to change the content of newlist.

b. shallow copy:
=========================
i. When we create a shallow copy than in this case both list original list and new list will not point to same memory location.
   For ex: 
====================
org_list = [1,2,3,4,5,[6,7,8]]
new_list = org_list[:]
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
=========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643974117384
New list in the python is:  139643973773000

ii. In this case if we change the content of newlist than originallist will not change because both point to different memory location.
    For ex:
===================
org_list = [1,2,3,4,5,[6,7,8]]
new_list = org_list[:]
new_list[0] = 9
new_list[1] = 10
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
==========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [9, 10, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643973782664
New list in the python is:  139643973781640

iii. There are 3 different method to create a shallow copy:
================================================================
a. First using slicing operator (:).
   For ex:
==================
org_list = [1,2,3,4,5,[6,7,8]]
new_list = org_list[:]
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
=========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643974117384
New list in the python is:  139643973773000  

b. 2nd using copy() function.
   For ex:
=================
org_list = [1,2,3,4,5,[6,7,8]]
new_list = org_list.copy()
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
=========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643974245256
New list in the python is:  139643974116552

c. 3rd from copy module , you can use the copy() method/function.
   For ex:
=================
import copy
org_list = [1,2,3,4,5,[6,7,8]]
new_list = copy.copy(org_list)
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
=========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643973782664
New list in the python is:  139643974115976

iv. In case of shallow copy only top level is preserved , but in case of nested list it is not preserved.
    so in this case original list will change if we change newlist.
    For ex:
=================
org_list = [1,2,3,4,5,[6,7,8]]
new_list = org_list[:]
new_list[0] = 9
new_list[1] = 10
new_list[5][0] = 11
new_list[5][1] = 12
new_list[5][2] = 13
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
==========
Original list in the python is:  [1, 2, 3, 4, 5, [11, 12, 13]]
New list in the python is:  [9, 10, 3, 4, 5, [11, 12, 13]]
Original list in the python is:  139643973783048
New list in the python is:  139644362241672

v. vi. Usecase:
====================
This is mainly used when we only want to copy the top level but not the nested list.


c. Deep copy:
=====================
i. when we use deep copy than in this case entire thing is copied in newlist even the nested list.
   It creates complete independent copy of original list.
   Both point to different memory location.
   For example:
=========================
import copy
org_list = [1,2,3,4,5,[6,7,8]]
new_list = copy.deepcopy(org_list)
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
Original list in the python is:  139643973782664
New list in the python is:  139643974041416

ii. So we change the newlist so in this case original list will not change even the nested list that is present inside original list will not change.
    For example:
=========================
import copy
org_list = [1,2,3,4,5,[6,7,8]]
new_list = copy.deepcopy(org_list)
new_list[0] = 9
new_list[1] = 10
new_list[5][0] = 11
new_list[5][1] = 12
new_list[5][2] = 13
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))
o/p:
========
Original list in the python is:  [1, 2, 3, 4, 5, [6, 7, 8]]
New list in the python is:  [9, 10, 3, 4, 5, [11, 12, 13]]
Original list in the python is:  139643973783496
New list in the python is:  139643973783304 



iii. Method to create deepcopy:
================================
a. From copy module use deepcopy().
   For example:
=========================
import copy
org_list = [1,2,3,4,5,[6,7,8]]
new_list = copy.deepcopy(org_list)
print("Original list in the python is: ",org_list)
print("New list in the python is: ",new_list)
print("Original list in the python is: ",id(org_list))
print("New list in the python is: ",id(new_list))


4. Difference b/t .append() vs .extend() vs del() vs remove() vs insert():
==============================================================================
i. .append():
==========================
a. When we use this .append() method to insert element in the list , it will append at the end of the list.
   For example:
   =======================
   courses = ["sql","python","etl"]
   courses.append("azure")
   print(courses) 
   o/p:
=====================
['sql', 'python', 'etl', 'azure']

b. It does not accept multiple arguments.
   For example:
   ===================
   courses = ["sql","python","etl"]
   courses.append("azure","aws")
   print(courses)
   o/p:
============
TypeError: append() takes exactly one argument (2 given)


ii. .extend():
=================================
a. It is mainly used to extend a list.
   For example:
   even_list = [2,4,6]
   odd_list = [1,3,5]
   even_list.extend(odd_list)
   print(even_list)
   o/p:
===================
[2, 4, 6, 1, 3, 5]

b. It accept multiple arguments.
   For example:
   ======================
   even_list = [2,4,6]
   odd_list = [1,3,5]
   even_list.extend(odd_list)
   print(even_list)
   o/p:
=================
[2, 4, 6, 1, 3, 5]

iii. del():
===================
i. It is used mainly when we are aware of the index and want to delete a element from a particular index.
   For example:
   =========================
   courses = ["sql","python","etl","azure"]
   del courses[0:2]
   print(courses)
   o/p:
====================
['etl', 'azure']
    courses = ["sql","python","etl","azure"]
    del courses[3]
    print(courses)
    o/p:
=====================
['sql', 'python', 'etl']

iv .remove():
==============================
i. It is mainly used when we are not aware of the index and want to remove the element of list using the value.
   For example:
=========================
    courses = ["sql","python","etl","azure"]
    courses.remove("sql")
    print(courses)
    o/p:
========================
['python', 'etl', 'azure']


v. .insert():
==============================
i. If you want to insert a element at particular position/index we will use this method.
   For example:
   ==============================
   courses = ["sql","python","etl","azure"]
   courses.insert(0,"dwh")
   print(courses)
   o/p:
=====================
['dwh', 'sql', 'python', 'etl', 'azure']


5. Difference b/t pass vs continue vs break statement in python:
=============================================================================
i. pass:
=================
a. It helps to do nothing.
b. It gives same output as continue .
c. But it can be used with any block of code like class(), func() and also inside the loop.
d. It is not limited to loop only.
e. Code:
=================
i=0
while i!=10:
    i+=1
    if i==3:
        pass
    else:
        print(i)
o/p:
========
1
2
4
5
6
7
8
9
10


ii. continue:
==========================
a. It is only limited to loop either (for loop, while loop, do while loop).
b.  It can't be used with function,class etc any other block of code.
c. It skips current iteration.
d. Code:
================
i=0
while i!=10:
    i+=1
    if i==3:
        continue
    else:
        print(i)
o/p:
========
1
2
4
5
6
7
8
9
10

iii. break:
============================
a. It is only limited to loop either (for loop, while loop, do while loop).
b.  It can't be used with function,class etc any other block of code.
c. It is used to break/exit out of the loop based on certain condition.
d. Code:
=================
i=0
while i!=10:
    i+=1
    if i==3:
        break
    else:
        print(i)
o/p:
======
1
2

