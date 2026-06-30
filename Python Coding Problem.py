1. How to switch the 1st and last characters in a python string?
========================================================================

solution:
=============
i. Approach 1st:
=================
my_string = "hello"
new_string = my_string[-1]+my_string[1:-1]+my_string[0]
print("String After swapping is: ",new_string)

ii. Approach 2nd:
====================
def swapString(my_string):
 new_string = my_string[-1]+my_string[1:-1]+my_string[0]
 return new_string

my_string = "hello"
print("String After swapping is: ",swapString(my_string))

output:
==========
String After swapping is: oellh

2. Python program to find length of the list?
========================================================

solution:
======================
i. Using len():
========================
a. list1 = [10,20,30,40,50]
size = len(list1)
print("Length of list is: ",size)

b. def lengthList(list1):
  size = len(list1)
  return size

list1 = [10,20,30,40,50]
print("Length of list is: ",lengthList(list1))

output:
=============
Length of list is:  5

ii. Using Native method:
=======================================
a. list1 = [10,20,30,40,50]
count = 0
for i in list1:
  count=count+1
print("Length of list is: ",count)

b. def lengthList(list1):
  count = 0
  for i in list1:
    count=count+1
  return count

list1 = [10,20,30,40,50]
print("Length of list is: ",lengthList(list1))

o/p:
==========
Length of list is:  5

iii. Using List Comprehension:
=====================================
a. list1 = [10,20,30,40,50]
count=0
length = sum(1 for i in list1)
print("Length of list is: ",length)

b. def comprehensionList(list1):
  length = sum(1 for i in list1)
  return length

list1 = [10,20,30,40,50]
print("Length of list is: ",comprehensionList(list1))

o/p:
===========
Length of list is:  5

iv. Using Collections:
===============================
a. from collections import Counter
list1 = [10,20,30,40,50]
length = sum(Counter(list1).values())
print("Length of list is: ",length)

b. from collections import Counter
def lengthList(list1):
  length = sum(Counter(list1).values())
  return length

list1 = [10,20,30,40,50]
print("Length of list is: ",lengthList(list1))

o/p:
===========
Length of list is:  5

3. Python program to check maximum between 2 number:
==============================================================
solution:
=================
i. Approach 1st Using native approach:
============================================
a. a=4
b=2
if a>=b:
    print("Maximum between 2 number is: ",a)
else:
    print("Maximum bewteen 2 number is: ",b)
b. def maxNumber(a,b):
    if a>=b:
        return a
    else:
        return b

a=4
b=2
print("Maximum between 2 number is: ",maxNumber(a,b))
o/p:
===========
Maximum between 2 number is:  4

ii. Approach 2nd Using max():
==================================
a. a=4
b=2
maximum = max(a,b)
print("Maximum between 2 number is: ",maximum)

b. def maxNumber(a,b):
    maximum = max(a,b)
    return maximum

a=4
b=2
print("Maximum between 2 number is: ",maxNumber(a,b))
o/p:
============
Maximum between 2 number is:  4

iii. Approach 3rd Using list comprehension:
=================================================
a. a=4
b=2
maximum = [a if a>=b else b]
for max in maximum:
    print("Maximum between 2 number is: ",max)
	
b.  def maxNumber(a,b):
    maximum = [a if a>=b else b]
    for max in maximum:
        return max

a=4
b=2
print("Maximum between 2 number is: ",maxNumber(a,b))
o/p:
==============
Maximum between 2 number is:  4

iv. Approach 4th using lambda function:
==============================================
a=4
b=2
maximum = lambda a,b:a if a>=b else b
print("Maximum between 2 number is: ",maximum(a,b))
o/p:
==============
Maximum between 2 number is:  4

4. Python program to check minimum between 2 number:
==============================================================
solution:
=================
i. Approach 1st Using native approach:
============================================
a. a=4
b=2
if a<=b:
    print("Minimum between 2 number is: ",a)
else:
    print("Minimum between 2 number is: ",b)
	
b. def minimumNumber(a,b):
    if a<=b:
        return a
    else:
        return b
    
a=4
b=2
print("Minimum between 2 number is: ",minimumNumber(a,b))
o/p:
==============
Minimum between 2 number is:  2

ii. Approach 2nd using min():
==========================================
a. a=4
b=2
minimum = min(a,b)
print("Minimum between 2 number is: ",minimum)

b. def minNumber(a,b):
    minimum = min(a,b)
    return minimum

a=4
b=2
print("Minimum between 2 number is: ",minNumber(a,b))
o/p:
=============
Minimum between 2 number is:  2

iii. Approach 3rd using list comprehension:
====================================================
a. a=4
b=2
minimum = [min(a,b)]
for value in minimum:
    print("Minimum between 2 number is: ",value)
	
b. def minNumber(a,b):
    minimum = [min(a,b)]
    for value in minimum:
        return value
    
a=4
b=2
print("Minimum between 2 number is: ",minNumber(a,b))
o/p:
=============
Minimum between 2 number is:  2

iv. Approach 4th using lambda():
=========================================
a=4
b=2
minimum = lambda a,b:a if a<=b else b
print("Minimum between 2 number is: ",minimum(a,b))
o/p:
==========
Minimum between 2 number is:  2

5. Check if element exists in python list:
====================================================
Approach 1st:
==================
i. list1 = [1,6,3,5,3,4]
i=7
if i in list1:
    print("Exist")
else:
    print("not exist")
	
ii. def listExist(list1):
    i=7
    if i in list1:
        return "exist"
    else:
        return "not exist"
    
list1 = [1,6,3,5,3,4]
print(listExist(list1))
o/p:
=======
not exist

Approach 2nd:
==================
i. list1 = [1,6,3,5,3,4]
i=4
if (i==4):
    print("Exist")
else:
    print("Not Exist")

ii. def listExist(list1):
    i=4
    if i==4:
        return "exist"
    else:
        return "Not Exist"
    
list1 = [1,6,3,5,3,4]
print(listExist(list1))
o/p:
======
exist

6. Python program to clear a list:
================================================
Approach 1st using clear():
===============================
i. list1 = [1,6,3,5,3,4]
list1.clear()
print("After clearing list: ",list1)

ii. def listClear(list1):
    list1.clear()
    return list1

list1 = [1,6,3,5,3,4]
print("After clearing list: ",listClear(list1))
o/p:
=============
After clearing list:  []

 Approach 2nd Using del:
 =============================
 i. list1 = [1,6,3,5,3,4]
del list1[:]
print("After clearing list: ",list1)

ii. def listClear(list1):
    del list1[:]
    return list1

list1 = [1,6,3,5,3,4]
print("After clearing list: ",listClear(list1))
o/p:
=====
After clearing list:  []

7. Reverse a list in python:
============================
Solution:
=============
Approach 1st using slicing:
=================================
a. input_list = [4,5,6,7,8,9]
print("Reverse of list is: ",input_list[::-1])

b. def reverseList(input_list):
    return input_list[::-1]

input_list = [4,5,6,7,8,9]
print("Reverse of list is: ",reverseList(input_list))
o/p:
=====
Reverse of list is:  [9, 8, 7, 6, 5, 4]

Approach 2nd Using reverse():
===============================
a. input_list = [4,5,6,7,8,9]
input_list.reverse()
print("Reverse of list is: ",input_list)
b. def reverseList(input_list):
    input_list.reverse()
    return input_list

input_list = [4,5,6,7,8,9]
print("Reverse of list is: ",reverseList(input_list))
o/p:
====
Reverse of list is:  [9, 8, 7, 6, 5, 4]

Approach 3rd using insert():
============================
a. input_list = [4,5,6,7,8,9]
lst1 = []
for i in input_list:
    lst1.insert(0,i)
print("Reverse of the list is: ",lst1)
b. def reverseList(input_list):
    lst1 = []
    for i in input_list:
        lst1.insert(0,i)
    return lst1

input_list = [4,5,6,7,8,9]
print("Reverse of list is: ",reverseList(input_list))
o/p:
=======
Reverse of list is:  [9, 8, 7, 6, 5, 4]

Approach 4th using Two pointer Approach:
========================================
a. input_list = [4,5,6,7,8,9]
left = 0
right = len(input_list)-1
while(left<right):
    temp = input_list[left]
    input_list[left]=input_list[right]
    input_list[right]=temp
    left = left+1
    right = right-1
print("Reverse of list is: ",input_list)
b. def reverseList(input_list):
    left = 0
    right = len(input_list)-1
    while(left<right):
        temp = input_list[right]
        input_list[right] = input_list[left]
        input_list[left] = temp
        left = left+1
        right = right-1
        return input_list
    
input_list = [4,5,6,7,8,9]
print("Reverse of list is: ",reverseList(input_list))
o/p:
======
Reverse of list is:  [9, 5, 6, 7, 8, 4]

8. Python Coding Challenge:
=========================
Count the Occurence of each element in list:
====================================
i/p:
==
lst = ['apple','banana','apple','orange','banana','banana']
o/p:
=====
{'apple': 2, 'banana': 3, 'orange': 1}

Solution:
=========
Approach 1st:
============
a. lst = ['apple','banana','apple','orange','banana','banana']
dict1 = {}
for item in lst:
 if item in dict1:
 dict1[item] = dict1[item]+1
 else:
 dict1[item] = 1
print("Occurence of element in the list is: ",dict1)

b. def occurenceCounter(lst):
 dict1 = {}
 for item in lst:
 if item in dict1:
 dict1[item] = dict1[item] + 1
 else:
 dict1[item] = 1
 return dict1


lst = ['apple','banana','apple','orange','banana','banana']
print("Occurrence of element in the list is:", occurenceCounter(lst))
o/p:
======
Occurrence of element in the list is: {'apple': 2, 'banana': 3, 'orange': 1}
Approach 2nd Using Counter():
=====================
a. from collections import Counter
lst = ['apple','banana','apple','orange','banana','banana']
count_occurence = Counter(lst)
print("Occurrence of element in the list is:", count_occurence)

b. from collections import Counter
def occurenceCounter(lst):
 count_occcurence = Counter(lst)
 return count_occurence

lst = ['apple','banana','apple','orange','banana','banana']
print("Occurrence of element in the list is:", occurenceCounter(lst))
o/p:
======
Occurrence of element in the list is: Counter({'banana': 3, 'apple': 2, 'orange': 1})

9. Python Coding Challenge:
===============================
Find sum and average of list in Python:
===========================================
i. Approach 1st:
=====================
lst = [4,5,1,2,9,7,10,8]
sum = 0
for i in lst:
    sum = sum+i
avg = sum/len(lst)
print("Sum of element in list is: ",sum)
print("Average of element in list is: ",avg)
o/p:
=====
Sum of element in list is:  46
Average of element in list is:  5.75

ii. Approach 2nd:
======================
def summingList(lst):
    sum = 0
    for i in lst:
        sum = sum+i
    avg = sum/len(lst)
    return (sum,avg)
    
    
    
lst = [4,5,1,2,9,7,10,8]
print("Final output",summingList(lst))
o/p:
======
Final output (46, 5.75)

10. Multiply Element in a list:
==================================
i. Approach 1st:
=====================
list1 = [1,2,3]
result = 1
for i in list1:
    result = result*i
