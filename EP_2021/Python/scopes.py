promenna_1 = 987

print(promenna_1)

def foo():
    print(promenna_1)

def baz(param1):
    return param1 * 2

foo()
a = baz("a")
print(a)

param2 = "ahoj"

def baa(param2):
    print(promenna_1)
    print(param2)

baa(123)