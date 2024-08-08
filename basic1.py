n=int(input())
temp=n
sum=0
while n>0:
    last=n%10
    fact=1
    for i in range(1,last+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==temp:
    print("strong number")
else:
    print("it is   not ")
    
        
    