print("Multiply Element in a list is: ",result)
o/p:
=======
Multiply Element in a list is:  6

ii. Approach 2nd:
======================
def multipleList(list1):
    result = 1
    for i in list1:
        result = result*i
    return result

list1 = [1,2,3]
print("Multiply Element in a list is: ",multipleList(list1))
o/p:
=========
Multiply Element in a list is:  6

10. Python Coding Challenge:
================================
i. Approach 1st using sort():
================================
a. list1 = [10,20,4,45,99]
list1.sort()
print("Smallest Elemnt in a list is: ",list1[0])

b. def smallestList(list1):
    list1.sort()
    return list1[0]

list1 = [10,20,4,45,99]
print("Smallest Element is a list is: ",smallestList(list1))

o/p:
======
Smallest Element is a list is:  4

ii. Approach 2nd using min():
==============================
a. list1 = [10,20,4,45,99]
min_element = min(list1)
print("Smallest Element in a list is: ",min_element)

b. def smallestList(list1):
    min_element = min(list1)
    return min_element

list1 = [10,20,4,99]
print("Smallest Element in a list is: ",smallestList(list1))

o/p:
========
Smallest Element in a list is:  4

iii. Approach 3rd using normal approach:
==========================================
a. list1 = [10,20,4,45,99]
min1 = list1[0]
for i in range(len(list1)):
    if list1[i]<min1:
        min1 = list1[i]
print("Smallest Element in a list is: ",min1)

b. def smallestElement(list1):
    min1 = list1[0]
    for i in range(len(list1)):
        if list1[i]<min1:
            min1 = list1[i]
    return min1

list1 = [10,20,4,45,99]
print("Smallest Element in a list is: ",smallestElement(list1))

o/p:
=========
Smallest Element in a list is:  4

11. Finding the minimum element in a list that consists of duplicate elements:
================================================================================
Solution:
============
i. Approach 1st using sort():
===============================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
set_list.sort()
print("List after removing duplicate is: ",set_list , '\n' , "Smallest Element in a list is: ",set_list[0])

b. def smallestElement(my_list):
    set_list = list(set(my_list))
    set_list.sort()
    return (set_list, set_list[0])

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]

result = smallestElement(my_list)

print("List after removing duplicate is:", result[0], '\n',
      "Smallest Element in a list is:", result[1])

o/p:
=======
List after removing duplicate is: [2, 3, 4, 5, 7, 9, 10, 15, 68] 
 Smallest Element in a list is: 2

ii. Approach 2nd using min():
================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
smallest = min(set_list)
print("List after removing duplicate is: ",set_list , '\n' , "Smallest Element in a list is: ",smallest)

b. def smallestElement(my_list):
    set_list = list(set(my_list))
    smallest = min(set_list)
    return (set_list,smallest)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = smallestElement(my_list)
print("List after removing duplicate is: ",result[0] , '\n' , "Smallest Element in a list is: ",result[1])

o/p:
=========
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Smallest Element in a list is:  2

iii. Approach 3rd using normal approach:
============================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
min1 = set_list[0]
size = len(set_list)
for i in range(size):
    if set_list[i] < min1:
        min1 = set_list[i]
print("List after removing duplicate is: ",set_list , '\n' , "Smallest Element in a list is: ",min1)

b. def smallestElement(my_list):
    set_list = list(set(my_list))
    min1 = set_list[0]
    size = len(set_list)
    for i in range(size):
        if set_list[i] < min1:
            min1 = set_list[i]
    return (set_list,min1)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = smallestElement(my_list)
print("List After removing duplicate is: ",result[0] , '\n' , "Samllest Element in a list is: ",result[1])

o/p:
======
List After removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Samllest Element in a list is:  2 

12. 11. Finding the smallest,second smallest  element in a list that consists of duplicate elements:
=======================================================================================================
 Solution:
============
i. Approach 1st using sort():
===============================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
set_list.sort()
smallest1 = set_list[0]
smallest2 = set_list[1]
print("List after removing duplicate: ",set_list,'\n',"Smallest Element in the list is: ",smallest1,'\n',"Second Smallest Element in the list is: ",smallest2)

b. def secondsmallestElement(my_list):
    set_list = list(set(my_list))
    set_list.sort()
    smallest1 = set_list[0]
    smallest2 = set_list[1]
    return (set_list,smallest1,smallest2)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondsmallestElement(my_list)
print("List after removing duplicate",result[0],'\n',"Smallest Element in the list is: ",result[1],'\n',"Second Smallest Element in the list is: ",smallest2)

o/p:
==========
List after removing duplicate [2, 3, 4, 5, 7, 9, 10, 15, 68] 
 Smallest Element in the list is:  2 
 Second Smallest Element in the list is:  3
 
ii. Approach 3rd using normal approach:
============================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
min1 = float('inf')
min2 = float('inf')
size = len(set_list)
for i in range(size):
    if set_list[i] < min1:
        min2 = min1
        min1 = set_list[i]
    elif set_list[i] < min2:
        
        min2 = set_list[i]
print("List after removing duplicate: ",set_list,'\n',"Smallest Element in the list is: ",min1,'\n',"Second Smallest Element in the list is: ",min2)

b. def secondsmallestElement(my_list):
    set_list = list(set(my_list))
    min1 = float('inf')
    min2 = float('inf')
    size = len(set_list)
    for i in range(size):
        if set_list[i] < min1:
            min2 = min1
            min1 = set_list[i]
        elif set_list[i] < min2:
            min2 = set_list[i]
    return (set_list,min1,min2)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondsmallestElement(my_list)
print("List after removing duplicate: ",set_list,'\n',"Smallest Element in the list is: ",min1,'\n',"Second Smallest Element in the list is: ",min2)

o/p:
===========
List after removing duplicate:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Smallest Element in the list is:  2 
 Second Smallest Element in the list is:  3

iii. Approach 3rd using max():
================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
min1 = min(set_list)
min2 = min([x for x in set_list if x != min1])
print("List after removing duplicate is: ",set_list,'\n',"Smallest Element in the list is: ",min1,'\n',"Second Smallest Element in the list is: ",min2)

b. def secondSmallestElement(my_list):
    set_list = list(set(my_list))
    min1 = min(set_list)
    min2 = min([x for x in set_list if x!=min1])
    return(set_list,min1,min2)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondSmallestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1],'\n',"Second Largest Element in the list is: ",result[2])

o/p:
============
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Smallest Element in the list is:  2 
 Second Smallest Element in the list is:  3
 
13. Finding the maximum element in a list that consists of duplicate elements:
================================================================================
Solution:
============
i. Approach 1st using sort():
===============================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
set_list.sort()
print("List after removing duplicate: ",set_list,'\n',"Largest Element in the list is: ",set_list[-1])

b. def largestElement(my_list):
    set_list = list(set(my_list))
    set_list.sort()
    return (set_list,set_list[-1])

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = largestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1])

o/p:
=======
List after removing duplicate is:  [2, 3, 4, 5, 7, 9, 10, 15, 68] 
 Largest Element in the list is:  68

ii. Approach 2nd using max():
================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
maximum = max(set_list)
print("List after removing duplicate is: ",set_list,'\n',"Largest Element in the list is: ",maximum)

b. def largestElement(my_list):
    set_list = list(set(my_list))
    
    maximum = max(set_list)
    return (set_list,maximum)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = largestElement(my_list)
print("List after removing duplicate: ",result[0],'\n',"Largest Element in the list is: ",result[1])

o/p:
=========
List after removing duplicate:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Largest Element in the list is:  68

iii. Approach 3rd using normal approach:
============================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
size = len(set_list)
max1 = set_list[0]
for i in range(size):
    if set_list[i] > max1:
        max1 = set_list[i]
print("List after removing duplicate is: ",set_list,'\n',"Largest Element in the list is: ",max1)

b. def largestElement(my_list):
    set_list = list(set(my_list))
    size = len(set_list)
    max1 = set_list[0]
    for i in range(size):
        if set_list[i] > max1:
            max1 = set_list[i]
    return (set_list,max1)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = largestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1])

o/p:
======
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Largest Element in the list is:  68 

14.  Finding the Largest,second Largest  element in a list that consists of duplicate elements:
=======================================================================================================
i. Approach 1st using sort():
==================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
set_list.sort()
print("List after removing duplicate is: ",set_list,'\n',"Largest Element in the list is: ",set_list[-1],'\n',"Second Largest Element in the list is: ",set_list[-2])

b. def secondLargestElement(my_list):
    set_list = list(set(my_list))
    set_list.sort()
    return(set_list,set_list[-1],set_list[-2])

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondLargestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1],'\n',"Second Largest Element in the list is: ",result[2])

o/p:
=========
List after removing duplicate is:  [2, 3, 4, 5, 7, 9, 10, 15, 68] 
 Largest Element in the list is:  68 
 Second Largest Element in the list is:  15

ii. Using Normal Approach:
=====================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
max1 = float('-inf')
max2 = float('-inf')
size = len(set_list)
for i in range(size):
    if set_list[i] > max1:
        max1 = set_list[i]
    elif set_list[i] > max2:
        max2 = set_list[i]
print("List after removing duplicate is: ",set_list,'\n',"Largest Element in the list is: ",max1,'\n',"Second Largest Element in the list is: ",max2)

b. def secondLargestElement(my_list):
    set_list = list(set(my_list))
    max1 = float('-inf')
    max2 = float('-inf')
    size = len(set_list)
    for i in range(size):
        if set_list[i] > max1:
            max1 = set_list[i]
        elif set_list[i] > max2:
            max2 = set_list[i]
    return(set_list,max1,max2)


my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondLargestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1],'\n',"Second Largest Element in the list is: ",result[2])

o/p:
============
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Largest Element in the list is:  68 
 Second Largest Element in the list is:  15

Note:
==========
Key Concept:
=============================

| Case     | Initialization  |
| -------- | --------------- |
| Smallest | `float('inf')`  |
| Largest  | `float('-inf')` |

“Use +infinity for min problems and -infinity for max problems.”

iii. Approach 3rd using max():
=======================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
max1 = max(set_list)
max2 = max([x for x in set_list if x != max1])
print("List after removing duplicate is: ",set_list,'\n',"Largest Element in the list is: ",max1,'\n',"Second Largest Element in the list is: ",max2)

b. def secondLargestElement(my_list):
    set_list = list(set(my_list))
    max1 = max(set_list)
    max2 = max([x for x in set_list if x!=max1])
    return(set_list,max1,max2)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = secondLargestElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Largest Element in the list is: ",result[1],'\n',"Second Largest Element in the list is: ",result[2])

o/p:
=============
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Largest Element in the list is:  68 
 Second Largest Element in the list is:  15

15. Finding the even,odd number in a list that consists of duplicate elements:
=======================================================================================
i. Approach 1st using list comprehension:
==================================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
even_nos = [num for num in set_list if num%2==0]
odd_nos = [num for num in set_list if num%2!=0]
print("List after removing duplicate is: ",set_list,'\n',"Even number in the list is: ",even_nos,'\n',"Odd number in the list is: ",odd_nos)

