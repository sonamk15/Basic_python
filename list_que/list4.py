# # def smallest_num_in_list( list ):
# #     min = list[ 0 ]
# #     print (min)
# #     for a in list:
# #         if a < min:
# #             min = a
# #     return min
# # print(smallest_num_in_list([1, 2, -8, 0]))
# list =[1,-4,2,-8,0]
# min = list[ 0 ]
# for a in list:
#     if a < min:
#         min = a
# print (min,"min")
# sec_min = list[ 0 ]
# for i in list:
#     if i>min and i<sec_min:
#         sec_min = i
# print (sec_min,"sec_min")

list =[1,2,0]
min = min(list)
print (min)
sec_min = list[ 0 ]
i = 0
while i <len(list):
    if list[i]>min and list[i]<sec_min:
        sec_min = list[i]
    i+=1
print (sec_min,"sec_min")

