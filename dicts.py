
info = ['noha' ,'iti', 31, 'cairo']

""" list , tuple, set ---> unlabeled data"""

"""you need to use new datatype ---> meaning of the data --> datalabel"""

"""
    keyword : value
    
    ---> keyword :  unique
    --> sets --> unique items 
    --> dict --> keys ---> unique
"""

"""1- construct a dict """

d = {}
myd = dict()

""" comma seperated , key:value pair """

info = {
    "name":"noha", "age":31, 'work':'iti', 'country':'egypt',
    "work":"Information Technology Institute"
}

print(info)

"""access dict elements using key"""
print(info['name'])

"""dicts are mutable datatypes"""
info['name'] ='Noha Shehab'  # update the value of existing keys
print(info)

info['city']='Mansoura'   # add new key:value pair to the dict
print(info)

"""get len of dict """
print(len(info))
"""loop over the dict """
for element in info:
    print(f"---> {element}: {info[element]}")

""" check element exists in the dict"""
print(31 in info)  # in --> check if the values exists in the keys

"""You somthing ---> enables you to search in dict values """

# "1- get dict keys"
# keys = info.keys() # dict_keys --> cast it to list
# print(keys)
# keys_list = list(keys)
# print(keys_list)

"1- get dict values"
values = info.values() # dict_keys --> cast it to list
print(values)
values_list = list(values)
print(values_list)

print(31 in info.values())

"""dict items """
d_items = info.items()
print(d_items)  # dict_items

for k , v in info.items():
    print(f"{k}:{v}")

"update dict "

additional_info = {"salary":1000, 'email':'n@gmail.com'}

info.update(additional_info)
print(info)

#
# info.clear()
# print(info)

# del --> remove varaible from memory

""" remove key value pair from dict """

# del info["name"]
""" pop key, value from dict """
popped_element=info.pop("name")


