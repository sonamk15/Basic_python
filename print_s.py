# i=0
for row in  range(7):
    for col in range(5):
        if (row==0 or row==3 or row==6) and (col>0 and col<4) or (col==0 and (row>0 and row<3)) or col==4 and (row>3 and row<6):
            print ("*",end="")
        else:
            print(end=' ')
    print ()
# # i=0
# for row in  range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or ((col>0 or col<4) and (row==0 or row==3)) :
#             print ("*",end="")
#         else:
#             print(end=' ')
#     print ()
    
# i=0
# while i<5:
#     if i==0 or i==2 or i==4:
#         print "  ****"
#     elif i==3:
#         print "      *"
#         print "      *"
#     else:
#         print " *"
#         print " *"
#     i=i+1