b. def evenoddList(my_list):
    set_list = list(set(my_list))
    even_nos = [num for num in set_list if num%2==0]
    odd_nos =  [num for num in set_list if num%2!=0]
    return (set_list,even_nos,odd_nos)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = evenoddList(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Even nos in the list is: ",result[1],'\n',"Odd nos in the list is: ",result[2])

o/p:
============
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even number in the list is:  [2, 4, 68, 10] 
 Odd number in the list is:  [3, 5, 7, 9, 15]

ii. Approach 2nd using lambda funct + filter():
=========================================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
even_nos = list(filter((lambda x:x%2==0),set_list))
odd_nos = list(filter((lambda x:x%2!=0),set_list))
print("List after removing duplicate is: ",set_list,'\n',"Even nos in the list is: ",even_nos,'\n',"Odd number in the list is: ",odd_nos)
o/p:
============
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even nos in the list is:  [2, 4, 68, 10] 
 Odd number in the list is:  [3, 5, 7, 9, 15]

16. Finding the even,odd number count in a list that consists of duplicate elements:
=======================================================================================
i. Approach 1st using normal approach:
================================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
even_count = 0
odd_count = 0
for num in set_list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("List after removing duplicate is: ",set_list,'\n',"Even count in the list is: ",even_count,'\n',"Odd count in the list is: ",odd_count)
o/p:
==========
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even count in the list is:  4 
 Odd count in the list is:  5

b. def oddevenCount(my_list):
    set_list = list(set(my_list))
    even_count,odd_count=0,0
    for num in set_list:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    return(set_list,even_count,odd_count)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
result = oddevenCount(my_list)
print("Value of result is:",result)
print("List after removing duplicate: ",result[0],'\n',"Even count in the list is: ",result[1],'\n',"Odd count in the list is: ",result[2])

o/p:
============
Value of result is: ([2, 3, 4, 5, 68, 7, 9, 10, 15], 4, 5)
List after removing duplicate:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even count in the list is:  4 
 Odd count in the list is:  5

ii. Approach 2nd uisng list comprehension + len():
================================================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
even = [num for num in set_list if num%2==0]
odd = [num for num in set_list if num%2!=0]
even_count = len(even)
odd_count = len(odd)
print("List after removing duplicate is: ",set_list,'\n',"Even count in the list is: ",even_count,'\n',"Odd count in the list is: ",odd_count)
o/p:
===========
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even count in the list is:  4 
 Odd count in the list is:  5

b. def oddevenCount(my_list):
    set_list = list(set(my_list))
    even = [num for num in set_list if num%2==0]
    odd = [num for num in set_list if num%2!=0]
    even_count = len(even)
    odd_count = len(odd)
    return (set_list,even_count,odd_count)

my_list = [5,2,3,2,5,4,7,9,7,10,15,68] 
result = oddevenCount(my_list)
print("Value of result is:",result)
print("List after removing duplicate is: ",result[0],'\n',"Even count in the list is: ",result[1],'\n',"Odd count inn the list is: ",result[2])
o/p:
===========
Value of result is: ([2, 3, 4, 5, 68, 7, 9, 10, 15], 4, 5)
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even count in the list is:  4 
 Odd count inn the list is:  5

iii. Approach 3rd using lambda function:
==================================================
a. my_list = [5,2,3,2,5,4,7,9,7,10,15,68]
set_list = list(set(my_list))
even_count = len(list(filter(lambda num:(num%2==0),set_list)))
odd_count = len(list(filter(lambda num:(num%2!=0),set_list)))
print("List after removing duplicate is: ",set_list,'\n',"Even count in the list is: ",even_count,'\n',"Odd count in the list is: ",odd_count)
o/p:
==========
List after removing duplicate is:  [2, 3, 4, 5, 68, 7, 9, 10, 15] 
 Even count in the list is:  4 
 Odd count in the list is:  5

15. Finding the positive,negative,zeros number in a list that consists of duplicate elements:
==================================================================================================
i. Approach 1st using list comprehension:
=====================================================
a. my_list = [11,-21,0,45,66,-93,-93,-21,11]

set_list = list(set(my_list))

positive_num = [num for num in set_list if num > 0]
negative_num = [num for num in set_list if num < 0]
zeros_num = [num for num in set_list if num == 0]

print("List after removing duplicate is: ",set_list,'\n',"Positive number in the list is: ",positive_num,'\n',"Negative number in the list is: ",negative_num,'\n',"Zeros in the list is: ",zeros_num)


print(f"""
List after removing duplicate is: {result[0]}
Positive number in the list is: {result[1]}
Negative number in the list is: {result[2]}
Zeros in the list is: {result[3]}
""")

b. def elementList(my_list):
    set_list = list(set(my_list))
    positive_num = [num for num in set_list if num>0]
    negative_num = [num for num in set_list if num<0]
    zeros_num = [num for num in set_list if num==0]
    return (set_list,positive_num,negative_num,zeros_num)

my_list = [11,-21,0,45,66,-93,-93,-21,11]
result = elementList(my_list)
print("List after removing duplicate is: ", result[0], '\n',
      "Positive number in the list is: ", result[1], '\n',
      "Negative number in the list is: ", result[2], '\n',
      "Zeros in the list is: ", result[3])

print(f"""
List after removing duplicate is: {result[0]}
Positive number in the list is: {result[1]}
Negative number in the list is: {result[2]}
Zeros in the list is: {result[3]}
""")

o/p:
===========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive number in the list is:  [66, 11, 45] 
 Negative number in the list is:  [-93, -21] 
 Zeros in the list is:  [0]

ii. Approach 2nd using lambda() function:
=================================================
a. my_list = [11,-21,0,45,66,-93,-93,-21,11]
set_list = list(set(my_list))
positive_num = list(filter(lambda num:(num>0),set_list))
negative_num = list(filter(lambda num:(num<0),set_list))
zeros_num = list(filter(lambda num:(num==0),set_list))
print(f"""
     List after removing duplicate is: {set_list},
     Positive number in the list is: {positive_num},
     Negative number in the list is: {negative_num},
     Zeros number in the list is: {zeros_num}""")

print("List after removing duplicate is: ",set_list,'\n',
      "Positive number in the list is: ",positive_num,'\n',
      "Negative number in the list is: ",negative_num,'\n',
      "Zeros in the list is: ",zeros_num)

o/p:
===========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive number in the list is:  [66, 11, 45] 
 Negative number in the list is:  [-93, -21] 
 Zeros in the list is:  [0]

iii. Approach 3rd using normal approach:
==========================================
a. my_list = [11, -21, 0, 45, 66, -93, -93, -21, 11]

set_list = list(set(my_list))

positive_num = []
negative_num = []
zeros_num = []

for num in set_list:   
    if num > 0:
        positive_num.append(num)
    elif num < 0:
        negative_num.append(num)
    else:
        zeros_num.append(num)

print(f"""
List after removing duplicate is: {set_list}
Positive number in the list is: {positive_num}
Negative number in the list is: {negative_num}
Zeros number in the list is: {zeros_num}
""")
        
print("List after removing duplicate is: ",set_list,'\n',
      "Positive number in the list is: ",positive_num,'\n',
      "Negative number in the list is: ",negative_num,'\n',
      "Zeros in the list is: ",zeros_num)

b. def elementList(my_list):
    set_list = list(set(my_list))
    positive_num = []
    negative_num = []
    zeros_num = []
    for num in set_list:
        if num>0:
            positive_num.append(num)
        elif num<0:
            negative_num.append(num)
        elif num==0:
            zeros_num.append(num)
    return(set_list,positive_num,negative_num,zeros_num)

my_list = [11, -21, 0, 45, 66, -93, -93, -21, 11]
result = elementList(my_list)
print("List after removing duplicate is: ",result[0],'\n',
      "Positive number in the list is: ",result[1],'\n',
      "Negative number in the list is: ",result[2],'\n',
      "Zeros in the list is: ",result[3])

print(f"""
List after removing duplicate is: {result[0]}
Positive number in the list is: {result[1]}
Negative number in the list is: {result[2]}
Zeros in the list is: {result[3]}
""")
o/p:
===========
List after removing duplicate is: [0, 66, -93, 11, -21, 45]
Positive number in the list is: [66, 11, 45]
Negative number in the list is: [-93, -21]
Zeros in the list is: [0]


16.  Find the count of positive,negative,zeros number in a list that consists of duplicate elements:
========================================================================================================
Solution:
===============
i. Approach 1st using list comprehension + len():
=======================================================
a. my_list = [11,-21,0,45,66,-93,-93,-21,11]
set_list = list(set(my_list))
pos_count = len([num for num in set_list if num>0])
neg_count = len([num for num in set_list if num<0])
zeros_count = len([num for num in set_list if num==0])
print("List after removing duplicate is: ",set_list,'\n',"Positive count in list is: ",pos_count,'\n',"Negative count in list is: ",neg_count,'\n'"Zeros in list is: ",zeros_count)
print(f"""
       List after removing duplicate is: {set_list}
       Positive count in list is: {pos_count}
       Negative count in list is: {neg_count}
       Zeros count in list is: {zeros_count}""")

b. def countElement(my_list):
    set_list = list(set(my_list))
    pos_count = len([num for num in set_list if num>0])
    neg_count = len([num for num in set_list if num<0])
    zeros_count = len([num for num in set_list if num==0])
    return(set_list,pos_count,neg_count,zeros_count)

my_list = [11,-21,0,45,66,-93,-93,-21,11]
result = countElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Positive count in the list is: ",result[1],'\n',"Negative count in the list is: ",result[2],'\n',"Zeros in the list is: ",result[3])
print(f"""
       List after removing duplicate is: {result[0]}
       Positive count in list is: {result[1]}
       Negative count in list is: {result[2]}
       Zeros count in list is: {result[3]}""")
o/p:
===========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive count in list is:  3 
 Negative count in list is:  2 
Zeros in list is:  1

ii. Approach 2nd using lambda() function:
=================================================
a. my_list = [11,-21,0,45,66,-93,-93,-21,11]
set_list = list(set(my_list))
pos_count = len(list(filter(lambda num:(num>0),set_list)))
neg_count = len(list(filter(lambda num: num < 0, set_list)))
zeros_count = len(list(filter(lambda num:(num==0),set_list)))
print("List after removing duplicate is: ",set_list,'\n',"Positive count in list is: ",pos_count,'\n',"Negative count in list is: ",neg_count,'\n'"Zeros in list is: ",zeros_count)
print(f"""
       List after removing duplicate is: {set_list}
       Positive count in list is: {pos_count}
       Negative count in list is: {neg_count}
       Zeros count in list is: {zeros_count}""")
o/p:
=========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive count in list is:  3 
 Negative count in list is:  2 
Zeros in list is:  1

iii. Approach 3rd using normal approach:
========================================
a. my_list = [11,-21,0,45,66,-93,-93,-21,11]
set_list = list(set(my_list))
pos_count = 0
neg_count = 0
zeros_count = 0
for num in set_list:
    if num>0:
        pos_count = pos_count+1
    elif num<0:
        neg_count = neg_count+1
    else:
        zeros_count = zeros_count+1
print("List after removing duplicate is: ",set_list,'\n',"Positive count in list is: ",pos_count,'\n',"Negative count in list is: ",neg_count,'\n'"Zeros in list is: ",zeros_count)
print(f"""
       List after removing duplicate is: {set_list}
       Positive count in list is: {pos_count}
       Negative count in list is: {neg_count}
       Zeros count in list is: {zeros_count}""")
o/p:
=========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive count in list is:  3 
 Negative count in list is:  2 
Zeros in list is:  1

b. def countElement(my_list):
    set_list = list(set(my_list))
    pos_count = 0
    neg_count = 0
    zeros_count = 0
    for num in set_list:
        if num>0:
            pos_count = pos_count+1
        elif num<0:
            neg_count = neg_count+1
        else:
            zeros_count = zeros_count+1
    return (set_list,pos_count,neg_count,zeros_count)

my_list = [11,-21,0,45,66,-93,-93,-21,11]
result = countElement(my_list)
print("List after removing duplicate is: ",result[0],'\n',"Positive count in list is: ",result[1],'\n',"Negative count in list is: ",result[2],'\n'"Zeros in list is: ",result[3])
print(f"""
       List after removing duplicate is: {result[0]}
       Positive count in list is: {result[1]}
       Negative count in list is: {result[2]}
       Zeros count in list is: {result[3]}""")
o/p:
===========
List after removing duplicate is:  [0, 66, -93, 11, -21, 45] 
 Positive count in list is:  3 
 Negative count in list is:  2 
Zeros in list is:  1


17. Python program to remove an multiple element from the list:
===============================================================
i. Approach 1st using normal approach + remove():
====================================================
a. my_list = [1,2,3,4,5,6,7,8,9,10,10,2,3,4,5]
to_remove = [3,5,7]
set_list = list(set(my_list))
for num in to_remove:
    if num in set_list:
        set_list.remove(num)
print("List after removing an element: ",set_list)

b. def removeElement(my_list,to_remove):
    set_list = list(set(my_list))
    for num in to_remove:
        if num in set_list:
            set_list.remove(num)
    return(set_list)

my_list = [1,2,3,4,5,6,7,8,9,10,10,2,3,4,5]
to_remove = [3,5,7]
result = removeElement(my_list,to_remove)
print("List after removing an element: ",result)
o/p:
====
List after removing an element:  [1, 2, 4, 6, 8, 9, 10]

ii. Approach 2nd using list comprehension:
==========================================
a. my_list = [1,2,3,4,5,6,7,8,9,10,10,2,3,4,5]
to_remove = [3,5,7]
set_list = list(set(my_list))
result = [num for num in set_list if num not in to_remove]
print("List after removing an duplicate is: ",set_list,'\n',"List after removing an element is: ",result)

b. def removeElement(my_list,to_remove):
    set_list = list(set(my_list))
    result = [num for num in set_list if num not in to_remove]
    return(set_list,result)

my_list = [1,2,3,4,5,6,7,8,9,10,10,2,3,4,5]
to_remove = [3,5,7]
result1 = removeElement(my_list,to_remove)
print("List after removing duplicate is: ",result1[0],'\n',"List after removing an element is: ",result1[1])
o/p:
====
List after removing duplicate is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
List after removing an element is:  [1, 2, 4, 6, 8, 9, 10]


18. Python Coding problem Converting List of List to Dictionary:
====================================================================
i. Approach 1st using zip():
==============================
a. keys = ["Rash","Kil","Varsha"]
values = [1,4,5]
dict1 = dict(zip(keys,values))
print("List after converting to dictionary is: ",dict1)

b. def listToDictConversion(keys,values):
    dict1 = dict(zip(keys,values))
    return dict1

keys = ["Rash","Kil","Varsha"]
values = [1,4,5]
result = listToDictConversion(keys,values)
print("List after converting to dictionary is: ",result)
o/p:
======
List after converting to dictionary is:  {'Rash': 1, 'Kil': 4, 'Varsha': 5}

ii. Approach 2nd using Dictionary Comprehension:
==================================================
a. keys = ["Rash","Kil","Varsha"]
values = [1,4,5]
result = {keys[i] : values[i] for i in range(len(keys))}
print("List after converting to dictionary is: ",result)

b. def listToDictConversion(keys,values):
    result = {keys[i] : values[i] for i in range(len(keys))}
    return result

keys = ["Rash","Kil","Varsha"]
values = [1,4,5]
result = listToDictConversion(keys,values)
print("List after converting to dictionary is: ",result)
o/p:
========
List after converting to dictionary is:  {'Rash': 1, 'Kil': 4, 'Varsha': 5}


19. Program to remove duplicates from a list of integers:
===========================================================
i. Approach 1st using set():
============================
a. my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
unique_list = list(set(my_list))
print("List after removing duplicate is: ",unique_list)

b. def removeDuplicate(my_list):
    unique_list = list(set(my_list))
    return unique_list

my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
result = removeDuplicate(my_list)
print("List after removing duplicate is: ",result)
o/p:
======
List after removing duplicate is:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

ii. Approach 2nd using normal approach:
=========================================
a. my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicate is: ",result)

b. def removeDuplicate(my_list):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
result = removeDuplicate(my_list)
print("List after removing duplicate is: ",result)
o/p:
======
List after removing duplicate is:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

iii. Approach 3rd using list comprehension:
============================================
a. my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]

