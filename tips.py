""" known maximum number of iterations  --> for loop """
# for i in range(3):
#     password = input("please enter password: ")
#     if password=='abc':
#         break
#     else:
#         print("---- not valid passwordsd")


"""while loop---> unknown number of iterations """

# while True:
#     name = input("please enter name: ")
#     if name.isalpha():
#         print("-- name correct ")
#         break
#     print("---- not valid input ")



############################################




# for i in range(10):
#     # if i==4:
#     #     break
#     print(f'i = {i}')
#
# if i==9:
#     print("---- loop reached the end -----")





for i in range(3):
    password=  input("please enter password: ")
    if password=='abc':
        break

    print("----- not valid password")
else:
    """ this block will be executed only if the loop reached its end 
    the loop wasn't broken"""
    print("=---- your account has been locked")


"""
    if(){}
"""
name =input("----")
if name=='ahmed':
    pass


print("----")