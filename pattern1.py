n=4
for i in range(1, n+1):
    for j in range(1,n-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("x",end=" ")
    print()