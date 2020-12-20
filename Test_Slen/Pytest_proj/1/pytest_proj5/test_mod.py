import test1
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print("runns only when {} is imported".format("import test_mod"))
if __name__ == '__main__':
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)

import sys
print(f"module is imported {__name__}, script name is {sys.argv[0]}")
print(f"importlib.reload({__name__}")