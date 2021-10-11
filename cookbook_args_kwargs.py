"""
Description: args and kwargs showcase use in function def
"""


def example(var, * args, ** kwargs):
    print('Var value:', var)
    print('args:', args, 'type of args:', type(args))
    print('kwargs:', kwargs, 'type of kwargs:', type(kwargs))

    print('Accessing args:', args[0])
    print('Accessing kwargs', kwargs['numberone'])


if __name__ == "__main__":
    example('variable', 'a', 'b', 'c', 'd', 'e', numberone=1, numbertwo=2)  # args kwargs can accept infinite variables
