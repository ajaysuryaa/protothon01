import math
num=input("Enter the numbers")
rms=num.split(",")
n=len(rms)
for i in range (n):
    rms[i]=int(rms[i])
for i in range (n):
    rms[i]*=rms[i]
    mean=sum(rms)/float(n)
    root=math.sqrt(mean)
print(root)    