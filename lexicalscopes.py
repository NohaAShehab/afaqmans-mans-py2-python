

course = 'python'  # global scope

""" local scope  --> any variable defined inside the function
scope --> localscope """
# def saywelcome():
#     name = 'Ali'  # local scope of the function
#     print(name)
#
# saywelcome()
# print("---------------")
# print(name)


""" global scope """

course = 'Django'
"you can access global variable anywhere in the script"


print(course)

# def printCourseInfo():
#     print(f"==>course = {course}")
#
# printCourseInfo()


# def modifycourse():
#     course = input('please enter new name for the course: ')  # define new local variable
#     print(f'in the function course = {course}')
#
# modifycourse()
# print(course)

""" to modify the global variable """
#
# def modifycourse():
#     global course
#     course = input('please enter new name for the course: ')  # define new local variable
#     print(f'in the function course = {course}')
#
# modifycourse()
# print(course)



"""-------------------------------function defined inside a function ------------------------------------------"""


# def myouterfun():
#     grade = 60 # local variable in the outerfunction
#     def formatgrade():
#         print(f"grade = {grade}")  # print the value from inner function
#     formatgrade()
#
#     def updategrade():
#         grade = input('please enter new grade: ')  # create new local variable for the updategrade func
#         print(f"--updated grade:{grade} ")
#     updategrade()
#     print(grade)
#     return grade
#
#
# print(myouterfun())


""" update local variable of the parent function """


def myouterfun():
    grade = 60 # local variable in the outerfunction
    def formatgrade():
        print(f"grade = {grade}")  # print the value from inner function
    formatgrade()

    def updategrade():
        nonlocal grade
        grade = input('please enter new grade: ')  # create new local variable for the updategrade func
        print(f"--updated grade:{grade} ")
    updategrade()
    print(grade)


myouterfun()







