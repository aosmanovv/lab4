def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc2():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc2()

x1 = 301

def myfunc():
    x1 = 200
    print(x1)

myfunc()

print(x1)


def myfunc():
    global x2   #make a global varible or change it to global
    x2 = 300

myfunc()

print(x)


def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())