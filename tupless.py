""" immutable """
"""1- to define a tuple"""
myt= ()
myt2 = tuple()
t = (3, 5, 6, 'iti', 'test', True, 44.4, None, "iti", "iti")  # can contain different values from different datatypes
#
#
"2- get len of tuple"
print(len(t))
#
"3- count element occurrence in the tuple"
print(t.count('iti'))

'4- get index of element in the tuple ?'
print(t.index('iti'))
#
'5- tuple can hold another tuple '
t = (3, 5, 6, 'iti', 'test', True, 44.4,(4.5,666,555),  None, "iti", "iti")
print(t)
#
"6- access elements of the tuple using index"
print(t[4])
print(t[7][2])
#






"""13- tuple concat"""


t1= ('python', 'django')
t2= ('flask', 'odoo', 'fast')
#
courses= t1 + t2
print(courses)
#





"""get min , max from the tuple ? ---> depends on compare  -->tuple items must be from the same type"""
print(min(t1))


"""loop over the tuple ? """
for item in t:
    print(f"item = {item}")

#
count = 0
for item in t:
    print(f"index ={count}, item = {item}")
    count +=1
#
#
""" enumurate ---> create index for iterable"""
t_enum = enumerate(t)
#
# print(t_enum)  #<enumerate object at 0x7fb090f90180>
#
for index , val in t_enum:
    print(f"{index}:{val}")

#

### cast string to tuple ?
name = 'ahmed'
name = tuple(name)
print(name)
#
# "use enumerate with string"
#
# """ convert tuple of strings to on string"""
#
myinfo=("my", 'name','is','noha')
mystr = ' '.join(myinfo)
print(mystr)
#
#
""" generate tuple of numbers in python """
## range ?

nums = range(10)
print(nums)
nums = tuple(nums)
print(nums)
#
# # nums = range(1,10, 2)
# # print(nums)
# # nums = tuple(nums)
# # print(nums)
#
# nums = range(10,-1, -1)
# print(nums)
# nums = tuple(nums)
# print(nums)
#

""" in operator """
print("iti" in t)

"tuple of one item ? "

myt = ("ali",)
print(myt, type(myt))