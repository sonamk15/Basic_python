# a = [12,0,39,50,1]

# first = a[0]

# i = 0
# j = 1
# while i < len(a):
#     if a[i] < first:
#         tmp = a[i]
#         a[i] = a[j]
#         a[j] = tmp
#     i += 1

# print(a)
a=[12,0,39,50,1]
i=0
while i<len(a):
    key=i
    j=i+1
    while j<len(a):
        if a[key]>a[j]:
            key=j
        j+=1
    a[i],a[key]=a[key],a[i]

    i+=1
print(a)