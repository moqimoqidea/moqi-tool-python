"""
参考网址：https://blog.csdn.net/qq_18192241/article/details/50486025
"""


def function_with_one_star(*para):
    print(para, type(para))


def function_with_two_starts(**para):
    print(para, type(para))


function_with_one_star(1, 2, 3)
print()

function_with_two_starts(a=1, b=2, c=3)
print()


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(2, 3))
print(multiply(2, 3, 4, 5, 6, 7, 8))
print()


def accept(**kwargs):
    for keyword, value in kwargs.items():
        print('%s => %s' % (keyword, value))


accept(foo='bar', spam='eggs')
print()


def add(a, b, c):
    return a + b + c


print(add(1, 2, 3))
print(add(a=4, b=5, c=6))
args = (2, 3)
print(add(1, *args))
kwargs = {'b': 8, 'c': 9}
print(add(a=7, **kwargs))

"""
(1, 2, 3) <class 'tuple'>

{'a': 1, 'b': 2, 'c': 3} <class 'dict'>

6
40320

foo => bar
spam => eggs

6
15
6
24
"""
