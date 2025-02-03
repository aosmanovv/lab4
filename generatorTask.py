def square(n):
    cnt=1
    while (cnt<=n):
        yield cnt*cnt
        cnt+=1
sq=square(5);
for i in sq:
    print(i)

def even(n):
    cnt=0
    while (cnt<=n):
        yield cnt
        cnt+=2
ev=even(int(input()))
for i in ev:
    print(i)

def tf(n):
    cnt=0
    while (cnt<=n):
        if (cnt%3==0 or cnt%4==0):
            yield cnt
        cnt+=1
for i in tf(10):
    print(i)

def squares(a,b):
    while (a<=b):
        yield a*a
        a+=1
sq=squares(4,12);
for i in sq:
    print(i)

def toZero(n):
    while(n>=0):
        yield n
        n-=1
for i in toZero(10):
    print (i)