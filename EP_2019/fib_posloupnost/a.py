def test(n):
    return n


def volej(fun):
    a = fun(5)
    return a


print(test(5))
print(test)

print(volej(test(5)))