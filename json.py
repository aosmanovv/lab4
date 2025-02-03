import json5

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json5.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
y = json5.dumps(x)

# the result is a JSON string:
print(y)

print(json5.dumps({"name": "John", "age": 30}))
print(json5.dumps(["apple", "bananas"]))
print(json5.dumps(("apple", "bananas")))
print(json5.dumps("hello"))
print(json5.dumps(42))
print(json5.dumps(31.76))
print(json5.dumps(True))
print(json5.dumps(False))
print(json5.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json5.dumps(x,indent=5))
print(json5.dumps(x, indent=4, separators=(". ", " = ")))
print(json5.dumps(x, indent=4, sort_keys=True))

