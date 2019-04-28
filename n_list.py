number = [10,20,30,40]
new_list = [10,20,30,40]
new = []
i = 0
while(i < len(number)):
    x = i + 1
    while(x<len(number)-1):
        new_list.append([number[i],number[x]])
        # new.append([number[i],number[x],number[x+1]])
        x = x + 1
    i = i + 1# print(new_list)# print(new)

count = 0
while(count < len(number)):
    count1 = count + 1
    while(count1<len(number)-1):
        new_list.append([number[count],number[count1],number[count1+1]])
        count1 = count1 + 1
    count = count + 1
new_list.append(number)
print(new_list)



# number = [10,20,30,40]
# new_list = [10,20,30,40]
# new = []
# i = 0
# while(i < len(number)):
#     x = i + 1
#     while(x<len(number)-1):
#         new_list.append([number[i],number[x]])
#         # new.append([number[i],number[x],number[x+1]])
#         x = x + 1
#     i = i + 1# print(new_list)# print(new)

# count = 0
# while(count < len(number)):
#     count1 = count + 1
#     while(count1<len(number)-1):
#         new_list.append([number[count],number[count1],number[count1+1]])
#         count1 = count1 + 1
#     count = count + 1
# new_list.append(number)
# print(new_list)
    # [10, 20, 30, 40, [10,20], [10,30], [10,40], # [20, 30],[20,40], # [30,40], [10,20,30],# [10,30,40][20,30,40],[10,20,30,40]]
    # [10, 20, 30, 40, [10,20], [10,30], [10,40], # [20, 30],[20,40], # [30,40], [10,20,30],# [10,30,40][20,30,40],[10,20,30,40]]