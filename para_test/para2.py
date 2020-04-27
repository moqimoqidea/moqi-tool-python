"""
参考网址：https://www.cnblogs.com/arkenstone/p/5695161.html
"""


def foo(param1, *param2):
    print(param1)
    print(param2)


foo(1, 2, 3, 4, 5)
print()


def bar(param1, **param2):
    print(param1)
    print(param2)


bar(1, a=3, b=111)
print()


def foo2(bar, lee):
    print(bar, lee)


args = [1, 2]
foo2(*args)
print()


def foo3(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


foo3(1, 2, 3, 4, e=5, f=6, g=7)

"""
1
(2, 3, 4, 5)

1
{'a': 3, 'b': 111}

1 2

1
2
(3, 4)
{'e': 5, 'f': 6, 'g': 7}
"""
