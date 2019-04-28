for row in  range(7):
    for col in range(5):
        if (col<5 and (row==6 or row==0) or (row<7 and col==2)):
            print ("*",end="")
        else:
            print(end=' ')
    print ()