lis=[[2,3,4],
    [3,8,5],
    [4,5,9]]
count=0
counter=-1
sum=0
sum1=0
while count<len(lis):
    while counter<len(lis[count]):
        sum=sum+lis[count][counter]
        counter=counter-1
        break
    count=count+1
print sum














# lis=[[2,3,4],[3,2,5],[4,5,9]]
# num=0
# num1=-1
# sum2=0
# sum1=0
# while num<len(lis):
#     while num<len(lis[num]):
#         sum2=sum2+lis[num][num]
#         sum1=sum1+lis[num1][num]
#     num1=num1-1
#     num=num+1
# print sum2
# print sum1