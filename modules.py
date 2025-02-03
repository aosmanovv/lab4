import mymodule
import mymodule as mx
import platform
# to import only one thing we use - from mymodule import person1 -> print (person1["age"])

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)

