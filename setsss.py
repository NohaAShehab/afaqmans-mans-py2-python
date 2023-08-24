

"1- define a set "

ss= set()
#
# """2- set can hold different data from different datatypes like tuple, int , str"""
#
# myset = {"test", 10, "iti", 99.4, True, "iti", None}
# print(myset)
# """ unordered datatype """
# """ no index """

s = {'ahmed', 'ali', ('abc', 'mm', 'ff')}
print(s)

# s = {'ahmed', 'ali', ['abc', 'mm', 'ff']}
# print(s)

""" set can hold hashable datatypes  --> immutable datatype"""

""" set  ---> hash elements 
'iti' --> hashing algorithm  ----> value 
'iti' ? 
set doesn't allow duplication 

tuple .. ok  --> immutable
list .. No ? mutable
"""

""" add element to the set ? """
s.add('abc')
print(s)

"pop element from the set "
popped_element = s.pop()
print(s)
print(popped_element)

"loop"

for ele in s :
    print(f"-->{ele}")

"check if element exists in set ? "
print('iti' in s)

"remove specific element from the set ? "

s.remove('abc')