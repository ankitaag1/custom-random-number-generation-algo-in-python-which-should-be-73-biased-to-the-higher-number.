import math
import time
from datetime import datetime
s=input("enter starting value:max 6 digits:")
s1=int(s)
e=input("enter ending value:max 6 digits:")
e1=int(e)
h=input("enter how many random values to generate:")
h1=int(h)
half=int((e1+s1)/2)#find mid value in the range
high1=(73/100)*h1
low1=(27/100)*h1
f1,w1=math.modf(high1)
f2,w2=math.modf(low1)
if f1>=0.5 and f2<0.5:
    high=math.ceil(high1)
    low=math.floor(low1)
if f1<0.5 and f2>=0.5:
    high=math.floor(high1)
    low=math.ceil(low1)
if f1==0.5 and f2==0.5:
    high=math.ceil(high1)
    low=math.floor(low1)
count =0 #count no. of digits in the ending value
num=e1
while num > 0:
    num=int(num/10)
    count += 1
mor=0
les=0
while True:
    x=datetime.now().strftime("%H:%M:%S.%f")#get current system time
    x1=x[-6:]
    x2=x1[0:count]
    x3=int(x2)
    if x3>=s1 and x3<=e1:
        if x3>=half:
            mor=mor+1
            if mor<=high:
                print(x3)
            else:
                continue
        if x3<half:
            les=les+1
            if les<=low:
                print(x3)
            else:
                continue
     
                     




    
