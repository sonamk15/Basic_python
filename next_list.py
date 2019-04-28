# inpit [10,20,30,40]
# output [10,20][10,30][10,40][20,30][20,40][30,40]\
lists= [10,20,30,40]
n_list=[10,20,30,40]
new=[]
i=0
while (i<len(lists)):
    j=i+1
    while (j<len(lists)):
        n_list.append([lists[i],lists[j]])
        j=j+1
    i=i+1
print n_list
