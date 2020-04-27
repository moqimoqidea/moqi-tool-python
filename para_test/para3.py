"""
参考网址：https://kodango.com/variable-arguments-in-python
"""

required_argumenet = 'Required argument:%d'
optional_argument = 'Optional argument:%d'


def test_defargs(one, two=2):
    print(required_argumenet % one)
    print(optional_argument % two)
    print()


test_defargs(1)
test_defargs(1, 3)


def test_args(first, *args):
    print(required_argumenet % first)
    for v in args:
        print(optional_argument % v)
    print()


test_args(1, 2, 3, 4)


def test_kwargs(first, *args, **kwargs):
    print(required_argumenet % first)
    for v in args:
        print('Optional argument (*args):%d' % v)
    for k, v in kwargs.items():
        print('Optional argument %s (**kwargs): %d' % (k, v))
    print()


test_kwargs(1, 2, 3, 4, k1=5, k2=6)


def test_args_unpack(first, second, third, fourth, fifth):
    print('First argument: %s' % first)
    print('Second argument: %s' % second)
    print('Third argument: %s' % third)
    print('Fourth argument: %s' % fourth)
    print('Fifth argument: %s' % fifth)
    print()


args = [1, 2, 3, 4, 5]
test_args_unpack(*args)

kwargs = {
    'first': 9,
    'second': 10,
    'third': 18,
    'fourth': 100,
    'fifth': 1000
}
test_args_unpack(**kwargs)

"""
Required argument:1
Optional argument:2

Required argument:1
Optional argument:3

Required argument:1
Optional argument:2
Optional argument:3
Optional argument:4

Required argument:1
Optional argument (*args):2
Optional argument (*args):3
Optional argument (*args):4
Optional argument k1 (**kwargs): 5
Optional argument k2 (**kwargs): 6

First argument: 1
Second argument: 2
Third argument: 3
Fourth argument: 4
Fifth argument: 5

First argument: 9
Second argument: 10
Third argument: 18
Fourth argument: 100
Fifth argument: 1000
"""