print(result)

b. def removeDuplicate(my_list):
    unique_list = []
    [unique_list.append(item) for item in my_list if item not in unique_list]
    return unique_list

my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
result = removeDuplicate(my_list)
print("List after removing duplicate is: ",result)
o/p:
=====
List after removing duplicate is:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

20. Python program to print duplicates from a list of integers:
===================================================================
Approach 1st:
================
a. my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
unique_list = []
duplicate_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicate_list:
        duplicate_list.append(item)
print("List after removing duplicate is: ",unique_list,'\n',"List that contain duplicate element",duplicate_list)

print(f"""List after removing duplicate is: {unique_list},
List that contain duplicate element: {duplicate_list}""")

b. def duplicateList(my_list):
    unique_list = []
    duplicate_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
        elif item not in duplicate_list:
            duplicate_list.append(item)
    return (unique_list,duplicate_list)


my_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
result = duplicateList(my_list)
print("List after removing duplicate is: ",result[0],'\n',"List that contain duplicate element",result[1])

print(f"""List after removing duplicate is: {result[0]},
List that contain duplicate element: {result[1]}""")
o/p:
========
List after removing duplicate is: [1, 2, 3, 4, 5, 6, 7, 8, 9],
List that contain duplicate element: [1, 2, 5, 9]

21. How to sort a list and remove duplicate in python:
=============================================================
i. Approach 1st using set():
=============================
a. my_list = [3,1,4,1,5,9,2,6,5]
unique_list = sorted(set(my_list))
print("List after sorting and removing duplicate is: ",unique_list)

b. def removeDuplicate(my_list):
    unique_list = sorted(set(my_list))
    return unique_list

my_list = [3,1,4,1,5,9,2,6,5]
result = removeDuplicate(my_list)
print("List after sorting and removing duplicate is: ",result)
o/p:
=========
List after sorting and removing duplicate is:  [1, 2, 3, 4, 5, 6, 9]

ii. Approach 2nd using normal approach:
========================================
a. my_list = [3,1,4,1,5,9,2,6,5]
my_list.sort()
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after sorting and removing duplicate is: ",unique_list)

b. def removeDuplicate(my_list):
    my_list.sort()
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [3,1,4,1,5,9,2,6,5]
result = removeDuplicate(my_list)
print("List after sorting and removing duplicate is: ",result)
o/p:
=======
List after sorting and removing duplicate is:  [1, 2, 3, 4, 5, 6, 9]

iii. Approach 3rd using list comprehension:
============================================
a. my_list = [3,1,4,1,5,9,2,6,5]
my_list.sort()
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]
print("List after sorting and removing duplicate is: ",unique_list)

b. def removeDuplicate(my_list):
    my_list.sort()
    unique_list = []
    [unique_list.append(item) for item in my_list if item not in unique_list]
    return unique_list

my_list = [3,1,4,1,5,9,2,6,5]
result = removeDuplicate(my_list)
print("List after sorting and removing duplicate is: ",result)
o/p:
=========
List after sorting and removing duplicate is:  [1, 2, 3, 4, 5, 6, 9]


22. Python program to find unique_list,duplicate_list,unique_count,duplicate_count:
======================================================================================
i. Approach 1st using normal approach:
============================================
a. input_list = [1,2,2,5,8,4,4,8]
unique_list = []
duplicate_list = []
unique_count = 0
duplicate_count = 0
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
        unique_count+=1
    elif item not in duplicate_list:
        duplicate_list.append(item)
        duplicate_count+=1
print("Unique element in the list is: ",unique_list,'\n',"Unique count in the list is: ",unique_count,'\n',"Duplicate element in the list is: ",duplicate_list,'\n',"Duplicate count in the list is: ",duplicate_count)
print(f"""
Unique element in the list is: {unique_list}
Unique count in the list is: {unique_count}
Duplicate element in the list is: {duplicate_list}
Duplicate count in the list is: {duplicate_count}
""")
o/p:
==========
Unique element in the list is: [1, 2, 5, 8, 4]
Unique count in the list is: 5
Duplicate element in the list is: [2, 4, 8]
Duplicate count in the list is: 3

b. def unidupList(input_list):
    unique_list = []
    duplicate_list = []
    unique_count = 0
    duplicate_count = 0
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
            unique_count+=1
        elif item not in duplicate_list:
            duplicate_list.append(item)
            duplicate_count+=1
    return(unique_list,unique_count,duplicate_list,duplicate_count)


input_list = [1,2,2,5,8,4,4,8]
result = unidupList(input_list)
print("Unique element in the list is: ",result[0],'\n',"Unique count in the list is: ",result[1],'\n',"Duplicate element in the list is: ",result[2],'\n',"Duplicate count in the list is: ",result[3])
print(f"""
Unique element in the list is: {result[0]}
Unique count in the list is: {result[1]}
Duplicate element in the list is: {result[2]}
Duplicate count in the list is: {result[3]}
""")
o/p:
===========
Unique element in the list is: [1, 2, 5, 8, 4]
Unique count in the list is: 5
Duplicate element in the list is: [2, 4, 8]
Duplicate count in the list is: 3

23. Python program to merge two list in python:
====================================================
i. Using normal approach:
===============================
a. input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
for item in input_list2:
    input_list1.append(item)
print("List after merging is: ",input_list1)

b. def listMerging(input_list1,input_list2):
    for item in input_list2:
        input_list1.append(item)
    return input_list1

input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
result = listMerging(input_list1,input_list2)
print("List after merging is: ",result)
o/p:
========
List after merging is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ii. Using "+" operator:
=============================
a. input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
merge_list = input_list1 + input_list2
print("List after merging is: ",merge_list)

b. def listMerging(input_list1,input_list2):
    merge_list = input_list1 + input_list2
    return merge_list

