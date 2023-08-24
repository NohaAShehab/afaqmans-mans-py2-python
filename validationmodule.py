# print("=========welcome to validation module =======")

def validateNum(var):
    if isinstance(var, int) or isinstance(var, float):
        return  True

    return  False


# print(validateNum('iti'))


def abc():
    print("---abc ----")
"""entry point __name__ = '__main__'"""

if __name__=='__main__':
    print('--- welcome to this module')
    print(validateNum(100))
