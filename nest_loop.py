for row in  range(7):
    for col in range(5):
        if (row<7 and row==0 ) or ((row>0 or row<6)and col==1) or ((row>2 or row<4)and col==0) or ((row==3 and col==4)):
            print ("*",end="")
        else:
            print(end='  ')
    print ()