input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
result = listMerging(input_list1,input_list2)
print("List after merging is: ",result)
o/p:
========
List after merging is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iii. Using extend() method:
===============================
a. input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
input_list1.extend(input_list2)
print("List after merging is: ",input_list1)

b. def listMerging(input_list1,input_list2):
    input_list1.extend(input_list2)
    return merge_list

input_list1 = [1,2,3,4,5]
input_list2 = [6,7,8,9,10]
result = listMerging(input_list1,input_list2)
print("List after merging is: ",result)
o/p:
=========
List after merging is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


24. Split nested list into two lists:
===============================================
i. Approach 1st Using List Comprehension:
================================================
a. my_list = [[1,2],[4,3],[45,65],[223,2]]
res1 = [item[0] for item in my_list]
res2 = [item[1] for item in my_list]
print("Original nested list before splitting is: ",my_list,'\n',"List one after splitting is: ",res1,'\n',"List two after splitting is: ",res2)
print(f"""
Original nested list before splitting is: {my_list}
List one after splitting is: {res1}
List two after splitting is: {res2}
    """)
o/p:
=======
Original nested list before splitting is: [[1, 2], [4, 3], [45, 65], [223, 2]]
List one after splitting is: [1, 4, 45, 223]
List two after splitting is: [2, 3, 65, 2]


b. def splitList(my_list):
    res1 = [item[0] for item in my_list]
    res2 = [item[1] for item in my_list]
    return(my_list,res1,res2)

my_list = [[1,2],[4,3],[45,65],[223,2]]
result = splitList(my_list)
print("Original nested list before splitting is: ",result[0],'\n',"List one after splitting is: ",result[1],'\n',"List two after splitting is: ",result[2])
print(f"""
Original nested list before splitting is: {result[0]}
List one after splitting is: {result[1]}
List two after splitting is: {result[2]}
    """)
o/p:
==========
Original nested list before splitting is: [[1, 2], [4, 3], [45, 65], [223, 2]]
List one after splitting is: [1, 4, 45, 223]
List two after splitting is: [2, 3, 65, 2]

ii. Approach 2nd Using extend() method:
==============================================
a. my_list = [[1,2],[4,3],[45,65],[223,2]]
res1 = []
res2 = []
x = []
for i in my_list:
    x.extend(i)
print(x)
for i in range(0,len(x)):
    if (i%2==0):
        res1.append(x[i])
    else:
        res2.append(x[i])
print("Original nested list before splitting is: ",my_list,'\n',"List one after splitting is: ",res1,'\n',"List two after splitting is: ",res2)
print(f"""
Original nested list before splitting is: {my_list}
List one after splitting is: {res1}
List two after splitting is: {res2}
    """)
o/p:
=======
[1, 2, 4, 3, 45, 65, 223, 2]
Original nested list before splitting is:  [[1, 2], [4, 3], [45, 65], [223, 2]] 
 List one after splitting is:  [1, 4, 45, 223] 
 List two after splitting is:  [2, 3, 65, 2]


b. def splitList(my_list):
    res1 = []
    res2 = []
    x = []
    for i in my_list:
        x.extend(i)
    print(x)
    for i in range(0,len(x)):
        if i%2==0:
            res1.append(x[i])
        else:
            res2.append(x[i])
    return(my_list,res1,res2)

my_list = [[1,2],[4,3],[45,65],[223,2]]
result = splitList(my_list)
print("Original nested list before splitting is: ",result[0],'\n',"List one after splitting is: ",result[1],'\n',"List two after splitting is: ",result[2])
print(f"""
Original nested list before splitting is: {result[0]}
List one after splitting is: {result[1]}
List two after splitting is: {result[2]}
    """)
o/p:
=========
[1, 2, 4, 3, 45, 65, 223, 2]
Original nested list before splitting is:  [[1, 2], [4, 3], [45, 65], [223, 2]] 
 List one after splitting is:  [1, 4, 45, 223] 
 List two after splitting is:  [2, 3, 65, 2]

25. Python code to find fibonaaci series:
=================================================
i. Using normal approach:
===============================
a. n = 10
a = 0
b = 1
for i in range(n):
    c = a + b
    a = b
    b = c
print("Fibonaaci series is: ",a)

b. def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a
 

n=10
result = fibonacci(n)
print("Fibonaaci series is: ",result)
o/p:
========
Fibonaaci series is:  55

ii. Using recursion():
=======================================
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


result = fibonacci(10)
print("Fibonaaci series is: ",result)
o/p:
=========
Fibonaaci series is:  55

26. Intersection of 2 nested list:
=========================================
i. Using normal approach:
==================================
a. test_list1 = [[1,2],[3,4],[5,6]]
test_list2 = [[3,4],[5,7],[1,2]]
result = []
for item in test_list1:
    if item in test_list2:
        result.append(item)
print("Intersection of two list is: ",result)

b. def intersectionList(test_list1,test_list2):
    result = []
    for item in test_list1:
        if item in test_list2:
            result.append(item)
    return result

test_list1 = [[1,2],[3,4],[5,6]]
test_list2 = [[3,4],[5,7],[1,2]]
result1 = intersectionList(test_list1,test_list2)
print("Intersection of two list is: ",result1)
o/p:
===========
Intersection of two list is:  [[1, 2], [3, 4]]

27. Check if a nested list is a subset of another nested list:
====================================================================
i. Using normal approach:
=================================
a. list1 = [[2,3,1],[4,5],[6,8]]
list2 = [[4,5],[6,8]]
for item in list2:
    if item in list1:
        print("It exist")
    else:
        print("It does not exist")

b. def checkList(list1,list2):
    for item in list2:
        if item in list1:
            print("It exist")
        else:
            print("It does not exist")
            
list1 = [[2,3,1],[4,5],[6,8]]
list2 = [[4,5],[6,8]]
result = checkList(list1,list2)
print(result)
o/p:
==========
It exist
It exist

28. Write a python program to print the data stored in a list along with its address:
=============================================================================================
i. courses = ['sql','python','etl','azure','aws']
for item in courses:
    print(item,id(item))
o/p:
=========
sql 140518096295280
python 140518229028064
etl 140517929371664
azure 140518045550608
aws 140517929371720

ii. def funcList(courses):
    for item in courses:
        print(item, id(item))
    return courses   

courses = ['sql','python','etl','azure','aws']
result = funcList(courses)

print(result[0], result[1])
o/p:
============
sql 140518096295280
python 140518229028064
etl 140517929371664
azure 140518045550608
aws 140517929371720
sql python

iii. def funcList(courses):
    for item in courses:
        print(item, id(item))
       

courses = ['sql','python','etl','azure','aws']
funcList(courses)
o/p:
=========
sql 140518096295280
python 140518229028064
etl 140517929371664
azure 140518045550608
aws 140517929371720

29.WAP to create a list of customers and add any new customer:
1. At the begining of the list:
2. At the end of the list.
3. At the second position from begining.
4. At the second last position.

solution:
===============
1. At the begining of the list:
=========================================
a. customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
customers.insert(0,customer)
print("List after adding customer at beginning is: ",customers)
o/p:
=========
Enter the name of new customer:  Jacob
List after adding customer at beginning is:  ['Jacob', 'Abdul', 'John', 'Yusuf']

b. def beginingList(customers,customer):
    customers.insert(0,customer)
    return customers

customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
result = beginingList(customers,customer)
print("List after adding customer at beginning is: ",result)
o/p:
=========
Enter the name of new customer:  Jacob
List after adding customer at beginning is:  ['Jacob', 'Abdul', 'John', 'Yusuf']

2. At the end of the list:
=========================================
i. customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
customers.append(customer)
print("List after adding customer at end is: ",customers)


ii. def endList(customers,customer):
    customers.append(customer)
    return customers

customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
result = endList(customers,customer)
print("List after adding customer at end is: ",result)
o/p:
==============
Enter the name of new customer:  Jacob
List after adding customer at end is:  ['Abdul', 'John', 'Yusuf', 'Jacob']

3.  At the second position from begining:
===================================================
i. customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
customers.insert(1,customer)
print("List after adding customer at 2nd position from begining is: ",customers)

ii. def secondPosList(customers,customer):
    customers.insert(1,customer)
    return customers

customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
result = secondPosList(customers,customer)
print("List after adding customer at 2nd position from begining is: ",customers)
o/p:
=========
Enter the name of new customer:  Jacob
List after adding customer at 2nd position from begining is:  ['Abdul', 'Jacob', 'John', 'Yusuf']

4. At the second last position:
==========================================
i. customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
customers.insert(-2,customer)
print("List after adding customer at 2nd position from Last is: ",customers)

ii. def secondLastPosList(customers,customer):
    customers.insert(-2,customer)
    return customers

customers = ['Abdul','John','Yusuf']
customer = input("Enter the name of new customer: ")
result = secondPosList(customers,customer)
print("List after adding customer at 2nd position from Last is: ",customers)
o/p:
========
Enter the name of new customer:  Jacob
List after adding customer at 2nd position from Last is:  ['Abdul', 'Jacob', 'John', 'Yusuf']

29. Flatten nested list in Python:
============================================
i. my_list = [1,2,3,[4,5],[6,7]]
result = []
for item in my_list:
    if type(item) == int:
        result.append(item)
    elif type(item) == list:
        for i in range(len(item)):
            result.append(item[i])
print("List after flatten is: ",result)

ii. def flattenNestedList(my_list):
    result = []
    for item in my_list:
        if type(item) == int:
            result.append(item)
        elif type(item) == list:
            for i in range(len(item)):
                result.append(item[i])
    return result

my_list = [1,2,3,[4,5],[6,7]]
result1 = flattenNestedList(my_list)
print("List after flatten is: ",result1)
o/p:'
==========
List after flatten is:  [1, 2, 3, 4, 5, 6, 7]


30. Valid Anagram code:
===================================
i. Approach 1st using sorted():
==========================================
a. str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
if sorted_str1 == sorted_str2:
    print("True")
else:
    print("False")


