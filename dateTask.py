import datetime
a =datetime.datetime.now();
print(a-datetime.timedelta(5))

print(a-datetime.timedelta(1))
print(a)
print(a+datetime.timedelta(1))

print (a.microsecond)

b=(a-(a-datetime.timedelta(5)))
print(abs(b.total_seconds()))



