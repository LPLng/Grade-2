from math import ceil
from math import sqrt
import time

startTime=time.time()
arr=[None]*1001;
for i in range(1001):
    if arr[i]!=1:
        arr[i]=i
arr[1]=0;
for i in range(2,ceil(sqrt(1000))):
    for j in range(i+1,1001):
        if arr[i]!=0 and arr[j]!=0:
            if arr[j]%arr[i]==0:
                arr[j]=0;
endTime=time.time()
print("筛选方法的时间是",endTime-startTime)

startTime=time.time()
arr=[]
for i in range(2,1001):
    count=0
    for j in range(2,i):
        if i%j!=0:
            count+=1
    if count==i-2:
        arr.append(i);
endTime=time.time()
print("正常方法的时间是",endTime-startTime)
