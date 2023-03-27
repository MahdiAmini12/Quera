x_1,y_1,x_2,y_2 = input().split() # get input
#convert input strings to ints
x_1 = int(x_1)
x_2 = int(x_2)
y_1 = int(y_1)
y_2 = int(y_2)
if x_1 == x_2:
    print("Vertical")
elif y_1 == y_2:
    print("Horizontal")
else:
    print("Try again")
