a=[1,2,3,4,5,6,7,8]
A=[]
B=[]
i=0
while i<len(a):
    if a[i]==a[0] or a[i]==a[3]:
        A.append(a[i])
    else:
        B.append(a[i])
    i=i+1
print (A)
print (B)