b. def anagramStringFunc(str1,str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
    
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(anagramStringFunc(str1,str2))


ii. Approach 2nd using sort():
===============================
a. str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
sorted_str1 = list(str1).sort()
sorted_str2 = list(str2).sort()
if sorted_str1 == sorted_str2:
    print("True")
else:
    print("False")

b. def anagramStringFunc(str1,str2):
    sorted_str1 = list(str1).sort()
    sorted_str2 = list(str2).sort()
    if sorted_str1 == sorted_str2:
        return True
    else: 
        return False
    

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(anagramStringFunc(str1,str2))

o/p:
==========
Enter the first string:  abcd
Enter the second string:  bacd
True


iii. Approach 3rd using hashing/dictionary:
======================================================
a. str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
dict1 = {}
for item in str1:
    if item not in dict1:
        dict1[item]=1
    else:
        dict1[item] = dict1[item]+1
for item in str2:
    if item in dict1:
        dict1[item]=dict1[item]-1
    else:
        print("False")
for val in dict1.values():
    if val!=0:
        print("False")
print("True")

b. def hashAnagramFunc(str1,str2):
    dict1 = {}
    for item in str1:
        if item not in dict1:
            dict1[item]=1
        else:
            dict1[item]=dict1[item]+1
    for item in str2:
        if item in dict1:
            dict1[item]=dict1[item]-1
        else:
            return False
    for val in dict1.values():
        if val!=0:
            return False
    return True

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(hashAnagramFunc(str1,str2))
o/p:
========
Enter the first string:  abcd
Enter the second string:  bacd
True

This is most efficeient approach:

iv. Using Counter():
============================
a. from collections import Counter
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
freq_str1 = Counter(str1)
freq_str2 = Counter(str2)
if freq_str1==freq_str2:
    print("True")
else:
    print("False")

b. from collections import Counter
def counterAnagramFunc(str1,str2):
    freq_str1 = Counter(str1)
    freq_str2 = Counter(str2)
    if freq_str1==freq_str2:
        return True
    else: 
        return False
    
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(counterAnagramFunc(str1,str2))
o/p:
=========
Enter the first string:  abcd
Enter the second string:  dacb
True


31. Find the frequency of each element in the list, highest Occurence of element in the list, least Occurence of element in the list:
=================================================================================================================================================
Solution:
=================
i. Approach 1st using normal approach:
=======================================================================
a. lst = [1,10,20,1,30,40,1,1,2]
dict1 = {}
for item in lst:
    if item in dict1:
        dict1[item]=dict1[item]+1
    else:
        dict1[item]=1
max_value = max(dict1.values())
min_value = min(dict1.values())
max_ele = [k for k,v in dict1.items() if v==max_value]
min_ele = [k for k,v in dict1.items() if v==min_value]

print("Frequency of each element in a list: ",dict1,'\n',"Highest Occurence of element in the list is: ",max_ele,'\n',"Least Occurence of element in the list is: ", min_ele)

b. def freqList(lst):
    dict1 = {}
    for item in lst:
        if item in dict1:
            dict1[item]+=1
        else:
            dict1[item]=1
    max_value = max(dict1.values())
    min_value = min(dict1.values())
    max_ele = [k for k,v in dict1.items() if v==max_value]
    min_ele = [k for k,v in dict1.items() if v==min_value]
    return (dict1,max_ele,min_ele)

lst = [1,10,20,1,30,40,1,1,2]
result = freqList(lst)
print("Frequency of each element in a list: ",result[0],'\n',"Highest Occurence of element in the list is: ",result[1],'\n',"Least Occurence of element in the list is: ",result[2])
o/p:
===================
Frequency of each element in a list:  {1: 4, 10: 1, 20: 1, 30: 1, 40: 1, 2: 1} 
 Highest Occurence of element in the list is:  [1] 
 Least Occurence of element in the list is:  [10, 20, 30, 40, 2]


ii. Approach 2nd using Counter():
===============================================
a. from collections import Counter
lst = [1,10,20,1,30,40,1,1,2]
frequency = Counter(lst)
max_value = max(frequency.values())
min_value = min(frequency.values())
max_ele = [k for k,v in frequency.items() if v==max_value]
min_ele = [k for k,v in frequency.items() if v==min_value]

print("Frequency of each element in a list: ",frequency,'\n',"Highest Occurence of element in the list is: ",max_ele,'\n',"Least Occurence of element in the list is: ", min_ele)

b. from collections import Counter
def freqList(lst):
    frequency = Counter(lst)
    max_value = max(frequency.values())
    min_value = min(frequency.values())
    max_ele = [k for k,v in frequency.items() if v==max_value]
    min_ele = [k for k,v in frequency.items() if v==min_value]
    return (frequency,max_ele,min_ele)


lst = [1,10,20,1,30,40,1,1,2]
print("Frequency of each element in a list: ",result[0],'\n',"Highest Occurence of element in the list is: ",result[1],'\n',"Least Occurence of element in the list is: ",result[2])
o/p:
============
Frequency of each element in a list:  {1: 4, 10: 1, 20: 1, 30: 1, 40: 1, 2: 1} 
 Highest Occurence of element in the list is:  [1] 
 Least Occurence of element in the list is:  [10, 20, 30, 40, 2]


32. Find the frequency of each element in the list, highest Occurence of element in the list, least Occurence of element in the list:
=================================================================================================================================================
Solution:
=================
i. Approach 1st using normal approach:
=======================================================================
a. lst = [1,2,3,1,2,1,2,1,2]
dict1 = {}
for item in lst:
    if item in dict1:
        dict1[item]=dict1[item]+1
    else:
        dict1[item]=1
min_value = min(dict1.values())
max_value = max(dict1.values())
max_ele = [k for k,v in dict1.items() if v==max_value]
min_ele = [k for k,v in dict1.items() if v==min_value]
print("Frequency of each element in the list is: ",dict1,'\n',"Highest Occurence of element in the list is: ",max_ele,'\n',"Least Occurence of element in the list is: ",min_ele)

b. def freqCheck(lst):
    dict1 = {}
    for item in lst:
        if item in dict1:
            dict1[item]=dict1[item]+1
        else:
            dict1[item]=1
    max_value = max(dict1.values())
    min_value = min(dict1.values())
    max_ele = [k for k,v in dict1.items() if v==max_value]
    min_ele = [k for k,v in dict1.items() if v==min_value]
    return (dict1,max_ele,min_ele)

lst = [1,2,3,1,2,1,2,1,2]
result = freqCheck(lst)
print("Frequency of each element in the list is: ",result[0],'\n',"Highest Occurence of element in the list is: ",result[1],'\n',"Least Occurence of element in the list is: ",result[2])
o/p:
===================
Frequency of each element in the list is:  {1: 4, 2: 4, 3: 1} 
 Highest Occurence of element in the list is:  [1, 2] 
 Least Occurence of element in the list is:  [3]


ii. Approach 2nd using Counter():
===============================================
a. from collections import Counter
lst = [1,2,3,1,2,1,2,1,2]
frequency = Counter(lst)
max_value = max(frequency.values())
min_value = min(frequency.values())
max_ele = [k for k,v in dict1.items() if v==max_value]
min_ele = [k for k,v in dict1.items() if v==min_value]
print("Frequency of each element in the list is: ",dict1,'\n',"Highest Occurence of element in the list is: ",max_ele,'\n',"Least Occurence of element in the list is: ",min_ele)

b. from collections import Counter
def freqList(lst):
    frequency = Counter(lst)
    max_value = max(frequency.values())
    min_value = min(frequency.values())
    max_ele = [k for k,v in frequency.items() if v==max_value]
    min_ele = [k for k,v in frequency.items() if v==min_value]
    return (frequency,max_ele,min_ele)


lst = [1,2,3,1,2,1,2,1,2]
result = freqList(lst)
print("Frequency of each element in a list: ",result[0],'\n',"Highest Occurence of element in the list is: ",result[1],'\n',"Least Occurence of element in the list is: ",result[2])

o/p:
============
Frequency of each element in a list:  Counter({1: 4, 2: 4, 3: 1}) 
 Highest Occurence of element in the list is:  [1, 2] 
 Least Occurence of element in the list is:  [3]


32. WAP to create a list of various courses may be 3 or 4 course you can store in that list and all must be in upper case.¶
Please ask user to input the course for which he/she wants to enroll.
If the course is found in the list of courses then display ‘course found’. Course search must be case insensitive. 
And if the course is not found then display ‘course not found’ and then add that course in the list of courses at the end.
===========================================================================================================================================================================================================================================================
Solution:
==============
i. courses = ['PYSPARK','SQL','PYTHON']
course = input("Enter the course: ")
if course in courses:
    print("course found")
else:
    print("Course not found")
    courses.append(course)
print("Final course list after performing all operations: ",courses)


ii. def courseFounder(courses,course):
    if course in courses:
        print("course found")
    else:
        print("course not found")
        courses.append(course)
    return courses

courses = ['PYSPARK','SQL','PYTHON']
course = input("Enter the course: ")
result = courseFounder(courses,course)
print("Final course list after performing all operations: ",result)
o/p:
============
Enter the course:  AI
course not found
Final course list after performing all operations:  ['PYSPARK', 'SQL', 'PYTHON', 'AI']



33. WAP to create a list of various courses may be 3 or 4 course you can store in that list and all must be in upper case.¶¶
Please ask user to input the course for which he/she wants to enroll.
If the course is found in the list of courses then display ‘course found’. Course search must be case insensitive. 
And if the course is not found then display ‘course not found’ and then add that course in the list of courses at the beginning.
==========================================================================================================================================
Solution:
==================
i. courses = ['PYSPARK','SQL','PYTHON']
course = input("Enter the course: ")
if course in courses:
    print("course found")
else:
    print("Course not found")
    courses.insert(0,course)
print("Final course list after performing all operations: ",courses)



ii. def courseFounder(courses,course):
    if course in courses:
        print("course found")
    else:
        print("course not found")
        courses.insert(0,course)
    return courses

courses = ['PYSPARK','SQL','PYTHON']
course = input("Enter the course: ")
result = courseFounder(courses,course)
print("Final course list after performing all operations: ",result)
o/p:
=============
Enter the course:  AI
course not found
Final course list after performing all operations:  ['AI', 'PYSPARK', 'SQL', 'PYTHON']

34. Q7.WAP to print first character of each data in a list in upper case.¶
courses=['sql','python','etl']
=========================================================================================
solution:
===================
i. courses=['sql','python','etl']
for item in courses:
    print(item[0].upper())


ii. def courseFounder(courses):
    for item in courses:
        print(item[0].upper())

courses=['sql','python','etl']
courseFounder(courses)
o/p:
==========
S
P
E

35. Q8. WAP to remove the data in a list which starts with upper case.
courses=[‘sql’,’Python’,’etl’]
============================================================================
Solution:
=======================
i. courses=['sql','Python','etl']
print("List before removal is: ",courses)
for item in courses:
    if item[0]==item[0].upper():
        courses.remove(item)
print("Final list after removal is: ",courses)


ii. def courseFounder(courses):
    print("List before removal is: ",courses)
    for item in courses:
        if item[0]==item[0].upper():
            courses.remove(item)
    return courses

courses=['sql','Python','etl']
print("Final list after removal is: ",courseFounder(courses))
o/p:
===========
List before removal is:  ['sql', 'Python', 'etl']
Final list after removal is:  ['sql', 'etl']



36. Print each element of a list using for loop.
===========================================================
i. my_list = ['etl','sql','python','databricks','snowflake','pyspark']
for item in my_list:
    print("Each element of the list in: ",item)
print("Datatype of list is: ",type(my_list))
print("Length of list is: ",len(my_list))


ii. def func(my_list):
    for item in my_list:
        print("Each element of the list in: ",item)
    
    
my_list = ['etl','sql','python','databricks','snowflake','pyspark']
result = func(my_list)
print("Datatype of list is: ",type(my_list))
print("Length of list is: ",len(my_list))
o/p:
============
Each element of the list in:  etl
Each element of the list in:  sql
Each element of the list in:  python
Each element of the list in:  databricks
Each element of the list in:  snowflake
Each element of the list in:  pyspark
Datatype of list is:  <class 'list'>
Length of list is:  6


37. WAP to print each element of a list in upper case.
===========================================================
i. my_list = ['etl','sql','python','databricks','snowflake','pyspark']
for item in my_list:
    print(item.upper(),end=" ")

ii. def func(my_list):
    for item in my_list:
        print(item.upper(),end=" ")

my_list = ['etl','sql','python','databricks','snowflake','pyspark']
func(my_list)

o/p:
===========
ETL SQL PYTHON DATABRICKS SNOWFLAKE PYSPARK


38. WAP to print each element of a list in lower case.
=================================================================
i. my_list = ['ETL','SQL','PYTHON','DATABRICKS','SNOWFLAKE','PYSPARK']
for item in my_list:
    print(item.lower(),end=" ")

ii. def func(my_list):
    for item in my_list:
        print(item.lower(),end=" ")
        
my_list = ['etl','sql','python','databricks','snowflake','pyspark']
func(my_list)
o/p:
===========
etl sql python databricks snowflake pyspark


39. WAP to print count of uppercase and lowercase element in the list:
==================================================================================
i. my_list = ['ETL','SQL','PYTHON','databricks','snowflake','PYSPARK']

cnt_upper = 0
cnt_lower = 0

for item in my_list:
    
    if item.isupper():
        cnt_upper += 1
        
    elif item.islower():
        cnt_lower += 1

print("Count of uppercase item in the list is:", cnt_upper)
print("Count of lowercase item in the list is:", cnt_lower)

ii. def caseCountFunc(my_list):
    cnt_lower = 0
    cnt_upper = 0
    for item in my_list:
        if item.isupper():
            cnt_upper+=1
        elif item.islower():
            cnt_lower+=1
    return(cnt_upper,cnt_lower)

my_list = ['ETL','SQL','PYTHON','databricks','snowflake','PYSPARK']
result = caseCountFunc(my_list)
print("Count of uppercase item in the list is:",result[0],'\n',"Count of lowercase item in the list is:",result[1])
o/p:
==========
Count of uppercase item in the list is: 4
Count of lowercase item in the list is: 2

40.  WAP to print each and every element of below list.
Nested_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
==========================================================================
i. nested_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for item in nested_list:
    print(item,end=" ")
    print(item[0],'\n',item[1],'\n',item[2])
print("Length of nested_list is: ",len(item))
print("DataType of list is: ",type(nested_list))
print("Datatype is: ",type(item))


ii. def funcList(nested_list):
    for item in nested_list:
        print(item,end=" ")
        print(item[0],'\n',item[1],'\n',item[2])
 
nested_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
funcList(nested_list)
print("Length of nested_list is: ",len(item))
print("DataType of list is: ",type(nested_list))
print("Datatype is: ",type(item))
o/p:
============
[1, 2, 3] 1 
 2 
 3
[4, 5, 6] 4 
 5 
 6
[7, 8, 9] 7 
 8 
 9
[10, 11, 12] 10 
 11 
 12
Length of nested_list is:  3
DataType of list is:  <class 'list'>
Datatype is:  <class 'list'>

41. How to compare 2 lists and get common and uncommon elements in Python:
===================================================================================
1. Using normal approach:
===========================================
i. lst1 = [10,20,30,40]
lst2 = [10,20,300,400]
resut_common = []
uncommon_lst = []
for item in lst1:
    if item in lst2:
        resut_common.append(item)
    elif item not in lst2:
        uncommon_lst.append(item)
        
print("Common element from both list is: ",resut_common,'\n',"Uncommon element from both list is: ",uncommon_lst)


ii. def listReader(lst1,lst2):
    result_common = []
    uncommon_lst = []
    for item in lst1:
        if item in lst2:
            result_common.append(item)
        elif item not in lst2:
            uncommon_lst.append(item)
    return(result_common,uncommon_lst)


lst1 = [10,20,30,40]
lst2 = [10,20,300,400]
result = listReader(lst1,lst2)
print("Common element from both list is: ",result[0],'\n',"Uncommon element from both list is: ",result[1])
o/p:
==========
Common element from both list is:  [10, 20] 
Uncommon element from both list is:  [30, 40]

2. Using set():
============================================
i. lst1 = [10,20,30,40]
lst2 = [10,20,300,400]
common_set = set(lst1).intersection(set(lst2))
common_elements = list(common_set)
uncommon_set = set(lst1).symmetric_difference(set(lst2))
uncommon_elements = list(uncommon_set)
print("Common element from both list is: ",common_elements,'\n',"Uncommon element from both list is: ",uncommon_elements)


ii. def funcList(lst1,lst2):
    common_set = set(lst1).intersection(set(lst2))
    common_list = list(common_set)
    uncommon_set = set(lst1).symmetric_difference(set(lst2))
    uncommon_list = list(uncommon_set)
    return (common_list,uncommon_list)

lst1 = [10,20,30,40]
lst2 = [10,20,300,400]
result = funcList(lst1,lst2)
print("Common element from both list is: ",result[0],'\n',"Uncommon element from both list is: ",result[1])
o/p:
============
Common element from both list is:  [10, 20] 
Uncommon element from both list is:  [40, 300, 400, 30]


41. WAP to print the numbers which are less than the average from the below list.
numbers=[1,2,3,4,5,6,7,8,9]:
=============================================================================================================
i. numbers = [1,2,3,4,5,6,7,8,9]

total_value = sum(numbers)
total_count = len(numbers)

avg_number = total_value / total_count

result = []

for num in numbers:
    if num < avg_number:
        result.append(num)

print("Numbers which are less than average number from list:", result)
print("Average number from list is:", avg_number)


ii. def numberChecker(numbers):
    total_value = sum(numbers)
    total_count = len(numbers)
    avg_number = total_value/total_count
    result = []
    for num in numbers:
        if num<avg_number:
            result.append(num)
    return result

numbers=[1,2,3,4,5,6,7,8,9]
print("Numbers which are less than average number from list: ",numberChecker(numbers))
print("Average number from list is:", avg_number)
o/p:
========
Numbers which are less than average number from list:  [1, 2, 3, 4]
Average number from list is: 5.0

42. WAP to print only even numbers, odd numbers  from the below list.
numbers=[1,2,3,4,5,6,7,8,9]
===========================================================================
i. numbers=[1,2,3,4,5,6,7,8,9]
even_list = []
odd_list = []
for num in numbers:
    if num%2==0:
        even_list.append(num)
    elif num%2!=0:
        odd_list.append(num)
print("Even number in the list is: ",even_list,'\n',"Odd number in the list is: ",odd_list)

ii. def numberChecker(numbers):
    even_list = []
    odd_list = []
    for num in numbers:
        if num%2==0:
            even_list.append(num)
        elif num%2!=0:
            odd_list.append(num)
    return(numbers,even_list,odd_list)

numbers=[1,2,3,4,5,6,7,8,9]
result = numberChecker(numbers)
print("Even number in the list is: ",result[1],'\n',"Odd number in the list is: ",result[2])
o/p:
==========
Even number in the list is:  [2, 4, 6, 8] 
Odd number in the list is:  [1, 3, 5, 7, 9]

43.WAP to create a list of courses and take a course as an input from user and delete it from the list. Display the elements of list before deletion and after deletion.
====================================================================================================================================================================================
i. courses=['sql','python','etl']
course = input("Enter the course: ")
print("Course before deletion is: ",courses)
for item in courses:
    if item == course:
        courses.remove(item)
print("Course after deletion is: ",courses)

ii. def courseChecker(courses):
    print("Course before deletion is: ",courses)
    for item in courses:
        if item == course:
            courses.remove(item)
    return(courses)

courses=['sql','python','etl']
course = input("Enter the course: ")
print("Course after deletion is: ",courseChecker(courses))
o/p:
==========
Enter the course:  etl
Course before deletion is:  ['sql', 'python', 'etl']
Course after deletion is:  ['sql', 'python']


43. Python program move all zeros to end of the list in python:
===========================================================================
i. a = [1,3,0,5,4,0,3,2]
b = []
for item in a:
    if item != 0:
        b.append(item)
for item in a:
    if item == 0:
        b.append(item)
print("Before moving zero to end of the list in python: ",a)
print("After moving zero to end of the list in python: ",b)


ii. def movingZeros(a):
    b=[]
    for item in a:
        if item != 0:
            b.append(item)
    
    for item in a:
        if item == 0:
            b.append(item)
    return b

a = [1,3,0,5,4,0,3,2]
print("Before moving zero to end of the list in python: ",a)
print("After moving zero to end of the list in python: ",movingZeros(a))
o/p:
========
Before moving zero to end of the list in python:  [1, 3, 0, 5, 4, 0, 3, 2]
After moving zero to end of the list in python:  [1, 3, 5, 4, 3, 2, 0, 0]


44. Python program to find how may strings , integers, float values are there in a list:
==============================================================================================
i. lst = [10,20,'aaa','bbb',33.5,'ccc',88,'bbb',25]
str_count = 0
int_count = 0
float_count = 0

for item in lst:
    
    if type(item) == str:
        str_count += 1
        
    elif type(item) == float:
        float_count += 1
        
    else:
        int_count += 1
        
print("String count in list is: ",str_count,'\n',"Integer count in list is: ",int_count,'\n',"Float count in the list is: ",float_count)
print(f"""
String count in list is: {str_count}
Integer count in list is: {int_count}
Float count in the list is: {float_count}
""")
        

ii. def listChecker(lst):
    str_count = 0
    int_count = 0
    float_count = 0
    for item in lst:
        if type(item) == str:
            str_count += 1
        elif type(item) == float:
            float_count += 1
        else:
            int_count += 1
    return (str_count,int_count,float_count)

lst = [10,20,'aaa','bbb',33.5,'ccc',88,'bbb',25]
result = listChecker(lst)
print("String count in list is: ",result[0],'\n',"Integer count in list is: ",result[1],'\n',"Float count in the list is: ",result[2])
print(f"""
String count in list is: {result[0]}
Integer count in list is: {result[1]}
Float count in the list is: {result[2]}
""")
o/p:
========
String count in list is:  4 
 Integer count in list is:  4 
 Float count in the list is:  1


45. Two training institutes are interested in a merger. Write a program to create a new list of courses after merging the courses from each institute, ensuring it is case-sensitive.
=====================================================================================================================================================================================
i. Approach 1st using concate "+" :
=======================================================
a. institute1_courses = ['SQL', 'Python', 'ETL']
institute2_courses = ['Data Science', 'Machine Learning', 'Python']
merged_course = institute1_courses + institute2_courses
final_merged = list(set(merged_course))
print("After merging the list is: ",final_merged)


b. def mergedList(institute1_courses,institute2_courses):
    merged_course = institute1_courses + institute2_courses
    final_merged = list(set(merged_course))
    return final_merged

institute1_courses = ['SQL', 'Python', 'ETL']
institute2_courses = ['Data Science', 'Machine Learning', 'Python']
result = mergedList(institute1_courses,institute2_courses)
print("After merging the list is: ",result)
o/p:
==========
After merging the list is:  ['SQL', 'Python', 'Data Science', 'ETL', 'Machine Learning']


ii. Approach 2nd using extend():
=========================================
a. institute1_courses = ['SQL', 'Python', 'ETL']
institute2_courses = ['Data Science', 'Machine Learning', 'Python']
institute1_courses.extend(institute2_courses)
merged_course = list(set(institute1_courses))
print("After merging the list is: ",merged_course)


b. def mergedList(institute1_courses,institute2_courses):
    institute1_courses.extend(institute2_courses)
    merged_course = institute1_courses
    final_course = list(set(merged_course))
    return final_courseun

institute1_courses = ['SQL', 'Python', 'ETL']
institute2_courses = ['Data Science', 'Machine Learning', 'Python']
result = mergedList(institute1_courses,institute2_courses)
print("After merging the list is: ",result)
o/p:
===========
After merging the list is:  ['SQL', 'Python', 'Data Science', 'ETL', 'Machine Learning']


46. WAP to check whether duplicate data exist in a list or not and display the message accordingly.
==================================================================================================================
i. Approach 1st :
===========================
a. data = [1, 2, 3, 4, 5, 2]

unique_list = []
duplicate_list = []

unique_count = 0
duplicate_count = 0

for item in data:
    if item not in unique_list:
        unique_list.append(item)
        unique_count += 1

    elif item not in duplicate_list:
        duplicate_list.append(item)
        duplicate_count += 1

print(
    "Unique element in the list is:", unique_list, '\n',
    "Unique count of element is:", unique_count, '\n',
    "Duplicate element in the list is:", duplicate_list, '\n',
    "Duplicate count of element is:", duplicate_count
)


b. def duplicateCheckList(data):
    unique_list = []
    duplicate_list = []
    unique_count = 0
    duplicate_count = 0
    for item in data:
        if item not in unique_list:
            unique_list.append(item)
            unique_count+=1
        elif item not in duplicate_list:
            duplicate_count+=1
            duplicate_list.append(item)
    return(unique_list,duplicate_list,unique_count,duplicate_count)

data = [1, 2, 3, 4, 5, 2]
result = duplicateCheckList(data)
print(
    "Unique element in the list is:", result[0], '\n',
    "Unique count of element is:", result[2], '\n',
    "Duplicate element in the list is:", result[1], '\n',
    "Duplicate count of element is:", result[3]
)
o/p:
===========
Unique element in the list is: [1, 2, 3, 4, 5] 
 Unique count of element is: 5 
 Duplicate element in the list is: [2] 
 Duplicate count of element is: 1


47. Identify unique values from a list of numbers and print how many times each value occurs:
=====================================================================================================
i. Approach 1st :
=========================
a. lst = [5,3,5,6,3,5,7]
dict1 = {}
unique_value = list(set(lst))
unique_count = len(unique_value)
for item in lst:
    if item not in dict1:
        dict1[item]=1
    else:
        dict1[item]+=1
print("Unique element in the list is: ",unique_value,'\n',"Occurence of each element in the list is: ",dict1,
      '\n',"Unique count of element in the list is: ",unique_count)
      
print(f"""
Unique element in the list is: {unique_value}
Unique count in the list is: {unique_count}
Occurence of each element in the list is: {dict1}""")
o/p:
==========
Unique element in the list is: [3, 5, 6, 7]
Unique count in the list is: 4
Occurence of each element in the list is: {5: 3, 3: 2, 6: 1, 7: 1}


b. def elementCheckerFunc(lst):
    dict1 = {}
    unique_value = list(set(lst))
    unique_count = len(unique_value)
    for item in lst:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item]+=1
    return (unique_value,unique_count,dict1)

