a=[[1,2,3],
[4,5,6]]
i=0
s=0
new_list=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        s=s+a[i][j]
        j=j+1
    new_list.append(s)
    s=0
    i=i+1
print (new_list)

def distance(new_list):
    i=0
    while i<len(new_list):

        if new_list[i] >= new_list[i+1]:
            result = new_list[i] - new_list[i+1]
        else:
            result = new_list[i+1] - new_list[i]
        return result
a=distance(new_list)
print (a)
