""" the versatile datatype in python"""
"""1- to define a list"""
myl = []
myl2 = list()
l = [3, 5, 6, 'iti', 'test', True, 44.4, None, "iti", "iti"]  # can contain different values from different datatypes


"2- get len of list"
print(len(l))

"3- count element occurrence in the list"
print(l.count('iti'))

'4- get index of element in the list ?'
print(l.index('iti'))

'5- list can hold another list '
l = [3, 5, 6, 'iti', 'test', True, 44.4,[4.5,666,555],  None, "iti", "iti"]
print(l)

"6- access elements of the list using index"
print(l[4])
print(l[7][2])

" list is mutable datatype "
"7- update  elements at existing indices "
l[4] = 'updated'
# print(l)
# l[30]='iti'
"8- append new element --> to the end of the list"
l.append("added element")

"9- insert element at certain index? "
l.insert(8, 'inserted element')
l.insert(20, 'myelement')

"""10- pop element"""
popped_el = l.pop()  # retrun with the popped element
print(l)
print(popped_el)

"11-pop element at certain index "
# popped_el=l.pop(10)
# print(popped_el)

"12-remove element"
l.remove('iti')
print(l)

"""13- list concat"""


l1= ['python', 'django']
l2= ['flask', 'odoo', 'fast']

courses= l1 + l2
print(courses)

"""14- extend a list? """
l1.extend(l2)
print(l1)
print(l2)

""" sort list ---> list items must be from the same type """

"sort list itself"
# l1.sort()  # asc
# print(l1)

l1.sort(reverse=True)  # asc
print(l1)

""" reverse a list"""
print(l)
l.reverse()
print(l)


"""get min , max from the list ? ---> depends on compare  -->list items must be from the same type"""
print(min(l1))


"""loop over the list ? """
# for item in l:
#     print(f"item = {item}")
#
#
# count = 0
# for item in l:
#     print(f"index ={count}, item = {item}")
#     count +=1


""" enumurate ---> create index for iterable"""
l_enum = enumerate(l)

print(l_enum)  #<enumerate object at 0x7fb090f90180>

# for index , val in l_enum:
#     print(f"{index}:{val}")



### cast string to list ?
name = 'ahmed'
name = list(name)
print(name)

"use enumerate with string"

""" convert list of strings to on string"""

myinfo=["my", 'name','is','noha']
mystr = ' '.join(myinfo)
print(mystr)

""" split string  a list """

message = 'I love python'
print(message.split(' '))

""" generate list of numbers in python """
## range ?

# nums = range(10)
# print(nums)
# nums = list(nums)
# print(nums)

# nums = range(1,10, 2)
# print(nums)
# nums = list(nums)
# print(nums)

nums = range(10,-1, -1)
print(nums)
nums = list(nums)
print(nums)


""" in operator """
print("iti" in l)