"1- define string "
#
# mymessage='hello world'
#
# """ access parts using index  starts from 0 """
# print(mymessage[6])
#
# "get len of string"
# print(len(mymessage))
#
# "slicing the string "
# print(mymessage[3:])
# print(mymessage[3:8])
# print(mymessage[8:3:-1])
# print(mymessage[::-1])
#
# """count char occurence in the string """
# print(mymessage.count('o'))
#
# "get index of char in the string "
# print(mymessage.index('o'))  #return index of the first occurence of the char
#
# """ check if char exists in the string """
# print('o' in mymessage)
#
# """ string is sequence """
# for char  in mymessage:
#     print(char)
#
# """---> string is immutable ----once created cannot be changed """
# "any operation on the string will return new string "
# course = 'python course'
# print(course.upper())  # new string
# print(course.lower())
# print(course.title())
# print(course.capitalize())
#
# """ format string ? """
# "1-string concat"
# fname = 'noha'
# midname  = 'abdelhady'
# lname = 'shehab'
#
# # fullname = fname + midname + midname + lname
# # print(fullname)
#
# """ string interpolation"""
# fullname = fname + midname *2 + lname
# print(fullname)
#
# """ replace part of the string """
#
# # msg = 'hello world ooooooooo'
# # print(msg.replace('o', '@', 4))
#
#
# #
# # temp = "my name is {0} I works at {1}"
# #
# # # print(temp.format('noha', 'iti'))
# #
# # print(temp.format( 'iti', 'noha'))
#
#
#
# temp = "my name is {username} I works at {userwork}"
#
# # print(temp.format('noha', 'iti'))
#
# print(temp.format( userwork='iti', username='noha'))  # format string using keyword argument.
#
#
#
# """ ask user to enter input """
#
# fname = input("please enter name: ")  # always return with string
# print(fname, type(fname))
# lname = input("please enter lname ")
#
# """f-format string  =--> based on existing variables"""
# fullname = f"{fname} {lname}"
# print(fullname)


""" examine content of the string ? """
#
# msg = input("please enter message ")
# print(msg.islower())
# print(msg.isupper())
# print(msg.isspace())  # true if the string consists only from spaces
# print(msg.isalpha())  # return True if the string consists of Alphas only [a-z]
# print(msg.isdigit())  # return True if the string consists of digits 09
#

""" ====> strip """
""" default behaviour --> strip white spaces """
msg = "             Hello world            "
print(msg)

print(msg.lstrip())  # strip whitespaces from the beginning of the string
print(msg.rstrip())  # strip whitespaces from the end of the string

""" strip chars ?"""

print(msg.strip(' dH')) #remove any space and any d from the begining and the end of the string

