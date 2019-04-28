user_input=input("inter any no")
i=0
even=[]
odd=[]
while i<user_input:
    if i%2==0:
        even.append(i)
    i=i+1
while user_input<100:
    if user_input%2 !=0:
        odd.append(user_input)
    user_input=user_input+1
print even
print odd