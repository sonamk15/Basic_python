a=[1,2,3,4,5,6,7]
# i=0
# n=0
# j=a[0]

# while i<len(a):
#     if j>a[i]:
#         n.append(a[i])
#         break
#     i=i+1

i = 0
n = []
while i<len(a):
    if a[i]%2==0:
        n.append(a[i])
    else:
        n.insert(0,a[i])
    i = i + 1
print (n)