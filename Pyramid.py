for i in range (0,10,2):
    for j in range(1,int((10-i)/2)):
        print("   ",end="")
    for j in range(1,i):
            print("",int(i/2),"",end="")
    print("\n")