lst = [5,3,5,6,3,5,7]
result = elementCheckerFunc(lst)
print("Unique element in the list is: ",result[0],'\n',"Unique count of element in the list is: ",result[1],'\n',"Occurence of each element in the list is: ",result[2])

print(f"""
Unique element in the list is: {result[0]}
Unique count in the list is: {result[1]}
Occurence of each element in the list is: {result[2]}""")
o/p:
==========
Unique element in the list is: [3, 5, 6, 7]
Unique count in the list is: 4
Occurence of each element in the list is: {5: 3, 3: 2, 6: 1, 7: 1}


48. Write a Python program that asks the user to input their age. If the age is between 13 and 17 (inclusive), print "You are not eligible to vote." Otherwise, print "You are eligible to vote.":
==================================================================================================================================================================================================
Solution:
=================
i. age = int(input("Enter the value of age: "))
if age>=13 and age<=17:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
    

ii. def voterCheckFunc(age):
    if age>=13 and age<=17:
        return "You are not eligible to vote"
    else:
        return "You are eligible to vote"

age = int(input("Enter the value of age: "))
print(voterCheckFunc(age))
o/p:
===========
Enter the value of age:  16
You are not eligible to vote


49. Write a Python program that asks the user to input a number. If the number is even, print "The number is even." If the number is odd, print "The number is odd."
===========================================================================================================================================================================
i. num = int(input("Enter the value of number: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")


ii. def numCheckFunc(num):
    if num%2==0:
        return "Number is even"
    else:
        return "Number is odd"

num = int(input("Enter the value of number: "))
print(numCheckFunc(num))
o/p:
============
Enter the value of number:  18
Number is even


50. Write a Python program that asks the user to input a number. If the number is positive, print "Positive". If it is negative, print "Negative". If it is zero, print "Zero". 
Additionally, if the number is positive, check if it is even or odd and print the corresponding message.
===============================================================================================================================================================================
i. num = int(input("Enter the value of number: "))

if num > 0:
    if num % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")
    

ii. def numCheckFunc(num):
    if num>0:
        if num%2==0:
            return "Number is positive and even"
        else:
            return "Number is positive and odd"
    elif num<0:
        return "Number is negative"
    else:
        return "Number is zero"
    
num = int(input("Enter the value of number: "))
print(numCheckFunc(num))
o/p:
===============
Enter the value of number:  18
Number is positive and even


iii. num = int(input("Enter the value of number: "))
if num>0 and num%2==0:
    print("Number is positive and even")
elif num>0 and num%2!=0:
    print("Number is positive and odd")
elif num<0:
    print("Number is negative")
else:
    print("Number is zero")
    

iv. def numCheckFunc(num):
    if num>0 and num%2==0:
        return "Number is positive and even"
    elif num>0 and num%2!=0:
        return "Number is positive and odd"
    elif num<0:
        return "Number is negative"
    else:
        return "Number is zero"


num = int(input("Enter the value of number: "))
print(numCheckFunc(num))
o/p:
===========
Enter the value of number:  18
Number is positive and even


51. Q4. Write a Python program that asks the user to input their score (0-100) and prints the corresponding grade based on the following criteria:
• A: 90-100
• B: 80-89
• C: 70-79
• D: 60-69
• F: 0-59
====================================================================================================================================================
i. scores = int(input("Enter the value of score: "))
if scores>=90 and scores<=100:
    print("A")
elif scores>=80 and scores<=89:
    print("B")
elif scores>=70 and scores<=79:
    print("C")
elif scores>=60 and scores<=69:
    print("D")
elif scores>=0 and scores<=59:
    print("F")
o/p:
=============
Enter the value of score:  60
D


ii. def gradeSystem(scores):
    if scores>=90 and scores<=100:
        print("A")
    elif scores>=80 and scores<=89:
        print("B")
    elif scores>=70 and scores<=79:
        print("C")
    elif scores>=60 and scores<=69:
        print("D")
    elif scores>=0 and scores<=59:
        print("F")

scores = int(input("Enter the value of score: "))
gradeSystem(scores)
o/p:
=========
Enter the value of score:  96
A


52. Write a Python program that asks the user to input a single character and checks if it is a vowel or consonant. Assume the input is a lowercase letter.
=================================================================================================================================================================
i. char = input("Enter a single character: ")

if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
o/p:
=========
Enter a single character:  a
a is a vowel.

ii. def vowelCheck(char):
    if char in 'aeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

char = input("Enter a single character: ")
vowelCheck(char)
o/p:
=========
Enter a single character:  a
a is a vowel


53.  Write a Python program that asks the user for their age and checks if they are eligible to vote. The voting age is 18 years and older.
============================================================================================================================================================
i. age = int(input("Enter the value of age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
    


ii. def voterCheckList(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"
    
age = int(input("Enter the value of age: "))
print(voterCheckList(age))
o/p:
=============
Enter the value of age:  35
Eligible to vote


54. Write a Python program that asks the user to input three numbers and prints the largest of the three.
===================================================================================================================
i. a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a>b and a>c:
    print(f"{a} is largest")
elif b>a and b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
    

ii. def largestElement(a,b,c):
    if a>b and a>c:
        return(f"{a} is largest")
    elif b>a and b>c:
        return(f"{b} is largest")
    else:
        return(f"{c} is largest")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
print(largestElement(a,b,c))
o/p:
============
Enter the value of a:  15
Enter the value of b:  10
Enter the value of c:  5
15 is largest


55. Write a Python program that asks the user to input a number and checks if it is divisible by both 5 and 11.
=======================================================================================================================
i. num = int(input("Enter the value of number: "))
if (num%5==0 and num%11==0):
    print(f"{num} is divisble by 5 and 11")
else:
    print(f"{num} is not divisble by 5 and 11")
    
 
ii. def numDivisible(num):
    if (num%5==0 and num%11==0):
        return(f"{num} is divisble by 5 and 11")
    else:
        return(f"{num} is not divisble by 5 and 11")
    
    
num = int(input("Enter the value of number: "))
print(numDivisible(num))
o/p:
===========
Enter the value of number:  55
55 is divisble by 5 and 11


56. Two pair sum using pyton:
=================================================
input:
===================
my_list = [1,2,3,4,5,6,7,8]

output:
============
Return all the pair of number which sums up to 9.


Solution:
=======================
Approach 1st:
===================
a. my_list = [1,2,3,4,5,6,7,8]
pair_list = []
sum = 9
for i in my_list:
    for j in my_list:
        if i+j == 9:
            pair_list.append((i,j))
print("Two pair sum in a list is: ",pair_list)

b. def pairListSum(my_list,pair_list):
    for i in my_list:
        for j in my_list:
            if i+j == 9:
                pair_list.append((i,j))
    return pair_list

my_list = [1,2,3,4,5,6,7,8]
pair_list = []
result = pairListSum(my_list,pair_list)
print("Two pair sum in a list is: ",result)
o/p:
==========
Two pair sum in a list is:  [(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)]


Approach 2nd:
=======================
a. my_list = [1, 2, 3, 4, 5, 6, 7, 8]
pair_list = []

x = len(my_list)

for i in range(0, x):
    for j in range(i + 1, x):
        if my_list[i] + my_list[j] == 9:
            pair_list.append((my_list[i], my_list[j]))

print("Two pair sum in a list is:", pair_list)


b. def pairListSum(my_list,pair_list):
    x = len(my_list)
    for i in range(0,x):
        for j in range(i+1,x):
            if my_list[i] + my_list[j] == 9:
                pair_list.append((my_list[i],my_list[j]))
    return pair_list

my_list = [1,2,3,4,5,6,7,8]
pair_list = []
result = pairListSum(my_list,pair_list)
print("Two pair sum in a list is: ",result)
o/p:
==========
Two pair sum in a list is:  [(1, 8), (2, 7), (3, 6), (4, 5)]