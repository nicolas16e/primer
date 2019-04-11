#%%
"""print("i am a comand, print me")
type(3)
y= 5.0+5.0
print(type(y))
type("a,b,c")
#%%
pi= 3.14
radius=11.2
area=pi*(radius**2)
radius=14.3
print(area)
area=pi*(radius**2)
print(area)

#%%
x,y=2,3
print("x =",x,"y=",y)
x=5
if x%2==0:
 print("even")
else:
    print("odd")
    print("done whit conditional")
#%%
x,y,z=1,3,1
if x<y:
    if x<z:
      print("x is least")
    else:
     print("x is second")
else:
     print("x is first")
#%%
if x<y and x<z:
    print("x is least")
elif y<z:
 print("y is least")
else:
 print("z is least")
#%%
type("a")
#%%
type(3*4.5)
#%%
type(())
#%%
type([])
#%%
type({})
#%%
name= input('enter your name: ')
print("are you really ", name, "?")
#%%
n=input("enter a int")
if type(n)==int:
 print(n,"is an integer")
else:
    print(n,"is NOT an integer") 

#%%
n=float(input("enter a int: "))
if type(n)==float:
     print(n,"is a float")
else:
       print(n,"is NOT an integer")
#%%
x=10
ans=0
itersleft=x
while(itersleft != 0):
    ans=ans+x
    itersleft=itersleft-1
print(x,"*",x,"=",ans)
print(str(x)+"*"+str(x)+"="+str(ans))
#%%
x=int(input("enter an integer: "))
ans=0
while ans**3<abs(x):
    ans=ans+1
if ans**3!=abs(x):
    print(x,"in not a perfect cube")
else:
    if x<0:
      ans=-ans
    print("cube root of",x,"is"+str(ans))

#%%
max=int(input("enter a positive integer "))
i=0
while i<max:
    i=i+1
    print(i)
#%%
x=10
for i,j in enumerate(range(5,x)):
    print("i=",i,"j=",j)
#%%
x=8
for i in range(x):
    print(i)
#%%
x=3
for j in range(x):
    for i in range(x):
        print(i)
        x=6
#%%
x=int(input("enter an integer: "))
for ans in range(abs(x)+1):
    if ans**3==abs(x):
       break
if ans**3!=abs(x):
    print(x, "is not a perfect cube")
else:
    if x<0:
     ans=-ans
    print("cube root of",x ,"is", ans)
#%%
x=0.25
ep=0.01
step=ep**2
nguess=0
ans=0
while abs(ans**2-x)>= ep and ans<=x:
    ans+=step
    nguess+=1
print("numguesses= ",nguess)
if abs(ans**2-x)>=ep:
    print("failed on square root of",x)
else:
 print(ans, "is close to square of", x)
#%%
x=0.9
ep=0.01
nguess=0
low=0
high=max(1,x)
ans=(high+low)/2
while abs(ans**2-x)>=ep:
    print("low=",low,"high=",high,"ans=",ans)
    nguess+=1
    if ans**2<x:
     low=ans
    else:
       high=ans
    ans=(high+low)/2
print("numguesses=",nguess)
print(ans,"is close to square of", x)
#%%
x=0
for i in range(10):
    x+=0.1
if x==1:
    print(x,"=1")
else:
    print(x,"is not 1")
    print(x==10*0.1)
#%%
x=0
for i in range(10):
    x+=0.1
if (1-x)<0.00001:
    print(1,"=1")
else:
    print(x,"is not 1")
    print(x==10*0.1)
#%%
# Newton-Raphson
ep=0.0001
y=45
guess=y/2
while abs((guess**2)-y)>=ep:
    guess=guess-(((guess**2)-y)/(2*guess))
print("square of",y, "is about", guess)
#%%
# functions
def max(x,y):
    if x>y:
     return x
    else:
     return y

max(7,9)
#%%
def printname(firstname,lastname,reverse=False):
    if reverse:
        print(lastname + "," + firstname)
    else:
        print(firstname, lastname)
printname("olga","toro", False)
printname("olga","toro",True)
printname("olga","toro",reverse=False)
printname("olga",lastname="toro")
#%%
def f(x):
    y=6
    x=x+y
    print("x=",x)
    return x
x=7
y=2
z=f(x)
print("z=",z)
print("x=",x)
print("y=",y)
#%%
def f(x):
    def g():
        x="abc"
        print("x=",x)
    def h():
        z=x
        print("z=",z)
    x+=1
    print("x=",x)
    h()
    g()
    print("x=",x)
    return g
x=3
z=f(x)
print("x=",x)
print("z=",z)
z()



No comprendi esta parte!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#%%
def findroot(x,power,ep):
    if x<0 and power%2==0:
          return None
    low=min(-1,x)
    print(type(x))
    high=max(1,x)
    ans=(high+low)/2
    while abs(ans**power-x)>=ep:
        if ans**power<x:
              low=ans
        else:
             high=ans
        ans=(high+low)/2
    return ans

def testfindroot():
    ep=0.0001
    for x in (0,25,-0,25,2,-2,8,-8):
        for power in range(1,4):
            print("testing x="+str(x)+"and power="+str(power))
            res =findroot(x,power,ep)
            if res==None:
                print("no root")
            else :
                print(''+str(res**power)+'cpolita de chanco='+str(x))
testfindroot()
help(findroot)

Hata aca!!!!!!!!!!!!!!!!

#%%
def facti(n):
    res=1
    while n>1:
        res=res*n
        n-=1
    return res

def factr(n):
    if n==1:
        return n
    return n*factr(n-1)

print(facti(6))
print(factr(5))
#%%
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def testfib(n):
    for i in range(n+1):
        print("fibonacci of", i ,"=",fib(i))

testfib(6)
#%%
def fib(n):
    global numcalls
    numcalls +=1
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def testfib(n):
    for i in range(n+1):
        global numcalls
        numcalls =0
        print("fibonacci of", i ,"=",fib(i))
        print("fibonacii called",numcalls,"times")

testfib(35)
#%%
mult3l=filter(lambda x:x%3==0,[1,2,3,4,5,6,7,8,9])
def filterfunc(x):
    return x%3==0
mult3n=filter(filterfunc,[1,2,3,4,5,6,7,8,9])
print(list(mult3l))
print(list(mult3n))
#%%
f= lambda x,y:x+y
print(f(2,3))
def f(x,y):
    return x+y
print (f(2,3))
#%%
def transform(n):
    return lambda x:x+n
f=transform(3) #da el valor de n
f(2) # da el valor de x"""
#%%
import numpy as np
help(np.arange)
arang=np.arange(10)
arang
#%%
import pandas as pd
data =pd.read_csv('Base.csv',sep=",", )
#%%
print(type(data))
data.head()

##### Para que es esta parte!!!!!!!!!!!!!!!!!!!