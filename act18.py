for i in range(0, 12, 1):
    if i<6:
        for j in range(0, i, 1):
            print("*", end=" ")
        print("")
    else:
        for k in range(10, i, -1):
            print("*", end=" ")
        print("")