lis=[[2,3,4],[3,2,5],[4,5,9]]
count=0
counter=0
sum=0
while count<len(lis):
    while counter<len(lis[count]):
        sum=sum+lis[count][counter]
        counter=counter+1
        break
    count=count+1
print sum
