g = [[3,4,5,6],
        [4,0,0,6],
        [0,3,5,0],
        [6,4,2,0]]
        
i=0
sum=0

while i<len(g):
    j=0
    while (j<len(g[i])):
        if g[i][j]!=0 and g[i+1][j]!=0:
            sum=sum+ (g[i][j])
        if g[i+3][j]!=0 and g[i+2][j]!=0:
            sum=sum+g[i+3][j]
        j=j+1
    i=i+1
print (sum)