num  = [4,5,120,55,76,9,99,6]
# num = [x for x in num if x%2 != 0]
# print (num)
i = 0
n=[]
while i<len(num):
    if num[i]%2 != 0:
        n.append(num[i])
    i+=1
print (n)



