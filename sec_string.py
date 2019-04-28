string="aaaaaaabbbbbccccddd"
a=0
b=0
c=0
d=0
count=0
while count<len(string):
    if string[count]=='a':
         a=a+1
    if string[count]=='b':
         b=b+1
    if string[count]=='c':
         c=c+1
    if string[count]=='d':
         d=d+1
    count=count+1
if a>b and b>c and c>d :
     print (b,'this is sec_max string')
else:
     print 'b is not sec string'
    

    