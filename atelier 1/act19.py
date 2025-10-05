space=""
temp=5
for i in range(10,0,-1):
    if i>5:
        space+=" "
        print(space, end=" ")
        for j in range(temp, 0, -1):
            print("*", end=" ")
        temp-=1
        print("")
    else:
        print(space, end=" ")
        for k in range(0, temp+1, 1):
            print("*", end=" ")
        temp+=1
        space=space[:-1]
        print("")
