def outer():
    x = 10
    def inner():
        print(x)
    inner()
    x = 20
    return inner
f=outer()
f
print type(f)