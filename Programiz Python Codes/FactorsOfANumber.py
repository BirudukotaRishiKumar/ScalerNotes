import math
n=120
c1=0
#Brute Force Approach
for i in range(1,n+1):
    if(n%i==0):
        c1+=1
print("C1",c1)

#Optimized Approach
c2=0
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        c2+=1
        if i!=n/i:
            c2+=1
print("C2",c2)
