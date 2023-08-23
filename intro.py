"python --> you must start script from the beginning of line, you must follow the indentation rules"
""" variable ?  ===> name refers to memory location """

#
# """
#     if(name==='ahmed'){
#         console.log('hii');
#     }
#
# """
#
#
# # name ='ahmed'
# #
# # if name=='ahmed':
# #     print('---hi')
# # else:
# #     print('----bye ----')
#
#
# message = 'hi'  # string
# message2 = "bye"  # string
#
# "multi line string ? "
# #
# # bio = 'My name is Noha' \
# #       'I works at ITI' \
# #       'I lives in cairo'
# #
# # print(bio)
#
#
# # bio = """My name is Noha
# # I works at ITI
# # I lives in cairo"""
# # print(bio)
#
# bio = '''My name is Noha
# I works at ITI
# I lives in cairo'''
# print(bio)
#
#
# # this is a comment
# print('test')
#
#
# """string without ref --> can be act like a comment"""
#
#
# name = 'tasneem'
# grade = 100
# happy =  True
#
# """ when you define a variable --> interpreter detect datatype in the runtime"""
#
# """ python is loosely dynamically typed lang?
#
#     --> 1- detect datatype in the runtime
#     --> 2- you can change datatype
# """
#
# ######################################################
# "print type of variable "
# name = 'ahmed'
# print(type(name))  # class str --->
# """
#     all datatypes in python are python classes
# """
# print(type(55))
# print(type(None))
# print(type(5.5))
# """
#     boolean
#     True
#     False
# """


"""convert between different types ? """
year = 2023  # int

year = str(year)

print(year, type(year))

# message  = 'hi'
# message = bool(message)

#
# message  = ' '
# message = bool(message)


message  = ''
message = bool(message)

""" empty strings  --> casted to bool 0--> false 

'        ' --> this string is not empty --> string contain spaces (space is special char.)

"""

# val = None
# val = bool(val)
# print(val)

""" convert string to an int """
# age = '31'
#
# age = int(age)
# print(age, type(age))

# age = 'iti'
# age = int(age)
# print(age, type(age))

""" string can be converted to int only if the string contains digits 0-->9"""

# numm = '4555.4444'
# print(int(numm))
#
# numm = '4555.4444'
# print(float(numm))
#
#
# myname = 'n'
# print(int(myname))


num=10000000000000000000007566453453432342342345678908765436789
print(num)


""" size of int , string in python """



print("iti" and 'Ahmed')


# print(bool('rawan'))  # rawan represent True

print('ahmed' and '')

print('test' and 'ahmed' and True and '              ')

print('ahmed' or 'iti')

print('' or True or 10)
