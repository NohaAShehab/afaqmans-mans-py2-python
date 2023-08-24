# def helloworld():
#     pass
#
# "call the function"
# r= helloworld()
# print(r)  # None

# def helloworld():
#     return
#
# "call the function"
# r= helloworld()
# print(r)  # None

""
# def helloworld():
#     print("--- hello world ---")
#
# "call the function"
# r= helloworld()
# print(r)  # None

""" function accept arguments and return with res  """
# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res

# r = sumnum(10 , 20)
# print(r)

"""  function with default arguments"""
#
# def sumnum(num1=10, num2=9):
#     print(f'num1= {num1}, num2= {num2}')
#     res = num1 + num2
#     print(res)
#     return res
#
# sumnum(5)
# sumnum(4,5)
# sumnum()
#
# print('hii', end='||')
# print('byeee')
# print(3,4,56,6, sep='|__$$__|')

"---------------------------------------------------------------"
#
# def sumnums(num1, num2):
#     res = num1 + num2
#     print(res)
#
#
# sumnums(10,20)
# sumnums('10', '20')
# sumnums('ahmed','mohamed')
# sumnums(3,'ggg')


# def sumnums(num1:int, num2:int):
#     res = num1 + num2
#     print(res)
#
#
# sumnums(10,20)
# sumnums('10', '20')
# sumnums('ahmed','mohamed')
# sumnums(3,'ggg')


### manaul check for the datatype

# print(isinstance(10, int))
# print(isinstance('noha', int))
#
#
# def sumnums(num1: int, num2: int):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#     else:
#         print("---- num1, num2 should be integers")
#
#
# #
#
# sumnums(10, 20)
# sumnums('10', '20')
# sumnums('ahmed', 'mohamed')
# sumnums(3, 'ggg')

#
#
#
#
""" function with variable number of arguments """
print()
print(345,56,6)
print(44)


# def askforstudents(*students):  # * zero or more
#     print(students)
#
#
# askforstudents()
# askforstudents('ahmed')
# askforstudents('4345','3434', 'erer')


""" ** -> keyword arguments """

def introduceyourself(**info):
    print(info) # dict 


introduceyourself(name='ahmed')
introduceyourself()
introduceyourself(fname='ddd', lname='ddd')

